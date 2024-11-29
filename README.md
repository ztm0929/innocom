# innocom

一个数据爬取与清洗练习，处理高企认定网站的数据与文件

## 题目

> 1. 打开 [http://www.innocom.gov.cn/gqrdw/c101318/list_gsgg.shtml](http://www.innocom.gov.cn/gqrdw/c101318/list_gsgg.shtml)
>  
> 2. 利用爬虫技术，对公示公告中的56页数据中的每一个进行数据爬取。例如， 北京市认定机构:关于北京市2024年第四批高新技术企业更名的通知中的pdf文件和标题中可以获取，企业原名称，企业现名称，证书编号，发证日期省份为北京市，类型是更名，发布时间为20241008，链接为[http://www.innocomgov.cn/gqrdw/c101486/202410/dcbf1625f26e4405b10595b8c0b8eccc.shtml](http://www.innocomgov.cn/gqrdw/c101486/202410/dcbf1625f26e4405b10595b8c0b8eccc.shtml).发文日期为20240926，认定机构等
>  
> 3. 将这些公开数据的公共字段进行打平，并可以入到数据库中，没有的字段置为空，并且可以支持每天更新
>  
> 4. 将上述功能写成一个demo，语言支持java和python.并能给出可以每天更新数据库的技术方案。

## 基本思路探索

1. 每篇公示公告都是网页，因此先存下标题和链接以备后用；

2. 网页内的文本各不相同，但必定有一份同名的PDF，需要将PDF的下载地址取到以备后用，接下来的重点就是定义PDF的类别从而方便内容整理；

3. 公示较简单，只有备案公示；公告较复杂，有认定备案公告、企业更名公告、取消高企资格公告、异地搬迁公告和问题中介机构公告；

4. **数据库的库表结构设计**🤔

announcements 表一：公告公示表，存放所有公告公示的标题、链接及发布时间

| 列名       | 数据类型     | 允许为空 | 默认值 | 备注           |
|------------|--------------|----------|--------|----------------|
| id         | INT          | 否       |        | 自增序号       |
| unique_id  | VARCHAR(255) | 否       |        | 主键，链接中的唯一ID |
| title      | VARCHAR(255) | 否       |        | 标题           |
| link       | VARCHAR(255) | 否       |        | 链接           |
| published_at | TIMESTAMP  | 否       |        | 发布时间       |

detail 表二：详情表，存放公告公示的详情，每一条记录对应一次公告公示，公共字段必填

| 列名       | 数据类型     | 允许为空 | 默认值 | 备注           |
|------------|--------------|----------|--------|----------------|
| id         | INT          | 否       |        | 自增序号       |
| unique_id  | VARCHAR(255) | 否       |        | 主键，链接中的唯一ID |
| 企业名称      | VARCHAR(255) | 否       |        |            |
| 证书编号       | VARCHAR(255) | 否       |        |            |
| 发证日期 | TIMESTAMP  | 否       |        | 发布时间       |
| 公告类别 |   | 否       |        | 备案、更名（迁入）、取消等       |
| 原企业名称 |   | 否       |        | 如果是更名（迁入），则必填       |
| 变更后企业名称 |   | 否       |        | 如果是更名（迁入），则必填       |
| 取消年度 |   | 否       |        | 如果是取消，则必填       |
