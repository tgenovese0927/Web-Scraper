from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

chrome_driver_path = "D:\prjects\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.gamesradar.com/news/")

articles = driver.find_elements(By.CLASS_NAME, 'article-name')

with open('game_news.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile)
    for article in articles:
        filewriter.writerow(["{}".format(article.text)])

driver.close()
