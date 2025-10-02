import sys
if len(sys.argv) !=3:
    sys.exit("Program exit. please enter 2 file names")

f = open(sys.argv[1],'r')
contents=f.read()
f.close()
f.open(sys.argv[2],'w')
f.write(contents)
