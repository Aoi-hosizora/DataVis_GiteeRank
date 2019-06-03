import getData as data
import getToken as token

if __name__ == "__main__":
	title, content = data.getData()
	for t, c in zip(title, content):
		print("----------------")
		print(t, c)