s=input()
if len(s)==0:
  print("empty")
else:
  first=s[0]
  if len(s)%2==0:
    idx = len(s)//2 -1
  else:
    idx = len(s)//2
  middle=s[idx]

  last=s[-1]
  res=first+middle+last
  print(res)