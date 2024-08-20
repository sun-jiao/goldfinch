import csv

if __name__ == '__main__':
    # 读取文件并处理数据
    bird_data = {}

    with open('bird_urls1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行尾的换行符并以第一个逗号分割行
            parts = line.strip().split(',', 1)

            if len(parts) < 2:
                continue

            key = parts[0].strip()
            urls = parts[1].strip()

            # 统计'http'的出现次数
            url_count = urls.count('http')

            # 如果key已存在于字典中，累加网址数量
            if key in bird_data:
                bird_data[key] += url_count
            else:
                bird_data[key] = url_count

    # 将结果保存到CSV文件
    with open('bird_urls_statistics.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # 写入表头
        csv_writer.writerow(['Key', 'URL Count'])

        # 写入数据
        for key, count in bird_data.items():
            csv_writer.writerow([key, count])

    print("结果已保存为bird_urls_statistics.csv文件。")
