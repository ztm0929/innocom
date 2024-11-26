import csv
import requests
from bs4 import BeautifulSoup

# 打开CSV文件并读取内容
with open('data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过首行
    for row in reader:
        link = row[1]  # 获取链接
        url = 'http://www.innocom.gov.cn' + link  # 构建完整URL
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            div = soup.find('div', id='detailcontent') or soup.find('div', class_='fjjian')
            if div:
                print(div.text)  # 输出div内容
                # 查找PDF文件链接
                a_tag = div.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    pdf_link = a_tag['href']
                    # 增加一个错误捕获
                    try:
                        with open('get_pdf.csv', 'a', newline='', encoding='utf-8') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow([url, pdf_link])
                    except Exception as e:
                        print(f'写入CSV文件时出错: {e}')
                else:
                    print(f'未找到PDF链接: {url}')
            else:
                print(f'未找到内容: {url}')
        else:
            print(f'无法访问链接: {url}')