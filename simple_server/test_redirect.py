import sys
import cStringIO


'''
name = raw_input("Please input your name: ")
print name
'''

'''
print "Please input your name: "
name = sys.stdin.readline()
print name
'''

'''
for fd in (sys.stdin, sys.stdout, sys.stderr):
    print fd

for fd in (sys.__stdin__, sys.__stdout__, sys.__stderr__):
    print fd
'''

memo = cStringIO.StringIO();
serr = sys.stderr;
file = open('out.txt', 'w+')

print >>memo, 'StringIO';
print >>serr, 'stderr';
print >>file, 'file'
print >>None, memo.getvalue()