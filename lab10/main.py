# nie do konca dobrze - w drugim zadaniu o cos innego jej chodzilo

import datetime
'''
zad1
Proszę utworzyć funkcję sprawdzającą poprawność numeru PESEL (3.5p)
Parametrami wejściowymi do funkcji są: Pesel, data urodzenia (datetime.date) oraz płeć.
Przykłady:
02070803628, 8 lipca 1902, kobieta
02270803624, 8 lipca 2002, kobieta
02270812350, 8 lipca 2002, mężczyzna

PESEL
cyfry 1-2 to ostatnie dwie cyfry roku urodzenia
cyfry 3-4 to dwie cyfry miesiąca urodzenia
cyfry 5-6 to dwie cyfry dnia urodzenia
cyfry 7-10 liczba porządkowa z oznaczeniem płci (liczba parzysta - kobieta, liczba nieparzysta - mężczyzna)
cyfra 11 suma kontrolna

Do numeru miesiąca dodawane są następujące wartości w zależności od roku:
dla lat 1800 - 1899 - 80
dla lat 1900 - 1999 - 0
dla lat 2000 - 2099 - 20
dla lat 2100 - 2199 - 40
dla lat 2200 - 2299 - 60

Suma kontroln: każdą pozycję numeru ewidencyjnego mnoży się przez odpowiednią wagę, są to kolejno: 1 3 7 9 1 3 7 9 1 3 i sumuje.
Wynik dzieli się modulo 10 i otrzymaną wartość należy odjąć od 10 i znów podzielić przez modulo 10.
Otrzymana wartość powinna być zgodna z ostatnią cyfrą numeru PESEL.


zad2
Proszę napisać funkcję zwracającą średni wiek osób, który daty urodzenia zapisane są w plik daty.in. (3.5p)
Funkcja powinna móc działać w trybie 'restrykcyjnym' - po napotkaniu niepoprawnej daty/wpisu zgłoszenie wyjątku i zakończenie działania, w trybie 'liberalnym' - niepoprawne wpisy są ignorowane.
Linia w pliku jest poprawna, jeśli zawiera dzień, miesiąc i rok,  które tworzą poprawną datę - zgodność liczby dni w miesiącu, w tym odpowiednia długość lutego w zależności od tego czy rok jest przestępny czy nie.
Rok przestępny: podzielny przez 4 i niepodzielny przez 100 lub podzielny przez 400.


zad3
Proszę napisać funkcję sprawdzającą czy elementy listy tworzą trójkę (a2+b2=c2)/czwórkę(a2+b2+c2=d2) pitagorejską (funkcja ma działać dla dowolnej długości "podciągu"!). Proszę zgłosić wyjątek w przypadku niepoprawnej długości listy oraz w przypadku, gdy lista nie zawiera żadnych trójek/czwórek pitagorejskich. Dla każdej trójki/czwórki proszę sprawdzić ile jest w niej wartości parzystych i nieparzystych (3p).
Listy testowe:
l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l=(1,2,3,4,5,6,7,8,9)
'''

####zad1
def check(pesel):
  try:
    if len(pesel)!=11:
      raise ValueError
  except ValueError:
    print("nieprawidlowa dlugosc peselu")
  else:
    sum=0
    tab1=[1,3,7,9,1,3,7,9,1,3,1]
    for i in range(11):
      sum+=(int(pesel[i]))*tab1[i]
      return (str(sum)[-1]=='0')

def fun1(pesel,data,plec):
  p=int(pesel[9])%2 #plec
  rok=int(pesel[0:2])
  miesiac=int(pesel[2:4])
  dzien=int(pesel[4:6])
  if check(pesel):
    if p==1:
      plec1='kobieta'
    else:
      plec1='mezczyzna'
    #sprawdzam rok
    if miesiac>80:
      rok+=1800
      miesiec-=80
    elif miesiac>60:
      rok+=2200
      miesiec-=60
    elif miesiac>40:
      rok+=2100
      miesiac-=40
    elif miesiac>20:
      rok+=2000
      miesiac-=20
    else:
      rok+=1900
    if miesiac==1:
      mies="stycznia"
    elif miesiac==2:
      mies="lutego"
    elif miesiac==3:
      mies="marca"
    elif miesiac==4:
      mies="kwietnia"
    elif miesiac==5:
      mies="maja"
    elif miesiac==6:
      mies="czerwca"
    elif miesiac==7:
      mies="lipca"
    elif miesiac==8:
      mies="sierpnia"
    elif miesiac==9:
      mies="wrzesnia"
    elif miesiac==10:
      mies="pazdziernika"
    elif miesiac==11:
      mies="listopada"
    elif miesiac==12:
      mies="grudnia"
    try:
      if rok==data.year:
        raise ValueError
      if miesiac==data.month:
        raise ValueError
      if dzien==data.day:
        raise ValueError
      if plec==plec1:
        raise ValueError
    except ValueError:
      print("Poprawny pesel ", dzien, mies, rok, plec)
    else:
      print("lala")

    

d=datetime.date(1902,7,8)
fun1('02070803628',d,'kobieta')

d=datetime.date(2002,7,8)
fun1('02270803624',d,'kobieta')



####zad2
def check(dzien,miesiac,rok):
  month=[31,28,31,30,31,30,31,31,30,31,30,31]
  if rok%4==0 and rok%100!=0 and rok%400==0:
    month[1]+=1
  try:
    if miesiac<=12 and miesiac>0:
      if dzien<=month[miesiac-1] and dzien>0:
        pass
      else:
        raise ValueError
    else:
      raise ValueError
  except ValueError:
    return 0
  return 1


def fun2(plik):
  with open(plik) as pl:
    lista=[]
    for i in pl:
      if len(i.split())==3:
        dzien=int(i.split()[0])
        miesiac=int(i.split()[1])
        rok=int(i.split()[2])
        if check(dzien,miesiac,rok):
          lista.append(2021-int(i.split(" ")[2]))
    suma=0
    for i in lista:
      suma+=i
    print ("Srednia rowna ", suma/len(lista))

fun2('daty.in')


####zad3
l1=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2)
l2=(1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29)
l3=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
l4=(1,2,3,4,5,6,7,8,9)

def par(tab3,tab4):
  par3=[]
  par4=[]
  for i in tab3:
    par=0
    npar=0
    for k in range(3):
      if i[k]%2==0:
        par+=1
      else:
        npar+=1
    par3.append([par,npar])
  for i in tab4:
    par=0
    npar=0
    for k in range(4):
      if i[k]%2==0:
        par+=1
      else:
        npar+=1
    par4.append([par,npar])
  print(par3,par4)
  


def fun3(lista):
  try:
    if len(lista)<4:
      raise ValueError
  except ValueError:
      print("za krotka lista")
  else:
    tab3=[]
    for i in range(2,len(lista)):
      if(lista[i-2]**2+lista[i-1]**2==lista[i]**2):
        tab3.append([lista[i-2],lista[i-1],lista[i]])
    try:
      if len(tab3)==0:
        raise ValueError
    except ValueError:
      print("brak trojki")
    tab4=[]
    for i in range(3,len(lista)):
      if(lista[i-3]**2+lista[i-2]**2+lista[i-1]**2==lista[i]**2):
        tab4.append([lista[i-3],lista[i-2],lista[i-1],lista[i]])
    try:
      if len(tab4)==0:
        raise ValueError
    except ValueError:
      print ("brak czworki")
    print(tab3)
    print(tab4)
    par(tab3, tab4)
fun3(l1)
fun3(l2)
fun3(l3)
fun3(l4)



