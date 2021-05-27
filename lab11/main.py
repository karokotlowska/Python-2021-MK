'''5/10 - kryzys egzystencalny i nie chcialo mi sie'''

'''1. Celem programu jest implementacja automatu komórkowego 2D "Gra w życie". Tworzy się go na siatce kwadratowej N×N. Każda komórka może być w jednym z dwóch stanów 1 (żywa) lub 0 (martwa). Stosujemy periodyczne warunki brzegowe ("spinamy" krawędzie).

Reguły:

martwa komórka, która ma dokładnie 3 żywych sąsiadów, staje się żywa w kolejnej iteracji

żywa komórka z 2 albo 3 żywymi sąsiadami pozostaje nadal żywa; przy innej liczbie żywych sąsiadów umiera

Proszę utworzyć klasę, a w niej:
metodę inicjalizującą przyjmującą trzy parametry całkowite, pierwszy parametr określa rozmiary siatki, drugi wielkość początkowego kwadratu wypełnionego jedynkami, a trzeci liczbę iteracji,
metodę ewolucji automatu - w każdej iteracji ustalamy nowy stan każdej komórki, na podstawie stanu układu w kroku poprzednim,
metodę wypisującą na ekran stan układu - jeśli komórka jest żywa proszę wypisać * w przeciwnym wypadku spację.

Proszę uruchomić program dla siatki 30x30 i "żywego" obszaru początkowego 10x10 oraz 11x11 (5p)



2 Proszę utworzyć klasę Tablica, a w niej metody:
inicjalizującą przyjmującą jako parametr wymiar tablicy oraz jej elementy (jeżeli liczba elementów nie pozwala na inicjalizację tablicy proszę zgłosić wyjątek),
przeciążającą operator dodawania,
przeciążającą operator dodawania przyrostowego,
przeciążającą operator nawiasowy (pobranie i przypisanie wartości, proszę zapewnić brak możliwości przypisania niepoprawnej wartości np. jeśli tablica jest dwuwymiarowa nie można zastąpić wiersza pojedynczą wartością),
pozwalającą na sprawdzenie wymiaru tablicy,
wypisanie tablicy na ekran.'''

import copy
import numpy as np
##zad1
class Game:
  def __init__(self,N,n,iter):
    self.height=N
    self.tab=[[0]*N for _ in range (N)]
    for i in range(N//2-n//2,N//2+n//2+1):
      for j in range(N//2-n//2,N//2+n//2+1):
        self.tab[i][j]=1
    for row in self.tab:
      print(row)
    for i in range (iter):
      self.checkNeighbours(N)

  def checkNeighbours(self,N):
    deep=copy.deepcopy(self.tab)
    l=[[0]*N for _ in range (N)]
    for i in range(N):
      for j in range(N):
        if i==0 and j==0:
          pass
        elif i==0:
          pass
          # for x in range (i,i+1):
          #   for y in range (j,j+1):
          #     if self.tab[x][y]==1:
          #       count+=1
          # if self.tab[0][N-1]==1:
          #   count+=1
          # if self.tab[N-1][0]==1:
          #   count+=1
          # if self.tab[N-1][N-1]==1:
          #   count+=1
          # if count==3 and self.tab[x][y]==0:
          #   l[i][j]= 1
          # elif (count==2 or count==3) and l[x][y]==1:
          #   l[i][j]= 1
          # else: 
          #   l[i][j]= 0
        elif j==0:
          pass
        elif i==N and j==N:
          pass
        elif i==N:
          pass
        elif j==N:
          pass
        else:
          l[i][j]=self.check(i,j,deep)
    for row in l:
      print(row)
    print("\n--------\n")

  def check(self,x,y,l):
    count=0
    #l=copy.deepcopy(self.tab)
    for i in range (x-1,x+1):
      for j in range (y-1,y+1):
        if l[i][j]==1:
          count+=1
    if count==3 and l[x][y]==0:
      return 1
    elif (count==2 or count==3) and l[x][y]==1:
      return 1
    else: 
      return 0


a=Game(30,11,3)



###zad2
class tablica:
  def __init__(self,n,N,*tab):
    arr=np.array(tab)
    if len(tab)==n*N:
      self.tab=np.reshape(arr,(n,N))
      print(self.tab)
    else:
      raise ValueError()
  def __add__(self ,t):
    pass

tab1=tablica(3,2,3,4,5,6,7,8)
tab2=tablica(3,2,4,5,6,7,8,9)
