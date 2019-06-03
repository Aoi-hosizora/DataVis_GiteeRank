import requests
from lxml import etree

from enum import Enum

class WebSite(Enum):
	Gitee = 0
	Github = 1
	Csdn = 2


GiteeURL = 'https://gitee.com/explore/starred'
GithubURL = 'https://github.com/trending?since=daily'

def getData(opt):
	'''
	获取:
	Gitee / Github 热门仓库的名称和描述
	Csdn 热门帖标题
	'''
	
	def removeSpAndNull(l):
		'''
		去除 List 内的空字符串与空项
		'''
		l = [li.strip() for li in l]
		while '' in l:
			l.remove('')
		return l

	if opt == WebSite.Gitee:
		html = requests.get(GiteeURL)
		et = etree.HTML(html.text)
		title = et.xpath('//a[@class="title project-namespace-path"]/text()')
		desc = et.xpath('//div[@class="project-desc"]/text()')
		return len(title), title, desc

	elif opt == WebSite.Github:
		html = requests.get(GithubURL)
		et = etree.HTML(html.text)

		title = et.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom"]/div[@class="d-inline-block col-9 mb-1"]//a/text()')
		title = removeSpAndNull(title)

		desc = et.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom"]/div[@class="py-1"]//p/text()')
		desc = removeSpAndNull(desc)
		return len(title), title, desc
		
	elif opt == WebSite.Casn:
		pass
	
