import sys
if len(sys.argv) == 1:
    print('{"args":[]}')
    sys.exit(1)
out='{"args":['
for i in sys.argv[1:]:
    if i != "--arg":
        out += '"' + i + "\","
out = out[:-1] + "]}"
print(out)
