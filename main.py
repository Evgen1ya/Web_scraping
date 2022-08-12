import bs4
import requests

HEADERS = {'Cookie': '_ym_d=1648471216; _ym_uid=164847121697127284; fl=ru; hl=ru; _ga=GA1.2.341794629.1648471217; habr_web_home_feed=/all/; _ym_isad=1; _gid=GA1.2.1527596466.1660286500; _gat_gtag_UA_726094_1=1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'habr.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
response = requests.get("https://habr.com/ru/all/", headers=HEADERS)
text = response.text

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('div', class_='tm-article-snippet')
print(len(articles))
for article in articles:
    # preview = article.find('div', class_="article-formatted-body article-formatted-body article-formatted-body_version-1")
    # preview_2 = article.find('div', class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    header = article.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2")
    date = article.find('span', class_="tm-article-snippet__datetime-published")
    article_tag_a = header.find('a')
    href = article_tag_a.attrs['href']
    url = 'https://habr.com' + href
    preview_text = article.find_all('p')
    # print(header.text)
    # print(date.text)
    # print(url)
    # print(preview_text)
    for preview in preview_text:
        for el in preview:
            # print(el)
            for word in KEYWORDS:
                if word in el:
                    # print(word)
                    print(f'{date.text} --- {header.text} --- {url}')
                    print('------------------------------------------')



