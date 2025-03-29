
import requests
from bs4 import BeautifulSoup
import os
import re

# 假设这是你从网页获取的 HTML 内容（你可以通过 requests 获取网页 HTML）
html_content = '''
<html>
    <body>
        <a href="http://example.com/10.1000/182/file1.pdf" data-pendo="green_submitted_link_summary">File 1</a>
        <a href="http://example.com/10.1000/183/file2.pdf" data-pendo="other_link_summary">File 2</a>
    </body>
</html>
'''

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, 'html.parser')

# 找到具有 data-pendo="green_submitted_link_summary" 属性的 <a> 标签
link = soup.find('a', {'data-pendo': 'green_submitted_link_summary'})

# 如果找到了该链接
if link and link.get('href'):
    file_url = link['href']
    print(f"找到文件链接: {file_url}")

    # 提取 DOI 号，假设 DOI 号格式为 http://example.com/{DOI}/{filename}.pdf
    doi_match = re.search(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+', file_url, re.IGNORECASE)
    if doi_match:
        doi_number = doi_match.group(0)  # 提取 DOI
        print(f"提取的 DOI 号: {doi_number}")

        # 使用 DOI 号作为文件名
        file_name = f"{doi_number}.pdf"
        
        # 使用 requests 下载文件
        try:
            response = requests.get(file_url)

            # 检查请求是否成功
            if response.status_code == 200:
                # 确认文件是 PDF（可以通过文件扩展名或 MIME 类型进行检查）
                if file_url.lower().endswith('.pdf') or 'application/pdf' in response.headers.get('Content-Type', ''):
                    # 以二进制模式保存文件
                    with open(file_name, 'wb') as file:
                        file.write(response.content)
                    print(f"文件已成功下载并保存为 {file_name}")
                else:
                    print("文件不是 PDF 格式")
            else:
                print(f"下载失败，状态码: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"请求过程中发生错误: {e}")
    else:
        print("未从 URL 中提取到 DOI 号")
else:
    print("未找到对应的链接")
