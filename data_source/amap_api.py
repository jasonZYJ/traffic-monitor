# coding = utf-8

"""
@author: sy

@file: amap_api.py

@time: 2018/6/3 18:59

@desc: 高德地图英文名称

    http://lbs.amap.com/api/webservice/gettingstarted 申请key值

    http://lbs.amap.com/api/webservice/guide/api/georegeo#geo 地理编码

    http://lbs.amap.com/api/webservice/guide/api/trafficstatus#road 指定线路交通态势

"""

import requests
from requests import RequestException
import json


# 获取地图信息类
class ReadMapInfo:

    # 请求url方法
    def request_url(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        try:
            r = requests.get(url=url, headers=headers)
            if r.status_code == 200:
                return r.text
            return None
        except RequestException:
            print('请求url返回错误异常')
            return None

    # 获取地理编码方法,args:城市、具体路段、开发者key
    def read_geo(self, city, address, key):
        """ 请求地理编码的url地址 """
        url = f'https://restapi.amap.com/v3/geocode/geo?city={city}&address={address}&&key={key}'
        r = self.request_url(url)
        result_json = self.parse_json(r)
        # 如果请求成功则进行处理,否则返回空,获取城市标识
        if result_json['status'] == '1':
            geocodes_list = list(result_json['geocodes'])
            geocodes_json = geocodes_list.pop()
            adcode = geocodes_json['adcode']
            return adcode
        else:
            return None

    # 获取指定路线交通趋势
    def read_road(self, city, address, key, select_road_mode):
        """ 根据客户端传入的标识选择不同的道路模式:rectangle(矩形),circle(圆形),road(指定路线)"""
        if select_road_mode == 'rectangle':
            pass
        if select_road_mode == 'circle':
            pass
        if select_road_mode == 'road':
            adcode = self.read_geo(city, address, key)
            """ 请求指定路线交通趋势的url地址 """
            url = f'https://restapi.amap.com/v3/traffic/status/road?name={address}&adcode={adcode}&level={level}&key={key}'
        r = self.request_url(url)
        print(r)

    # 解析json函数
    def parse_json(self, content_json):
        result_json = json.loads(content_json)
        return result_json


if __name__ == '__main__':
    readMapInfo = ReadMapInfo()
    readMapInfo.read_road('北京', '北京大厦', '')
