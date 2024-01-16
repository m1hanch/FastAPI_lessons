import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# def get_news():
#     # URL from which to fetch the HTML content
#     url = 'https://ua.korrespondent.net/all/world/'  # Replace with your actual URL
#
#     # Send a GET request to the URL
#     response = requests.get(url)
#
#     # Check if the request was successful
#     if response.status_code == 200:
#         html_content = response.text
#
#         # Parse the HTML content
#         soup = BeautifulSoup(html_content, 'html.parser')
#
#         # Find all article elements
#         articles = soup.find_all('div', class_='article')
#
#         # Create a list to hold article data
#         article_list = []
#         #print(articles)
#         count = 0
#         # Extract information from each article
#         for article in articles:
#             title = article.find('div', class_='article__title').get_text(strip=True)
#             print(title)
#             img_tag = article.find('img', class_='article__img')
#             if img_tag:
#                 img_link = img_tag.get('src')
#                 if img_link.endswith('/i/blank.gif'):
#                     img_link = img_tag.get('data-href', None)
#             else:
#                 img_link = None
#             article_text = article.find('div', class_='article__text').get_text(strip=True)
#             article_date = article.find('div', class_='article__date').get_text(strip=True)
#             source = article.find('div', class_='article__title').find('a')['href']
#             article_data = {
#                 'title': title,
#                 'img_link': img_link,
#                 'text': article_text,
#                 'date': article_date,
#                 'source': source
#             }
#             article_list.append(article_data)
#
#         # Convert list to JSON
#         json_result = json.dumps(article_list, indent=4, ensure_ascii=False)
#
#         # Print JSON result
#         return json_result
#     else:
#         return None
#
#
# print(get_news())
def get_news():
    url = "https://warsawexpo.eu/kalendarz-targowy/"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    trades = soup.find_all('div', class_='single-callendar-event')
    data = []
    for trade in trades:
        content_link = trade.find('a').get('href')
        response = requests.get(content_link)
        response.encoding = 'utf-8'
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find('h1').text
        date = soup.find('div', class_='h5').text
        title = title.split(' - ')
        data.append({
            'title': title[0],
            'description': title[1],
            'date': date
        })
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    excel_path = 'events.xlsx'
    df.to_excel(excel_path, index=False)
    # with open('trades.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f, ensure_ascii=False, indent=4)

get_news()



