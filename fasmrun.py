import fasmlib as fasm
import sys

def cleanprint(s):
  print(s,end='')

if sys.argv[1].split(".")[-1]=="frost": c=open(sys.argv[1]).read().replace("\n"," ").replace("\r"," ").replace('	',' ').split(' ')
else:
  print("FAsm does not support this file's format.")
  sys.exit()
fasm.runfasm(c,outdevice=cleanprint)
