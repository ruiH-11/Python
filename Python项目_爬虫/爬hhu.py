# 导入所需库
import requests  # 用于发送HTTP请求的核心库
from bs4 import BeautifulSoup  # HTML解析库
from urllib.parse import urljoin  # 用于拼接URL路径
import os  # 文件系统操作
import random
import time
from datetime import datetime  # 日期格式化处理

#宏定义基础变量
BASE_URL = "https://gs.hhu.edu.cn/17264/list"      # 基础URL地址
SAVE_PATH = r"D:\Python-code\news_data.txt"       # 数据保存路径
MAX_ITEMS =5   # 最大抓取数量
DELAY_RANGE = (1, 3)    # 请求延迟范围

# 请求头
headers = {
    # 模拟浏览器的标准User-Agent
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    # 保持Host头与目标网站一致
    "Host": "gs.hhu.edu.cn"
}


#请求访问网站函数
def enhanced_request(url):

    try:
        # 生成随机延迟
        delay = random.uniform(*DELAY_RANGE)
        time.sleep(delay)

        # 发送GET请求
        response = requests.get(url, headers=headers, timeout=10)
        # 强制设置UTF-8编码
        response.encoding = 'utf-8'
        return response
    except Exception as e:
        # 基础异常处理
        print(f"请求失败: {str(e)}")
        return None

#主抓取函数
def get_recent_news():
    count = 0  # 成功抓取计数器
    page = 1  # 起始页码
    # 分页循环控制
    while count < MAX_ITEMS:
        # 构造分页URL
        url = f"{BASE_URL}{page}.htm" if page > 1 else f"{BASE_URL}.htm"
        print(f"抓取页面: {url}")
        # 发送请求
        response = enhanced_request(url)
        # 响应有效性检查
        if not response or response.status_code != 200:
            break  # 保持原有中断逻辑

        # 使用lxml解析器
        soup = BeautifulSoup(response.text, 'lxml')
        # CSS选择器定位新闻条目
        items = soup.select('ul.news_list.list2 > li')

        # 遍历新闻条目
        for item in items:
            # 数量控制
            if count >= MAX_ITEMS:
                break

            # 标题元素提取
            title_tag = item.select_one('.news_title a')
            # 日期元素提取
            date_tag = item.select_one('.news_meta')

            # 数据字典构建
            news_data = {
                # 标题文本处理
                "标题": title_tag.get_text(strip=True) if title_tag else "无标题",
                # 链接拼接
                "链接": urljoin(BASE_URL, title_tag['href']) if title_tag else "",
                # 日期格式化
                "日期": datetime.strptime(date_tag.text, "%Y-%m-%d").strftime("%Y年%m月%d日") if date_tag else ""
            }

            # 调用保存函数
            save_to_file(news_data)
            count += 1  # 计数器递增

        page += 1  # 页码递增

#存储函数
def save_to_file(data):

    try:
        # 使用追加写入模式
        with open(SAVE_PATH, 'a', encoding='utf-8') as f:
            # 保持原始数据拼接格式
            entry = f"标题：{data['标题']}\n链接：{data['链接']}\n日期：{data['日期']}\n{'-' * 50}\n"
            f.write(entry)  # 保持原有写入方式
        # 保持原始成功提示
        print(f"已保存：{data['标题'][:15]}...")
    except Exception as e:
        # 保持原始错误处理
        print(f"保存失败: {str(e)}")


#主程序
if __name__ == "__main__":
    # 启动时删除旧数据
    if os.path.exists(SAVE_PATH):
        os.remove(SAVE_PATH)
    # 执行主抓取函数
    get_recent_news()
    print(f"最新{MAX_ITEMS}篇内容已保存至：{os.path.abspath(SAVE_PATH)}")