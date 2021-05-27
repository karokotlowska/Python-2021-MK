import modul


####zad1
print("\n\nzad1 rysuj")
modul.rysuj(1)
modul.rysuj(3)
modul.rysuj(5)
####zad2
print("zad2 arabski na rzymski")
print(modul.f2(1900))
print(modul.f2(19))
print(modul.f2(2020))

####zad3
print("zad3 rzymski na arabski")
print(modul.f3(modul.f2(1900)))
print(modul.f3(modul.f2(19)))
print(modul.f3(modul.f2(2020)))


help(modul)






