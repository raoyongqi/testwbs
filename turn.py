import re

# 从本地文件读取 JavaScript 代码
file_path = "immersive-translate-sdk-latest.js"  # 请替换为你的 JS 文件路径
output_file_path = "output_userscript_domains.js"  # 保存提取后的 JS 数组的文件路径

with open(file_path, "r", encoding="utf-8") as js_file:
    js_code = js_file.read()

# 使用正则表达式提取 userscript_domains 字符串中的内容
match = re.search(r"userscript_domains:'(\[.*?\])'", js_code)

# 如果找到了匹配项
if match:
    # 提取的字符串是一个JSON格式的数组，将其转换为 Python 列表
    domains_str = match.group(1)  # 取出捕获的部分
    # 将字符串解析为 Python 列表
    domains_list = eval(domains_str)

    # 格式化为 JS 数组，每个域名一行
    js_array_str = "const userscript_domains = [\n"
    js_array_str += ",\n".join(f'"{domain}"' for domain in domains_list)
    js_array_str += "\n];\n"

    # 将格式化后的字符串写入新的 JS 文件
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(js_array_str)

    print(f"Extracted userscript_domains saved to {output_file_path}")
else:
    print("No matching userscript_domains found.")
