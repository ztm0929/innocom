import requests
from bs4 import BeautifulSoup
import csv

# 基础URL
base_url = 'http://www.innocom.gov.cn/gqrdw/c101318/list_gsgg_{}.shtml'
first_page_url = 'http://www.innocom.gov.cn/gqrdw/c101318/list_gsgg.shtml'
# url_1 = 'http://www.innocom.gov.cn/gqrdw/c101333/list_gsgg_l2.shtml' # 公示列表
# url_2 = 'http://www.innocom.gov.cn/gqrdw/c101334/list_gsgg_l2.shtml' # 公告列表

def fetch_page(url):
    """获取网页内容并返回BeautifulSoup对象"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser')

def parse_page(soup):
    """解析页面内容，提取标题和链接"""
    data = []
    column_list = soup.find('div', class_='column-list')
    list = column_list.find('ul', class_='list')
    lis = list.find_all('li')
    for li in lis:
        a = li.find('a')
        href = a['href']
        title = a.get_text()
        data.append([title, href])
    return data

def scrape_data():
    """爬取所有页面的数据并保存到CSV文件"""
    all_data = []

    # 处理第一页
    print(f'正在处理: {first_page_url}')
    soup = fetch_page(first_page_url)
    page_data = parse_page(soup)
    all_data.extend(page_data)

    # 处理剩余页面
    for page_num in range(2, 57):  # 页码从2到56
        current_url = base_url.format(page_num)
        print(f'正在处理: {current_url}')
        soup = fetch_page(current_url)
        page_data = parse_page(soup)
        all_data.extend(page_data)

    # 将数据写入CSV文件
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Link'])
        writer.writerows(all_data)

    print(f'总条数: {len(all_data)}')