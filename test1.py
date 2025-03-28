import time
from bs4 import BeautifulSoup

def extract_and_insert_multiple(file1, output_file, start, end):
    # 读取第一个 HTML 文件
    with open(file1, "r", encoding="utf-8") as f1:
        html1 = f1.read()
    
    # 使用 BeautifulSoup 解析第一个 HTML
    soup1 = BeautifulSoup(html1, "html.parser")

    # 找到第一个文件中的 <app-records-list> 元素
    app_records_list = soup1.find("app-records-list")

    # 如果 <app-records-list> 元素存在
    if app_records_list:
        # 记录开始时间
        start_time = time.time()

        # 遍历第二个 HTML 文件，提取 <app-record> 元素并插入到第一个 HTML 文件中
        for i in range(start, end + 1):
            file2 = f"C:\\Users\\r\\Desktop\\test_webofsci\\test_webofsci\\ConvolutionalNeuralNetworks_{i}.html"
            try:
                # 记录每个文件处理的开始时间
                file_start_time = time.time()

                # 读取第二个 HTML 文件
                with open(file2, "r", encoding="utf-8") as f2:
                    html2 = f2.read()

                # 使用 BeautifulSoup 解析第二个 HTML 文件
                soup2 = BeautifulSoup(html2, "html.parser")

                # 提取第二个文件中的所有 <app-record> 元素
                app_records = soup2.find_all("app-record")

                # 将所有的 <app-record> 元素添加到 <app-records-list> 中
                for record in app_records:
                    app_records_list.append(record)

                # 计算当前文件的处理时间并打印
                file_end_time = time.time()
                file_duration = file_end_time - file_start_time
                print(f"Processed file {i}, time taken: {file_duration:.2f} seconds.")

            except FileNotFoundError:
                print(f"Warning: {file2} not found, skipping this file.")

            # 打印当前处理进度
            progress = (i - start + 1) / (end - start + 1) * 100
            print(f"Progress: {i - start + 1}/{end - start + 1} files processed ({progress:.2f}%).")

        # 将合并后的 HTML 写入新的文件
        with open(output_file, "w", encoding="utf-8") as out:
            out.write(str(soup1))

        # 计算总时间并打印
        end_time = time.time()
        total_duration = end_time - start_time
        print(f"\nApp records have been successfully extracted and inserted. The new HTML is saved to {output_file}")
        print(f"Total time taken: {total_duration:.2f} seconds.")

    else:
        print("Error: <app-records-list> not found in the first HTML.")

# 文件路径
file1 = r"C:\Users\r\Desktop\test_webofsci\test_webofsci\ConvolutionalNeuralNetworks_1.html"  # 第一个 HTML 文件
output_file = r"C:\Users\r\Desktop\test_webofsci\test_webofsci\ConvolutionalNeuralNetworks_1-50.html"  # 合并后的文件

# 调用合并函数，将第二个 HTML 文件从 2 到 50 合并到第一个文件
extract_and_insert_multiple(file1, output_file, start=2, end=10)
