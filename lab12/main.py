###zad1
'''Proszę napisać iterator zwracający kolejny wyraz ciągu arytmetycznego dwoma sposobami i porównać ich wykorzystanie (2p)'''

class sequence():
  def __init__(self,a,r):
    self.a=a
    self.r=r
  def __iter__(self):
    return self
  def __next__(self):
    if self.a>30:
      raise StopIteration
    self.a+=self.r
    return self.a
  def __str__(self):
    return f'{self.a}'

print("\nzad1:\n")
seq1=sequence(2,6)
for i in seq1:
  for j in seq1:
    print(i,j)
  
  
class sequence2():
  def __init__(self,a,r):
    self.a=a
    self.r=r
  def __next__(self):
    if self.a>30:
      raise StopIteration
    self.a+=self.r
    return self.a
  def __iter__(self):
    return sequence2(self.a,self.r)

print("\nzad1 cz 2:\n")
seq2=sequence2(2,6)
for i in seq2:
  for j in seq2:
    print(i,j)



###zad2
'''Proszę utworzyć iterator zwracający liczbę pseudolosową generowaną wg wzoru Xn+1 = (aXn + c)%m, dla m = 248, a = 44485709377909, c = 0, x0 = 1. Korzystając z zaimplementowanego iteratora proszę sprawdzić ile punktów trzeba wylosować, aby obliczyć wartość całki z zadaną dokładnością, np. 10−7 (stosujemy metodę Monte Carlo) (5p).

Losujemy n punktów znajdujących się w obrębie prostokąta ograniczającego funkcję w granicach całkowania. Wprowadzamy zmienną pomocniczą t, którą modyfikować będziemy następująco:
jeżeli wylosowany punkt (xi, yi) leży nad osią OY i jednocześnie pod wykresem funkcji całkowanej, czyli spełnia nierówność: 0 < yi ≤ f(xi), wówczas zwiększamy zmienną t o jeden,
jeżeli wylosowany punkt (xi, yi) leży pod osią OY i jednocześnie nad wykresem funkcji całkowanej, czyli spełnia nierówność: 0 > yi ≥ f(xi), wówczas zmniejszamy zmienną t o jeden,
jeżeli wylosowany punkt (xi, yi) nie spełnia żadnego z powyższych warunków, wówczas pozostawiamy zmienną t bez zmian.
Całkę obliczamy jako Pprostokąta t/n'''


import math

class r():
  def __init__(self):
    self.a = 44485709377909
    self.m=2**48
    self.c=0
    self.x=1
  def __iter__(self):
    return self
  def __next__(self):
    self.x=(self.a*self.x+self.c)%self.m
    return self.x/self.m

print("\nzad2:\n")
integral=r()
n=0
t=0
for x in integral:
  n+=1
  y=next(integral)
  if y>0 and 0<y<=math.cos(x):
    t+=1
  elif y<0 and 0>y>=math.cos(x):
    t-=1
  if(abs(math.cos(x)*x*t/n-x*y*t/n)<1e-7):
    break
print(n)
  #elif
   # pass





###zad3
'''Proszę napisać iterator zwracający kolejne przybliżenie miejsca zerowego metodą Newtona-Raphsona: xn+1=xn-f(xn)/f'(xn) z zadaną dokładnością startując od określonej wartości początkowej, np. f(x)=sin(x)-(0.5x)2, x=1.5 i eps=10-5 (pochodna - scipy.misc) (3p).'''

import scipy.misc
import math

class NR:
  def __init__(self,function,eps,x):
    self.function=function
    self.eps=eps
    self.x=x
  def __iter__(self):
    return self
  def __next__(self):
    xo=self.x
    self.x=self.x-self.function(self.x)/scipy.misc.derivative(self.function,self.x)
    if abs(self.x-xo)<self.eps:
      raise StopIteration
    return self.x


print("\nzad3:\n")
for i in NR(lambda x:math.sin(x)-(0.5*x)**2,1e-5,1.5):
  print(i)
