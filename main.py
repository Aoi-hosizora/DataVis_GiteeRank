import jieba
import nltk
import re, string
import sys
import matplotlib.pyplot

def HandlePunctuation(w):
	'''
	处理标点符号
	'''
	w = re.sub(pattern="[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+",
		       repl=" ", string=w)
	return w

def getToken(w):
	'''
	获取文字 token
	'''
	wl = jieba.lcut(w)
	return wl

if __name__ == "__main__":
	w = sys.argv[1]
	w = HandlePunctuation(w)
	wl = getToken(w)
	print(wl)