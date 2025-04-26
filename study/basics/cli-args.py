import sys

print('Number of args', len(sys.argv), 'arguments: ')
for i, arg in enumerate(sys.argv):
    print(str(i) + ': ' + arg)
