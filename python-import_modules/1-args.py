import sys

argv_len = len(sys.argv) - 1

print("Number of argument{}: {}".format("s" if argv_len != 1 else "", argv_len), end="")
print(" {}.".format("s" if argv_len == 0 else ":") if argv_len != 1 else "\n")

for i, arg in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, arg))