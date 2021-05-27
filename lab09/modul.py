import random
import string
import sys
import functools
import math
import glob
import matplotlib.pyplot as plt

'''
zad1
funkcję dokonującą przekształcenia (L-system) wyrażenia wg schematu F → F+F−F−F+F. Stan początkowy 'F', '+' obrót w lewo p 90 stopni,  '−' obrót w prawo o 90 stopni. Wynik proszę narysować (np. dla 1, 3 i 5 przekształceń) (4p)

zad2
funkcję konwertującą liczbę zapisaną w systemie arabskim na rzymski (3p)

zad3
funkcję konwertującą liczbę zapisaną w systemie rzymskim na arabski (3p)
'''


#####1
def wzor(f):
  pattern=""
  pattern=f+"+"+f+"-"+f+"-"+f+"+"+f
  return pattern

def fun1(n,f="F"):
  patt=""
  for _ in range(n):
    patt=wzor(f)
    f=patt
  return f

def rysuj(n):
  instrukcje=fun1(n)
  xs=[0]
  ys=[0]
  x=0
  y=0
  dx=1 #direction - kirunek poczatkowy
  dy=0
  for k in instrukcje:
    if k=="F":
      x+=dx
      y+=dy
      xs.append(x)
      ys.append(y)
    if k=="+":
      if dx==1 and dy==0:
        dx=0
        dy=1
      elif dx==0 and dy==1:
        dx=-1
        dy=0
      elif dx==-1 and dy==0:
        dx=0
        dy=-1
      elif dx==0 and dy==-1:
        dx=1
        dy=0
    if k=="-":
      if dx==1 and dy==0:
        dx=0
        dy=-1
      elif dx==0 and dy==1:
        dx=1
        dy=0
      elif dx==-1 and dy==0:
        dx=0
        dy=1
      elif dx==0 and dy==-1:
        dx=-1
        dy=0
  plt.plot(xs,ys)
  rys="plot"+str(n)+".png"
  plt.savefig(rys)

#####2
'''arabski na rzymski'''
convertTab=[[1,"I"],[4,"IV"],[5,"V"],[9,"IX"],[10,"X"],[40,"XL"],[50,"L"],
[90,"XC"],[100,"C"],[400,"CD"],[500,"D"],[900,"CM"],[1000,"M"]]

def f2(n):
  size=len(convertTab)-1
  rzymski=""
  while n>0:
    while convertTab[size][0]>n:
      size-=1
    rzymski+=convertTab[size][1]
    n-=convertTab[size][0]
  return rzymski

#####3
'''rzymski na arabski'''
def f3(n):
  tab=[]
  for i in n:
    for j in convertTab:
      if i in j: tab.append(j[0])
  print (tab)
  arabski=0
  l=0
  if l<len(tab):
    for i in range(len(tab)-1):
      if tab[i]<tab[i+1]:
        arabski=arabski-tab[i]+tab[i+1]
        l+=2
      else:
        arabski+=tab[i]
        l+=1
  else:
    arabski+=tab[i]
    l+=1
  return arabski
