import requests
from lxml import etree

from enum import Enum

class Data(Enum):
	AllData = 0
	DailyData = 1
	MonthlyData = 2

GiteeURL = 'https://gitee.com/explore/starred'

def getData():
	'''
	获取 Gitee 热门仓库的名称和描述
	'''
	html = requests.get(GiteeURL)
	et = etree.HTML(html.text)
	title = et.xpath('//a[@class="title project-namespace-path"]/text()')
	desc = et.xpath('//div[@class="project-desc"]/text()')
	return len(title), title, desc
