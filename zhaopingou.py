import time
import urllib.request
from urllib import parse

from lxml import etree


class ZhaopinGou(object):
    def __init__(self):
        self.base_url = 'http://qiye.zhaopingou.com/resume?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 第一层解析  http://qiye.zhaopingou.com/resume/detail?resumeId=30970515
        self.first = '//*[@id="wrapDiv"]/div//div[4]//a/@href'
        self.seconde = '//*[@id="resume_information_center"]/div[1]'
        # http: // qiye.zhaopingou.com/  +self.first(resume/detail?resumeId=30970515)

    # 发送请求
    def send_request(self,url):
        time.sleep(1)
        request = urllib.request.Request(url,headers=self.headers)
        # 发送请求，获取响应 读取数据
        response = urllib.request.urlopen(request)
        data = response.read().decode('utf-8')
        # print(data)
        # 返回数据
        return data

    # 解析数据
    def analysis(self,data,xpathStr):
        # 转换类型 可解析的类型
        html_data = etree.HTML(data)
        # 解析
        result_list = html_data.xpath(xpathStr)
        return result_list
    # 保存文件
    def write_file(self,data,page,):
        file_path = 'pages/' + page +'页'
        with open(file_path,'w') as f:
        # with open('zhaop.html','w') as f:
            f.write(data)
    # 运行
    def run(self):
        for page in range(1,36):
            page = str(page)
            params = {
                "job":"1037",
                "pn":'1'
            }
            # 拼接参数
            # 转译参数
            print(page)
            params_str = parse.urlencode(params)
            new_url = self.base_url + params_str
            # 发送请求
            data = self.send_request(new_url)
            # 解析数据
            data_first = self.analysis(data,self.first)
            for url_child in data_first:
                first_url = 'http://qiye.zhaopingou.com/'+url_child
                data = self.send_request(first_url)


            # # 保存文件
            self.write_file(data,page)

if __name__ == '__main__':
    foo = ZhaopinGou()
    foo.run()