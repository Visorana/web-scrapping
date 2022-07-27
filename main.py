import requests
import bs4

base_url = 'https://habr.com/'
url = base_url + '/ru/all'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    'Cookie': '_ym_d=1657965832; _ym_uid=1657965832665644792; _ga=GA1.2.616269460.1657965832; fl=ru; hl=ru; '
              'visited_articles=531472:254773:203282; _gid=GA1.2.1058816089.1658605017; habr_web_home_feed=/all/; '
              '_ym_isad=1',
    'Accept Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,sv;q=0.6,zh-CN;q=0.5,zh;q=0.4,ko;q=0.3',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'sec-ch-ua-mobile': '?0'
}

response = requests.get(base_url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet')
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        for key in KEYWORDS:
            if key in hub.lower():
                href = article.find(class_='tm-article-snippet__title-link').attrs['href']
                title = article.find('h2').find('span').text
                date = article.find('time').attrs['title']
                result = f"{(date.split(',')[0])} - {title} - {base_url}{href}"
                print(result)

