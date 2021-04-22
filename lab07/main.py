import random
import string
import sys
import time
import functools
import math

'''
zad1
Proszę napisać generator zwracający kolejne wiersze trójkąta Pascala wraz z sumą ich wartości (2p)

zad2
Proszę wygenerować losowy ciąg zer i jedynek o długości N. Proszę napisać generator zwracający liczbę zer oddzielających kolejne jedynki w sekwencji przekazanej jako parametr. Korzystając z utworzonego generatora proszę obliczyć średnią odległość między kolejnymi jedynkami w wygenerowanym wcześniej ciągu (2p)

zad3
Proszę napisać trzy funkcje generatorowe:
zwracającą kolejne elementy ciągu Fibonacciego (nieskończony),
zwracającą te wartości z przekazanej jako parametr sekwencji, które są parzyste/nieparzyste
zwracającą wartości z przekazanej jako pierwszy parametr sekwencji i przerywającą działanie po napotkaniu wartości większej niż drugi parametr przekazany do funkcji
Korzystając ze zdefiniowanych funkcji proszę obliczyć sumę parzystych/nieparzystych elementów ciągu Fibonacciego mniejszych od 100 (2p)

zad4
Proszę napisać generator działający dokładnie tak samo jak wbudowany range (proszę się upewnić, że wiecie Państwo jak on działa!), ale pozwalający na generowanie liczb rzeczywistych (2p)
Do testów: range(7), range(-7), range(2,7), range(7,2), range(2,7,2), range(2,7,-2), range(7,2,2), range(7,2,-2)

zad5
Proszę napisać generator obliczający ui wg zależności:
ui=ui-1+a/xi-1, z wartością początkową u0=0 dla x0=1 oraz z xi=x0+ia
Obliczenia proszę wykonać dla a=0.05 i przerwać je dla x=1.5. Zależność pozwala na wyznaczenie przybliżonej wartości logarytmu naturalnego z danej liczby. Generator ma zwracać x oraz przybliżoną i dokładną wartość logarytmu naturalnego dla danego x (2p)


#notatki

#jezeli w funkcji yield - to funkcja staje się generatorem

def gen():
  x=1
  yield x
  x+=2
  yield x
  x+=2
  yield x

for i in gen():
  print(i,end=' ')

def gen(seq,f):
  for el in seq:
    yield f(el)

w=[random.randrange(50) for _ in range(10)]
for i in gen(w,lambda x: x**3):
  print(i,end=" ")'''



####zad1
print("zad1")
N=5
def pascal(n):
  list1=[1]
  yield list1,sum(list1)
  for i in range (n):
    list1.insert(len(list1),1)
    for i in range (len(list1)-2,0,-1):
      list1[i]+=list1[i-1]
    yield list1,sum(list1)

def printPasc(a):
  s=' '.join(str(i) for i in a[0])
  print(a[1],s.center(5*N))

for i in pascal(N):
  printPasc(i)




####zad2
print("\nzad2")
N=7
ciag=[random.randint(0,1) for i in range (N)]
print(ciag)

def liczbazer(ciag):
  count=0
  b=False
  for i in range (N):
    if ciag[i]==1:
      if b:
        yield count
        count=0
      else:
        b=True
        count=0
    else:
      if b:
        count+=1
print("Liczba zer: ",N-len(list(liczbazer(ciag)))-1)
print("Odległości między jedynkami: ", list(liczbazer(ciag)))
print("Srednia odległość miedzy jedynkami: ",sum(list(liczbazer(ciag)))/len(list(liczbazer(ciag))))


####zad3
print("\nzad3")
def fib():
  x=1
  y=1
  yield x
  yield y
  while True:
    x,y=y+x,x
    yield x

def odeeven(seq,p):
  for i in seq:
    if p==True:
      if i%2==0:
        yield i
    else:
      if i%2!=0:
        yield i

def larg(seq,n):
  for i in seq:
    if i<n:
      yield i
    else:
      return

'''
gen=fib()
for i in range (10):
  print(next(gen))'''

suma=sum(odeeven(larg(fib(),100),True))
print("Suma parzystych",suma)

suma=sum(odeeven(larg(fib(),100),False))
print("Suma nieparzystych",suma)



####zad4
print("\nzad4")
def myrange(a=0,b=None,c=1):
  if b==None:
    if a<0:
      b=0
    else:
      b=a
      a=0
  elif a<b and c<=0:
    return
  elif a>b and c>=0:
    return
  if b>a:
    while a<b:
      yield a
      a+=c
  elif b<a:
    while a>b:
      yield a
      a+=c
  else:
    return


print(list(myrange(10)))
print(list(myrange(-7)))
print(list(myrange(2,7)))
print(list(myrange(7,2,-2)))
print(list(myrange(2,7,-2)))
print(list(myrange(7,2)))
print(list(myrange(7,2,2)))

'''
for i in range(2,7,-2):
  print (i)'''



####zad5
print("\nzad5")
from math import log
def logar():
  u=0
  x0=1
  a=0.05
  i=1
  x=1.
  while x<=1.5:
    yield x,u,log(x)
    u=u+a/x
    x=x0+i*a
    i+=1
for i in logar():
  print(i)
