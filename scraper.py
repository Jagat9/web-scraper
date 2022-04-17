
import requests

from bs4 import BeautifulSoup


youtube_trending_page = 'https://www.youtube.com/feed/trending'

response = requests.get(youtube_trending_page)

print('status Code', response.status_code)
print("output", response.text[:1000])


with open('trending.html', 'w') as f:
  f.write(response.text)


doc = BeautifulSoup(response.text, 'html.parser')
print('page.title:',doc.title)

video_divs= doc.find_all('div', class_='ytd-video-renderer')

print(f'found{len(video_divs)}videos')