f = open("file.txt", "wt")
f.write("hello world")
f.close()

f = open("./file.txt", "rt")
print(f.read())
