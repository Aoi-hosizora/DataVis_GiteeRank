import jieba
import re, string

def HandlePunctuation(w):
	'''
	处理标点符号
	'''
	punc = r"[\u0060|\u0021-\u002c|\u002e-\u002f|\u003a-\u003f|\u2200-\u22ff|\uFB00-\uFFFD|\u2E80-\u33FF]"
	w = re.sub(pattern=punc, repl=' ', string=w)
	return w

def getToken(w):
	'''
	获取文字 token，保留中英文
	'''
	wl = jieba.lcut(w)
	# wl = jieba.cut(w, cut_all=True)
	while ' ' in wl:
		wl.remove(' ')
	return wl