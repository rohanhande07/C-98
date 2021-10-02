from os import read


f = open ("newfile.txt", "r")
t = f.read()
print (t)
f.close()
