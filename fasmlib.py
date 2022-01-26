# FAsm Release V1.0

# Uses tinystack, a tiny stack
# library I wrote for this

# Source:    The code
# Indevice:  Function to use for input
# Outdevice: Function to use for output

# See miko1112.github.io/fasm/docs for documentation
import tinystack as t
import sys

def runfasm(source,indevice=input,outdevice=print,plugin=None):
  while len(t.stack)>0:
    t.pop()
  ifSwitch=False
  notSwitch=False
  aSwitch=False
  tempdata=0
  do=True
  accumulator=0
  spare=None
  index=0
  rstack=[]
  def add():
    t.push(t.pop()+t.pop())
  def sub():
    d=(t.pop(),t.pop())
    t.push(d[1]-d[0])
  def mul():
    t.push(t.pop()*t.pop())
  def div():
    d=(t.pop(),t.pop())
    t.push(d[1]/d[0])
  def nPrint():
    nonlocal aSwitch
    if aSwitch: d,aSwitch=accumulator,False
    else:
      d=t.pop()
      t.push(d)
    outdevice(str(d))
  def aPrint():
    nonlocal aSwitch
    if aSwitch: d,aSwitch=accumulator,False
    else:
      d=t.pop()
      t.push(d)
    outdevice(chr(d))
  def popEq():
    d=(t.pop(),t.pop())
    t.push(d[1])
    t.push(d[0])
    if d[0]==d[1]: t.push(1)
    else: t.push(0)
  def popMr():
    d=(t.pop(),t.pop())
    t.push(d[0])
    t.push(d[1])
    if d[0]>d[1]: t.push(1)
    else: t.push(0)
  def popLs():
    d=(t.pop(),t.pop())
    t.push(d[0])
    t.push(d[1])
    if d[0]<d[1]: t.push(1)
    else: t.push(0)
  def ifDo():
    nonlocal ifSwitch
    ifSwitch=True
  def notDo():
    nonlocal notSwitch
    notSwitch=True
  def aPull():
    nonlocal accumulator
    accumulator=t.pop()
  def aPush():
    t.push(accumulator)
  def useAccumulator():
    nonlocal aSwitch
    aSwitch=True
  def aInput():
    selfdata=indevice()
    if len(selfdata)>0: d=ord(selfdata[0])
    else: d=0
    t.push(d)
  def sToggle():
    nonlocal spare
    if spare==None: spare=t.pop()
    else: t.push(spare); spare=None
  def sReturn():
    nonlocal index,rstack
    index=rstack.pop()
  bindings={
    "+":add,
    "*":mul,
    "-":sub,
    "/":div,
    ".":nPrint,
    ",":aPrint,
    ";":aInput,
    "=":popEq,
    ">":popMr,
    "<":popLs,
    "?":ifDo,
    "!":notDo,
    "a":aPush,
    "p":aPull,
    "s":sToggle,
    "l":useAccumulator,
    "x":t.pop,
    "r":sReturn
  }
  c=source.replace("\n"," ").replace("\r"," ").replace('	',' ').split(' ')
  while index!=len(c):
    do=True
    tempdata=0
    work=c[index]
    index+=1
    if ifSwitch:
      if aSwitch:
        aSwitch=False
        if accumulator==0: do=False
        else: do=True
      else:
        tempdata=t.pop()
        t.push(tempdata)
        if tempdata==0: do=False
        else: do=True
      ifSwitch=False
    if notSwitch:
      if aSwitch:
        aSwitch=False
        if accumulator==0: do=False
        else: do=True
      else:
        tempdata=t.pop()
        t.push(tempdata)
        if tempdata==0: do=False
        else: do=True
      notSwitch=False
    if do:
      if work=='': continue
      if work.startswith('_'): continue
      if (work.startswith('-') and work.count('-')==1 and work[1:].isnumeric()) or (work.isnumeric()):
        t.push(int(work))
        continue
      if work.startswith(':'):
        try:
          index=c.index('_'+work[1:])
          continue
        except: pass
      if work.startswith('f'):
        tempdata=index
        rstack.append(index)
        index=c.index('_'+work[1:])
        continue
      if work in bindings.keys():
          try:
            bindings[work]()
            continue
          except: pass
      if work.startswith('o:'):
        try:
          eval('plugin.'+work[2:]+'('+str(t.pop())+')')
          continue
        except: pass
      if work.startswith('i:'):
        try:
          eval('t.push(plugin.'+work[2:]+'())')
          continue
        except: pass
      outdevice('Something went wrong at index '+str(index+1)+": '"+work+"'")
      return
