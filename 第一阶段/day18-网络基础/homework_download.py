# @Author   :xaidc
# @Time     :2018/9/12 19:25
# @File     :homework_download.py
# 2. 下载网络图片
# （https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2808438283,4249462766&fm=26&gp=0.jpg）到本地
import requests
url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2808438283,4249462766&fm=26&gp=0.jpg'
response = requests.get(url)
data = response.content
with open('./files/new1.jpg','wb') as f:
    f.write(data)