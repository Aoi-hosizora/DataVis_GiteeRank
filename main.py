import getData as data
import getToken as token
from wordcloud import WordCloud

import sys
import matplotlib.pyplot as plt

font = {
	'family' : 'SimHei',
	'weight' : 'regular',
	'size'   : '12'
}
plt.rc('font', **font)
plt.rc('axes', unicode_minus=False)
Axis_FontSize = 14
WC_Height = 500
WC_Width = 2000

def analyse(tokens, tokencnt, percnt):
	'''
	分析 tokens 列表生成
	柱状图, 圆饼图, 词云图
	'''
	src = {}
	for t in tokens:
		if src.get(t) == None:
			src[t] = 1
		else:
			src.update({t: src.get(t) + 1})
	
	src = dict(sorted(src.items(), key=lambda v: (v[1], v[0]), reverse=True)[0: tokencnt])
	print(src)

	# wordcloud
	text = " ".join(tokens) # src.keys()
	wordcloud = WordCloud(
		font_path = "C:/Windows/Fonts/simfang.ttf",
		background_color = "white",
		width = WC_Width, height = WC_Height
	).generate(text)

	plt.subplot(2, 1, 1)
	plt.title('词云图统计')
	plt.axis('off')
	plt.imshow(wordcloud, interpolation="bilinear")

	# bar
	x_axis = list(src.keys())
	y_axis = list(src.values())

	plt.subplot(2, 2, 3)
	plt.title('柱状图统计')
	plt.ylabel(u'次数', fontsize=Axis_FontSize)
	plt.bar(x_axis, y_axis, color='rgby')
	plt.xticks(x_axis, x_axis, rotation=60)

	# pie
	labels = list(src.keys())[0: percnt]
	labels.append('Others')

	pers_all = list(src.values())
	pers_others = pers_all[percnt:]
	pers = pers_all[0: percnt]
	pers.append(sum(pers_others))

	plt.subplot(2, 2, 4)
	plt.title('圆饼图统计')
	plt.pie(pers, labels=labels, colors='rgby', autopct='%2.0f%%', shadow=False, startangle=90, pctdistance=0.6)

	plt.show()

if __name__ == "__main__":
	cnt, title, desc = data.getData()
	d_tokens = []
	for t, d in zip(title, desc):
		d_nopunc = token.HandlePunctuation(d)
		d_tokens += token.getToken(d_nopunc)

	analyse(d_tokens, 20, 15)