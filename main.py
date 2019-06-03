import getData as data
import getToken as token
from wordcloud import WordCloud

import sys
import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

font = {
	'family' : 'SimHei',
	'weight' : 'regular',
	'size'   : '11'
}
plt.rc('font', **font)
plt.rc('axes', unicode_minus=False)

SupTitle_Size = 18

BarVal_FontSize = 10
Bar_Rot = 75

WC_Height = 500
WC_Width = 2000

BarPar_Color = 'rgbycm' # bgrcmykw

def analyse(tokens, tokencnt, percnt, title):
	'''
	分析 tokens 列表生成
	词云图，柱状图, 圆饼图
	'''
	gs = gridspec.GridSpec(2, 3)
	src = {}
	for t in tokens:
		if src.get(t) == None:
			src[t] = 1
		else:
			src.update({t: src.get(t) + 1})
	
	src = dict(sorted(src.items(), key=lambda v: (v[1], v[0]), reverse=True)[0: tokencnt])
	print("> " + title)
	print(src)
	
	# 新页面
	plt.figure()
	title = title + "(统计总数: {})".format(len(tokens))
	plt.suptitle(title, fontsize = SupTitle_Size)

	# wordcloud
	text = " ".join(tokens) # src.keys()
	wordcloud = WordCloud(
		font_path = "C:/Windows/Fonts/simfang.ttf",
		background_color = "white",
		width = WC_Width, height = WC_Height
	).generate(text)

	ax = plt.subplot(gs[0, :])
	plt.title('词云图统计')
	plt.axis('off')
	plt.imshow(wordcloud, interpolation="bilinear")

	# bar
	x_axis = list(src.keys())
	y_axis = list(src.values())

	plt.subplot(gs[1, 0:2])
	plt.title('柱状图统计')
	plt.ylabel(u'次数')	

	xy = plt.gca() # get current axis
	xy.spines['right'].set_color('none')
	xy.spines['top'].set_color('none')

	plt.bar(x_axis, y_axis, color=BarPar_Color)
	plt.xticks(x_axis, x_axis, rotation=Bar_Rot)
	for x, y in zip(x_axis, y_axis):
		plt.text(x, y + .1, str(y), ha='center', fontsize=BarVal_FontSize)

	# pie
	labels = list(src.keys())[0: percnt]
	labels.append('Others')

	pers_all = list(src.values())
	pers_others = pers_all[percnt:]
	pers = pers_all[0: percnt]
	pers.append(sum(pers_others))

	plt.subplot(gs[1, 2])
	plt.title('圆饼图统计')
	plt.pie(pers, labels=labels, colors=BarPar_Color, autopct='%2.0f%%', shadow=False, startangle=90, pctdistance=0.6)
	# analyse(tokens, tokencnt, percnt) end

def getDataAndToken(opt):
	'''
	获取爬虫出的已经处理好的 token list
	'''
	cnt, title, desc = data.getData(opt)
	d_tokens = []
	for d in desc:
		d_nopunc = token.HandlePunctuation(d)
		d_tokens += token.getToken(d_nopunc)
	return d_tokens

if __name__ == "__main__":
	print('> Get data start')
	try:
		gitee_list = getDataAndToken(data.WebSite.Gitee)
		github_list = getDataAndToken(data.WebSite.Github)
		csdn_list = getDataAndToken(data.WebSite.Csdn)
	except data.GetDataNetWorkException as ex:
		ex.printErrorMsg()
		exit(1)

	tokencnt = 35 # 使用的 Token 总数
	percnt = 15 # 圆饼图显示的块数

	print()
	try:
		analyse(gitee_list, tokencnt, percnt, 'Gitee 热门词汇统计')
		analyse(github_list, tokencnt, percnt, 'Github 热门词汇统计')
		analyse(csdn_list, tokencnt, percnt, 'Csdn 搜索词汇统计')
	except:
		print("> Analyse data error")
	
	plt.show()
