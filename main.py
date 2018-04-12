#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import string
import hashlib
 
if __name__=='__main__':
  
  x=1
  v=raw_input("please enter experiment data:")
  d=3
  h=v+str(x)
  hash=hashlib.sha1()
  hash.update(bytes(h))
  value=hash.hexdigest()
  print value
  dd=value[0:3]
  print dd
  
  while(dd!='000'):
   x=x+1
   h=v+str(x)
   hash.update(bytes(h))
   value=hash.hexdigest()
   print value
   dd=value[0:3]
   
print x 
