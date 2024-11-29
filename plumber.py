import pdfplumber
import re
import csv

with pdfplumber.open(r"pdf\3f365e09713b48c8bb52cc8bbc58dd4f.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())

    # pattern = re.compile(r'(\d+)\s+([\u4e00-\u9fa5（）()、]+)\s+(GR\d{12})')
    # matches = pattern.findall(first_page.extract_text())

    # # 写入CSV文件
    # with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerow(['序号', '企业名称', '证书编号'])
    #     for match in matches:
    #         csvwriter.writerow(match)

    # print("数据已成功写入 output.csv 文件")