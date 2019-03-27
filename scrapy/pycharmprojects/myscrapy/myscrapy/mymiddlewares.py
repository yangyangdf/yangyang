from selenium import webdriver
import time
from scrapy.http import HtmlResponse

class MyscrapyDownloaderMiddleware(object):

    def process_request(self, request, spider):
        if request.meta.get('hpjs'):
            driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
            driver.get(request.url)
            time.sleep(2)
            content = driver.page_source

            return HtmlResponse(url=request.url,body=content,encoding='utf-8',request=request)