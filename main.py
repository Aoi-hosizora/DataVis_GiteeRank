import getData as data
import getToken as token

import matplotlib.pyplot as plt

font = {'family' : 'SimHei',
        'weight' : 'regular',
        'size'   : '12'}
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
	x_axis = tuple(src.keys())
	y_axis = tuple(src.values())
	plt.bar(x_axis, y_axis, color='rgb')
	plt.show()
	print(src)

if __name__ == "__main__":
	cnt, title, desc = data.getData()
	d_tokens = []
	for t, d in zip(title, desc):
		d_nopunc = token.HandlePunctuation(d)
		d_tokens += token.getToken(d_nopunc)

	analyse(d_tokens, 30)