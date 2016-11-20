import urllib.request
import random
f = open(file="main.css",mode="w")
response = urllib.request.urlretrieve("https://docs.python.org/3/_static/","flask")
print(str(response))
