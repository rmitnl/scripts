import sys
if len(sys.argv) == 1:
    print('{"args":[]}')
    sys.exit(1)
out='{"args":['
for i in sys.argv[1:]:
    if i[0:5] != "--arg":
        out += '"' + i + "\","
out = out[:-1] + "]}"
print(out)
