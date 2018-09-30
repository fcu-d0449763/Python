# @Author   :xaidc
# @Time     :2018/9/12 16:53
# @File     :05-http请求.py
import requests

if __name__ == '__main__':
    # 1.准备url
    url = 'https://www.apiopen.top/satinApi?type=1&page=1'

    # 2.发送请求(GET)
    '''
    get(url,参数对应的字典)
    post(url,参数对应的字典)
    返回值是服务器返回的响应
    '''
    response = requests.get(url)
    # requests.get('https://www.apiopen.top/satinApi',{'type':1,'page':1})
    print(response)

    # 3.通过响应获取服务器返回的数据
    # a.获取字符串类型的数据
    print(response.text)

    # b.获取json格式的数据
    print(response.json())
    print(response.json()['msg'])

    # c.获取二进制格式的数据
    print(response.content)

    print(response.headers)