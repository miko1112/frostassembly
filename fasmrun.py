import fasmlib as fasm
import sys

cleanprint =lambda s: print(s,end='')

if sys.argv[1].split(".")[-1]=="frost": c=open(sys.argv[1]).read()
else:
  print("FAsm does not support this file's format.")
  sys.exit()
fasm.runfasm(c,outdevice=cleanprint)
