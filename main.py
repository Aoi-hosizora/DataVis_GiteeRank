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

def analyse(tokens, num):
	'''
	分析 tokens 列表生成柱状图
	'''
	src = {}
	for t in tokens:
		if src.get(t) == None:
			src[t] = 1
		else:
			src.update({t: src.get(t) + 1})
	
	src = dict(sorted(src.items(), key=lambda v: (v[1], v[0]), reverse=True)[0: num])
	print(src)

	# PLT
	wordcloud = WordCloud(
		font_path="C:/Windows/Fonts/simfang.ttf",
		background_color="white", width=1000, height=880
	)	.generate(" ".join(tokens))
	plt.subplot(2, 1, 1)
	plt.imshow(wordcloud, interpolation="bilinear")

	x_axis = tuple(src.keys())
	y_axis = tuple(src.values())
	plt.subplot(2, 2, 3)
	plt.bar(x_axis, y_axis, color='rgby')

	labels = src.keys()
	pers = src.values()
	plt.subplot(2, 2, 4)
	plt.pie(pers, labels=labels, colors='rgby', autopct='%2.0f%%', shadow=False, startangle=90, pctdistance=0.6)

	plt.show()

if __name__ == "__main__":
	cnt, title, desc = data.getData()
	d_tokens = []
	for t, d in zip(title, desc):
		d_nopunc = token.HandlePunctuation(d)
		d_tokens += token.getToken(d_nopunc)

	analyse(d_tokens, 15)