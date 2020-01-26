import sys

args = sys.argv

print("Say,     {}!".format(len(args)))
for arg in args:
    print("Hello,   {}!".format(arg))
