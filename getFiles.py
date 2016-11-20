import glob
import os
import random
def getNumbers():
    for k in range(0, 195):
        hello = k
    return k
#k[53:k.__len__()]
files = glob.glob("C:/Users/XLuis/Desktop/LaGrange/images/*")

try:
    for k in range(0,195):
        newfileName = "C:/Users/XLuis/Desktop/LaGrange/images/"+str(k)+".jpg"
        os.rename(files[k],newfileName);
except Exception:
    print(Exception)
