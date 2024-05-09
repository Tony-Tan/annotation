import json
import os
from generate_page import generate_page
from generate_home_page import generate_home
from shutil import copyfile


def read_json(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)


def generate_website(json_file, output_dir):

    data = read_json(json_file)
    copyfile('./style.css', output_dir + '/style.css')
    copyfile('./interactive.js', output_dir + '/interactive.js')
    # 生成主页
    generate_home(json_file, os.path.join(output_dir, "index.html"))
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for algo in data["algorithms"]:
        algo_name = algo["name"]
        script_path = algo["script_path"]
        output_html_path = os.path.join(output_dir, f"{algo_name}.html")

        # 生成每个算法的HTML页面
        generate_page(script_path, output_html_path)


# 调用函数
if __name__ == '__main__':
    generate_website('./examples/algs_path.json', './temp')

