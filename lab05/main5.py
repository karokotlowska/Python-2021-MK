import random

def obliczstring(s):
  l=[]
  for i in range(10):
    x=random.random()
    l.append((x,eval(s)))
  return l;

def powtarz_elem(*el):
  l=[]
  for i in el[0]:
    for j in el:
      if i not in j:
        break
    else:
      l.append(i)
  return(l)

def splitl(l1,l2,b=True):
  if b==True:
    d=min(len(l1),len(l2))
    w=[(l1[i],l2[i]) for i in range(d)]
  else:
    d=max(len(l1),len(l2))
    w=[(l1[i] if len(l1)>i else None,l2[i] if len(l2)>i else None) for i in range(d)]
  return w

def rozm(kw,nom=(10,5,2)):
  x=0
  while(kw>0):
    n=0
    for i in range(len(nom)):
      if(nom[i]<=kw and nom[i]>n):
        n=nom[i]
      kw-=n
      x+=1
  return x

def szuk(szu,a,b,mode='r',k=0):
  k+=1
  if mode=='r':
    l=random.randint(a,b)
    if l==szu:
      return k;
    elif l<szu:
      return szuk(szu,l,b,'r',k)
    else:
      return szuk(szu,a,l,'r',k)
  else:
    l=int((a+b)/2)
    if l==szu:
      return k;
    elif l<szu:
      return szuk(szu,l,b,'',k)
    else:
      return szuk(szu,a,l,'',k)



#####################################################
#1.

s='a*x+b'
tr=str.maketrans('ab',f'{random.randrange(10)}{random.randrange(10)}')
s=s.translate(tr)
print(s)
print(obliczstring(s))

###################################################
#2.
print(powtarz_elem([1,2,3],(1,2),[1,2]))

###################################################
#3.
print(splitl([1,2,3],[2,4]))
print(splitl([1,2,3],[2,4],False))
##################################################
#4.
print(rozm(25))

#############################################
#5.
print(szuk(15,0,100))
print(szuk(15,0,100,''))