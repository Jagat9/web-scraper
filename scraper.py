
from selenium import webdriver

youtube_trending_page = 'https://www.youtube.com/feed/trending'

driver = webdriver.Chrome()

driver.get(youtube_trending_page)

print('page title', driver.title)

