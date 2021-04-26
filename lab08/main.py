import random
import string
import sys
import time
import functools
import math
import glob
import matplotlib.pyplot as plt

#7,5/10


'''
zad1
Proszę napisać funkcję, która pozwoli na wypisanie: n początkowych wierszy pliku, n końcowych wierszy pliku, co n-tego wiersza pliku, n-tego słowa ze wszystkich wierszy i n-tego znaku ze wszystkich wierszy. Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p)


zad2
Odczytujemy wartości ze wszystkich plików, których nazwy rozpoczynają się od data i kończą na in w katalogu bieżącym. Na wyjściu proszę utworzyć jeden plik z trzema kolumnami:
pierwsza kolumna - numer wiersza,
druga kolumna - uśredniona wartość z danego wiersza ze wszystkich plików (numpy.average),
trzecia kolumna - odchylenie standardowe wartości z danego wiersza ze wszystkich plików (numpy.std)

zad3
Proszę napisać funkcję, tworzącą plik z instrukcjami pozwalającymi na wygenerowanie wykresu plików j.w. + wynikowego (łącznie z odchyleniem standardowym)*patrz niżej, proszę skorzystać z potrójnego cudzysłowa (1p)

zad4
Pliki o nazwach rok.in (rank.zip) zawierają informację o pozycji na liście rankingowej pewnych osób, w kolejnych latach. Proszę utworzyć zbiorczy plik, w którym w pierwszej kolumnie znajdzie się "nazwisko", kolejne kolumny będą odpowiadały pozycja danej osoby na liście rankingowej w kolejnych latach, od 2000 do 2020 (2.5p)

zad5
Proszę sporządzić histogram słów rozpoczynających się na daną literę alfabetu ze wszystkich plików pasujących do określonego wzorca w katalogu bieżącym, opcje wyświetlenia: sortowanie alfabetyczne bądź po liczbie słów (2.5p)


#notatki
pl=open(śceiżka do pliku, tryb)
pl.close()
with open(sceizka do pliku) as pl:
  #pass

#odczytywanie
with open('nazwa') as pl:
  line=pl.readline()
  print(line)
  while line:
    line=pl.readline()
    print(line)

with open('nazwa') as pl:
  for linein pl:
    print(line)

#wpisywanie do pliku
with open('nazwa') as pl:
  x,y=1,2
  pl.write(f'x={x},y={y}\n')


'''

####zad1
print('\nzad1')
def fun1(n):
  with open('zad1test.txt') as pl:
    p=pl.readlines()
    print(p[:n])
    print(p[-n:])
    print(p[::n])
    print([line.split()[n-1] for line in p])
    print([line[n-1] for line in p])
  
fun1(1)


####zad2
import numpy
print('\nzad2')
pliki=glob.glob('./data/**.in')

tab=[]
for plik in pliki:
  with open(plik) as pl:
    tab.append(pl.readlines())
with open('zad2wyniki.txt','w') as pl:
  for line in range(len(tab[0])):
    d=[]
    for i in range(len(tab)):
      d.append(float(tab[i][line]))
    pl.write(f'{line} {numpy.average(d)} {numpy.std(d)}\n')

  '''for line in range(len(tab[0])):
    for i in range(len(tab)):
      pass'''


####zad3
#pobrac pliki

with open('plt.py','w') as file:
  file.write(f"""import matplotlib.pyplot as plt\nimport numpy\nx,y,dy=numpy.loadtxt(glob.glob('./data/data1.in', unpack=True)\nplt.plot(x, y, 'o')\nplt.errorbar(x, y, marker='*', yerr=dy)\nplt.xlabel('x')\nplt.savefig('res.pdf')""")



####zad4
import os
dict1={}
folderpath=r"rank"
filepaths=[os.path.join(folderpath,name) for name in os.listdir(folderpath)]
rok=[]
for i in filepaths:
  rok.append(filepaths[6:-3])
for file in filepaths:
  with open(file) as pl:
    for line in pl:
      tab=line.split(' ')
      dict1.setdefault(tab[0],['='])
      dict1[tab[0]].append((file[5:-3],tab[1][:-1]))
with open('zad4wynik.txt','w') as pl:
  for i in dict1:
    pl.write(f'{i}')
    for j in dict1[i]:
      pl.write(f'{j}')
    pl.write(f'\n')




####zad5
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

huge_list=[]
with open('zad5A.in') as pl:
  huge_list=pl.read().split()
print(huge_list)

''''
#kolejnosc wystąpień - chyba dziala
counter=Counter(huge_list)
print(counter)
labels,counts=np.unique(huge_list,return_counts=True)
t=range(len(counter))
plt.bar(t,counts,align='center')
plt.xticks(t,labels)
plt.show()'''


''''
#kolejnosc alfabetyczna nie dziala
huge_list.sort()
counter=Counter(huge_list)
print(counter)
labels,counts=np.unique(huge_list,return_counts=True)
t=range(len(counter))
plt.bar(t,counts,align='center')
plt.xticks(t,labels)
plt.show()
'''
