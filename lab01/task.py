#napisz funkcję obliczającą miejsca zerowe funkcji kwadratowej

from math import sqrt
from cmath import sqrt as csqrt

print("\n------------------------------------\nZADANIE: \n")

a=float(input('podaj a= '))
b=float(input('podaj b= '))
c=float(input('podaj c= '))
delta=b**2-4*a*c
if delta>0:
  x1=(-b-sqrt(delta))/(2*a)
  x2=(-b+sqrt(delta))/(2*a)
  print("x1= ",x1," x2= ",x2)
elif delta==0:
  x=-b/(2*a)
  print(x)
else:
  print("brak rozwiązań")
  
  
  
 #kod z wykladu 1:
a=float(input('a=? '))
b=float(input('b=? '))
c=float(input('c=? '))
delta=b*b-4*a*c
if delta>0:
  x1=-b-sqrt(delta)/(2*a)
  x2=-b+sqrt(delta)/(2*a)
  print(f'{x1=:.3f}, {x2=:.3f}' )
elif delta==0:
  x=-b/(2*a)
  print(f'{x=:.3f}')
else:
 print('Nie ma miejsca zerowego')



#kod z wykładu 2
import sys
import math
import cmath
print("\n------------------------------------\nZADANIE: \n")

if len(sys.argv)!=5:
  sys.exit()
a=float(sys.argv[1])
b=float(sys.argv[1])
c=float(sys.argv[1])
eps=float(sys.argv[4])
if(d:=b**2-4*a*c)>eps:
  x1=(-b-sqrt(delta))/(2*a)
  x2=(-b+sqrt(delta))/(2*a)
  print(f '{x1=:.3f}, {x2=:.3f}')
elif math.fabs(d)<=eps:
  x=-b/(2*a)
  print(f 'x1=x2={-b/(2*a):.2f')
else:
  x1=(-b-cmath.sqrt(d))/(2*a)
  x2=(-b+cmath.sqrt(d))/(2*a)
  print(f '{x1=:.3f},{x2:.3f}')
