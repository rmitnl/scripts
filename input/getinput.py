import sys
# no args given
if len(sys.argv) == 1:
    print('No args provided!')
    sys.exit(1)

name=sys.argv[1]
print("Hello",name.split("=",1)[1])
