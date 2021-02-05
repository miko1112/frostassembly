# TinyStack Lib
# Allows for using a stack

stack=[]

def push(n):
   global stack
   stack.append(int(n))

def pop():
   global stack
   d=stack[-1]
   del stack[-1]
   return d
