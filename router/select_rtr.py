import sys
# no args given
if len(sys.argv) == 1:
    print('{"args":[]}')
    sys.exit(1)

# some args given
args = []
out='{"args":['
for i in sys.argv[1:]:
    if i[0:5] != "--arg":
        out += '"' + i + "\","
        args.append(i) 
out = out[:-1] + "]}"
print(out)
#print(args)
