import random
import string
import sys
import time
import functools
import math
'''
zad1
Proszę napisać program testujący alternatywne sposoby budowania zestawu wartości: pętla for, lista składana, funkcja map i wyrażenie generatorowe (składnia taka jak listy składanej tylko w miejsce nawiasów kwadratowych należy wstawić okrągłe; o generatorach będziemy mówić na kolejnych zajęciach). Dla każdego ze sposobów proszę utworzyć osobną funkcję tak, aby uzupełnić poniższy kod:

import time
import sys

powt=1000
N=10000
(...)
print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

gdzie: tester - funkcja wywołująca powt razy daną funkcję, w której tworzonych jest N wartości.

Proszę wykonać testy (wszystko w ramach tych samych funkcji):
        dodawanie elementu
        dodawanie elementu podniesionego do kwadratu
        sumowanie elementów z wykorzystaniem pętli for
        sumowanie z wykorzystaniem funkcji sum
        konwersja obiektu map i generatora do listy

Do pomiaru czasu proszę użyć funkcji time_ns z modułu time. Otrzymane wyniki proszę dołączyć do wysyłanego programu (2p)

--------------------------------------


zad2
Proszę utworzyć dwie listy po sto wartości losowych z przedziału [0,20) każda. Następnie na ich podstawie proszę utworzyć listę dwuelementowych krotek, elementów o jednakowych indeksach w listach wyjściowych spełniających warunek, że suma ich wartości jest większa od 3 i mniejsza od 15. Należy wykorzystać listę składaną oraz funkcje filter i zip (2p)


--------------------------------------


zad3
Proszę napisać funkcję przyjmującą dwa parametry - lista x-ów i y-ów. Korzystając z funkcji wbudowanych sum i map proszę obliczyć (i zwrócić z funkcji) wartości dofitowanych współczynników prostej oraz ich niepewności (wzory w pliku) (2p).


--------------------------------------


zad4 
Proszę napisać funkcję myreduce przyjmującą dwa parametry (funkcję i sekwencję) oraz zwracającą liczbę. Funkcja przekazywana jako parametr będzie funkcją przyjmującą dwa parametry. Działanie funkcji proszę przetestować korzystając z wyrażenia lambda dla dodawania i mnożenia (2p)


--------------------------------------


#zad5
Mamy listę, której elementami są listy dwuelementowe (możemy je potraktować jako współrzędne punktów na płaszczyźnie). Chcemy utworzyć nową listę, w której pierwszym elementem jest lista x-ów, a drugim lista y-ów. Proszę to zrobić w jednej linijce korzystając z funkcji myreduce, wyrażenia lambda oraz wbudowanej funkcji map (obie listy tworzymy jednocześnie!) (2p)


--------------------------------------


#notatki

f=lambda x: x+3
print (f(5))

print(bin(13)) #konwertowanie watrosci do sytemu dwójkowego, po konwersji dostajemy string
print(int('0b1101',2)) #konwertowanie zapisu binarnego do postaci binarnej

x=2
def fun(a,b):
  c=a+b
  print(locals())
  #print(globals())
fun(4,5)

ob=random.sample(string.ascii_uppercase,10)
rob=[el for el in reversed(ob)]
print(ob,rob)

#zwracaja wartosc logczina na podstawie elementow sekwencji
print(all(range(10))) # zwroci 0 bo range zaczyna się od 0 co ma wartosc falszu
all(range(2,10))
any(range(10)) #jezeli ktorykowliek

mapped=map(lambda x,y: x+y,range(5),range(5,10))
for el in mapped:
  print(el)
#przyjmuje parametry iterowalne - łączy w krotki elementy o tych samych indeksach
zipped=zip(range(5),range(5,7),range(0,10,2))
for el in zipped:
  print(el)
#otrzymamy dwie krotki bo ta srokowa wartosc jest najktorza

#jesli funkcja zwraca wartosc logiczną prawdy, to funkcja "odfiltrowuje" wartosc
filtered=filter(lambda x: x%2, range(10))
for el in filtered:
  print(el)

filter(None,range(5)) #1,2,3,4 - wylatuje 0 bo zero ma wartosc logiczną fałszu

#wymuszamy stworzenie listy
print(list(map(lambda x,y: x+y,range(5),range(5,10))))

import functools
print(functools.reduce(lambda x,y: x+y,[1,2,3,4,5])) #((((1+2)+3)+4)+5)
# najpierw pobiera pierwsze da elementy i potem przy kolejnym wywolaniu postawia wynik pierwszego wykonania pod

print(functools.reduce(lambda x,y: x*y,[1,2,3,4,5])) #liczenie silni'''

#zad1
'''' zakomentowane ponieważ zjadalo zbyt dużo czsu - wyniki w pliku result.txt
powt=1000
N=10000
def tester(function):
  for _ in range(powt):
    function(N)

def forStatement(num):
  list1=[]
  sum=0;
  for _ in range(num):
    #list1.append(_)
    #sum+=_
    sum+=_**2

def listComprehension(num):
  res=[_ for _ in range(num)]

def mapFunction(num):
  res=map(lambda x: x, range(num))

def generatorExpression(num):
  res=(_ for _ in range(num))



f=open("result3.txt","w")
print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
  t1=time.time()
  print(testFunction.__name__.ljust(20), '=>', tester(testFunction), time.time()-t1)
  t=time.time()-t1
  f.write(str(t))
  f.write("\n")
f.close()
'''


#zad2
first=[random.randrange(20) for i in range(100)]
second=[random.randrange(20) for i in range(100)]
print("\n\n",list(filter(lambda x: x if 15>sum(x)>3 else None,zip(first,second)))) #filter 'odfiltrowuje wartosci None


#zad3
def fit(l1,l2):
  xs=functools.reduce(lambda x,y: x+y,l1)/len(l1)
  ys=functools.reduce(lambda x,y: x+y,l2)/len(l2)
  D=functools.reduce(lambda x,y:(x-xs)**2,l1)
  ySum=functools.reduce(lambda x,y:x+y,l2)
  a=ySum*functools.reduce(lambda x,y: x-xs,l1)/D
  b=ys-a*xs
  deltaY=math.sqrt((functools.reduce(lambda x,y: x+y,map(lambda x,y:(y-(a*x+b))**2,l1,l2))/(len(l1)-2)))
  deltaA=deltaY/(math.sqrt(D))
  deltaB=deltaY*math.sqrt(1/len(l1)+xs**2/D)
  return a,b,deltaA, deltaB
print(fit([1,2,3,4],[2,3,4,5]))


#zad4
def myreduce(fun,seq):
  res=fun(seq[0],seq[1])
  for el in seq[2:]:
   res=fun(res,el)
  return res

print(myreduce(lambda x,y: x+y,[1,2,3,4,5,6]))
print(myreduce(lambda x,y: x*y,[1,2,3,4,5,6]))


#zad5
def fun5(l3):
  return myreduce(lambda x,y: map(lambda x,y:[x,y] if not isinstance(x,list) else x+[y],x,y),l3)
print(list(fun5([[2,3],[4,5],[4,5],[1,2]])))
