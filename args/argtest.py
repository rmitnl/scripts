import sys
if len(sys.argv) == 1:
    print("no args")
    sys.exit(1)
for i in sys.argv[1:]:
    print(i)

