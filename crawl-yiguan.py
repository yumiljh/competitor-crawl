# -*- coding:utf-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def func(product):
	url = 'http://zhishu.analysys.cn/public/view/wSearch/wSearch.html?words='+product
	browser.get(url)
	time.sleep(3)
	temp = browser.find_elements_by_css_selector('.m-table tr:nth-child(1) .data-nums .items-l')
	print("%s,%s,%s"%(product,temp[0].text,temp[1].text))

browser = webdriver.Firefox()
products = ['微信','应用宝','QQ邮箱','微信电话本','百度网盘']
print "易观,日活(万),月活(万)"
for x in products:
	func(x)
browser.close()
