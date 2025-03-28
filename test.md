import os
from bs4 import BeautifulSoup
import requests

def extract_css_from_link(link_url):
    """从外部链接下载 CSS 内容"""
    try:
        response = requests.get(link_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch CSS from {link_url}. Status code: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Error fetching CSS from {link_url}: {e}")
        return ""

def merge_html(file1, file2, output_file):
    # 读取第一个 HTML 文件
    with open(file1, "r", encoding="utf-8") as f1:
        html1 = f1.read()

    # 读取第二个 HTML 文件
    with open(file2, "r", encoding="utf-8") as f2:
        html2 = f2.read()

    # 使用 BeautifulSoup 解析 HTML 内容
    soup1 = BeautifulSoup(html1, "html.parser")
    soup2 = BeautifulSoup(html2, "html.parser")

    # 提取第一个文件的 head 和 body
    head1 = soup1.head
    body1 = soup1.body

    # 提取第二个文件的 head 和 body
    head2 = soup2.head
    body2 = soup2.body

    # 创建一个新的 HTML 结构
    new_html = BeautifulSoup("<html><head></head><body></body></html>", "html.parser")
    new_head = new_html.head
    new_body = new_html.body

    # 从第一个文件提取 CSS 样式（如果有）
    # 提取 <style> 标签中的 CSS 样式
    if head1:
        style_tags = head1.find_all("style")
        for style_tag in style_tags:
            new_head.append(style_tag)

        # 提取 <link> 标签中外部 CSS 链接并下载内容
        link_tags = head1.find_all("link", {"rel": "stylesheet"})
        for link_tag in link_tags:
            css_url = link_tag.get("href")
            if css_url:
                css_content = extract_css_from_link(css_url)
                if css_content:
                    # 将外部 CSS 内容嵌入到 <style> 标签中
                    new_style_tag = new_html.new_tag("style")
                    new_style_tag.string = css_content
                    new_head.append(new_style_tag)

    # 按顺序将内容添加到新文件中
    if body1:
        new_body.append(body1)
    if head2:
        new_head.append(head2)
    if body2:
        new_body.append(body2)

    # 将合并后的 HTML 写入新文件
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(str(new_html))

# 文件路径
file1 = r"C:\Users\r\Desktop\test_webofsci\test_webofsci\ConvolutionalNeuralNetworks_1.html"
file2 = r"C:\Users\r\Desktop\test_webofsci\test_webofsci\ConvolutionalNeuralNetworks_2.html"
output_file = r"C:\Users\r\Desktop\test_webofsci\test_webofsci\combined.html"

# 调用合并函数
merge_html(file1, file2, output_file)

print(f"HTML files have been merged and saved to {output_file}")
