f = open("file.txt", "wt")
f.write("hello world")
f.close()

f = open("/tmp/file.txt", "rt")
print(f.read())
