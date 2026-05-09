import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_imdb_to_10000(target=10000):
    # 1. Setup Chrome with 'Anti-Detection' settings
    options = Options()
    # options.add_argument("--headless") # Switch off if you get 0 results to see what's happening
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
    #url = "https://www.imdb.com/search/title/?release_date=2024-01-01,2024-12-31&sort=num_votes,desc"
    url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31&sort=num_votes,desc"
    driver.get(url)
    
    wait = WebDriverWait(driver, 20)
    all_movies = []
    csv_path = r"C:\Users\Niruban\Documents\Suriya\HCLGUVI\movie_recommendation_project\full_movies_2024.csv"

    try:
        while len(all_movies) < target:
            # Wait for items to be visible
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ipc-metadata-list-summary-item")))
            
            # Find all movie blocks currently on the page
            items = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")
            
            # Process only the NEW items we haven't scraped yet
            for i in range(len(all_movies), len(items)):
                if len(all_movies) >= target: break
                
                try:
                    item = items[i]
                    name = item.find_element(By.CLASS_NAME, "ipc-title__text").text
                    
                    # Some movies might lack ratings or storylines in early 2024
                    try:
                        story = item.find_element(By.CLASS_NAME, "ipc-html-content-inner-div").text
                    except:
                        story = "N/A"
                        
                    try:
                        rating = item.find_element(By.CLASS_NAME, "ipc-rating-star--rating").text
                    except:
                        rating = "Unrated"

                    all_movies.append({
                        "Movie Name": name,
                        "Storyline": story,
                        "Rating": rating
                    })
                except Exception:
                    continue

            print(f"Current Count: {len(all_movies)} / {target}")

            # SCROLL AND CLICK "LOAD MORE"
            if len(all_movies) < target:
                try:
                    # Scroll to bottom to trigger the button
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    
                    # Find and click the 'See More' button
                    load_more = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ipc-see-more__button")))
                    driver.execute_script("arguments[0].click();", load_more)
                    
                    # Wait for new data to load
                    time.sleep(4) 
                except Exception as e:
                    print("Reached the end of the list or button missing.")
                    break

        # Final Export
        df = pd.DataFrame(all_movies)
        df.to_csv(csv_path, index=False)
        print(f"Success! {len(df)} movies saved.")

    finally:
        driver.quit()

scrape_imdb_to_10000(10000)


