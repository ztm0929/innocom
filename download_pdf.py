import requests
import csv

# 打开CSV文件并读取内容，第一列是链接，第二列是唯一ID，通过直接链接下载PDF文件存放到pdf文件夹下
with open('get_pdf.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]  # 获取链接
        unique_id = row[1]  # 获取唯一ID
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'pdf/{unique_id}.pdf', 'wb') as pdf_file:
                pdf_file.write(response.content)
        else:
            print(f'无法访问链接: {url}')