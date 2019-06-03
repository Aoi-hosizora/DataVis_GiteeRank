import requests
from lxml import etree

from enum import Enum

class WebSite(Enum):
	Gitee = 0
	Github = 1
	Csdn = 2


GiteeURL = 'https://gitee.com/explore/starred'
GithubURL = 'https://github.com/trending?since=daily'
CsdnPartURL = 'https://www.csdn.net/gather/'

class GetDataNetWorkException(Exception):
	def __init__(self, website):
		Exception.__init__(self)
		self.website = website  

	def printErrorMsg(self):
		print("> Get data from {} network error".format(self.website))

def printGetDataSuccess(website):
	print("> Get data from {} finish".format(website))

def getData(opt):
	'''
	获取:
	Gitee / Github 热门仓库的名称和描述，返回 len(desc), title, desc
	Csdn 热门帖标题，len(desc), title(Null), desc
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
		try:
			html = requests.get(GiteeURL)
		except:
			raise GetDataNetWorkException("Gitee")
		
		et = etree.HTML(html.text)
		title = et.xpath('//a[@class="title project-namespace-path"]/text()')
		desc = et.xpath('//div[@class="project-desc"]/text()')
		printGetDataSuccess('Gitee')

	elif opt == WebSite.Github:
		try:
			html = requests.get(GithubURL)
		except:
			raise GetDataNetWorkException("Github")

		et = etree.HTML(html.text)
		title = et.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom"]/div[@class="d-inline-block col-9 mb-1"]//a/text()')
		title = removeSpAndNull(title)

		desc = et.xpath('//li[@class="col-12 d-block width-full py-4 border-bottom"]/div[@class="py-1"]//p/text()')
		desc = removeSpAndNull(desc)
		printGetDataSuccess('Github')
		
	elif opt == WebSite.Csdn:
		title = []
		desc = []
		for i in range(ord('A'), ord('Z') + 1):
			try:
				CsdnURL = CsdnPartURL + chr(i)
				html = requests.get(CsdnURL)
			except:
				raise GetDataNetWorkException("Csdn")

			et = etree.HTML(html.text)
			desc += et.xpath('//ul[@class="tag_list_wrap"]//a/text()')

		printGetDataSuccess('Csdn')

	return len(desc), title, desc
