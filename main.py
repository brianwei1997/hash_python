if __name__=='__main__':

  x=1
  v=raw_input("please enter experiment data:")
  d=raw_input("please input d value:")
  d=int(d)
  h=v+str(x)
  hash=hashlib.sha1()
  hash.update(bytes(h))
  value=hash.hexdigest()
  print value
  dd=value[0:d]
  print dd

  while(dd!=d*'0'):
   x=x+1
   h=v+str(x)
   hash.update(bytes(h))
   value=hash.hexdigest()
   print value
   dd=value[0:d]

print x
