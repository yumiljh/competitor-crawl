# -*- coding:utf-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

reload(sys)
sys.setdefaultencoding('utf-8')

browser = webdriver.Firefox()
urls = ['http://index.iresearch.com.cn/app/detail?id=1&Tid=66','http://index.iresearch.com.cn/app/detail?id=21&Tid=66','http://index.iresearch.com.cn/app/detail?id=41&Tid=66','http://index.iresearch.com.cn/app/detail?id=235&Tid=66','http://index.iresearch.com.cn/app/detail?id=40&Tid=66']
products = ['微信','应用宝','QQ邮箱','微信电话本','百度网盘']
print "艾瑞,月活(万)" 
for url,product in zip(urls,products):
	browser.get(url)
	time.sleep(3)
	yuehuo = browser.find_element_by_css_selector('.info.ng-binding:first-child').text
	print ("%s,%s"%(product,yuehuo))

browser.close()
