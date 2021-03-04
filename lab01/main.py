#import keyword
#print(keyword.kwlist)

#import math
#dir (math)
#help(math.modf)

#dir('')
#help(''.strip)

#print(type(''))
#print(type(" "))


a=7
print(type(a))
a=1,5
print(type(a))
print(a)

a,b=1,'2'
print(a,b)

#swap
a,b=b,a
print(a,b)

a,*b=1,'2',3.,4,5
print(a,b)
print(type(a),type(b))

print (1/2,1//2) #jeden ukośnik: dokladna wartość
print(1./2,1.//2) #dwa ukośniki: zaokrąglenie do częsci całkowitej

print(2**3,pow(2,3),math.pow(2,3),"\n")
print(pow(2,3,4),"\n")#trzeci parametr liczy modulo liczby utworzonej przez dwie pierwsze

print(math.ceil(1/3),math.floor(1/3),round(1/3),"\n")

print(math.modf(1/3),"\n")
print(min(2,11,3,4,2),"\n")

a=-1.7
print(abs(a),math.fabs(a))
