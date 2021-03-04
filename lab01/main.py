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


print('\n\n')
#krotki
k=()
print(type(k))

k=(2) #zrobi inta
print(type(k))

k=(2,)
print(type(k))

k=(1,2.3,'3',(4,7),[2,3,4])
print(len(k))

print(k[0],k[len(k)-1],k[-1])

#niemodyfikowalność krotek
#k[-1]=7 nie będzie działać
k[-1][1]=7 #zadziala bo 7 wskoczypod element z listy
print(k)




#listy
k=[]
print(type(k))

k=[2]
print(type(k))

k=[2,] #przecinek nizcego nie zmieni
print(type(k))
print(k[0],k[-1])

#kopie list
k=[1,2.3,'3',(4,7),[2,3,4]]
c=k
c[1]=[7,8,9] #modyfikacja c wplynie na oryginał
print(c,k)
print(id(c),id(k))

c=k[:] #kopiowanie płytkie
c[1]='4,5,6'
print(c,k)
print(id(c),id(k))

c[-1][1]='4,5,6' #tu oryginal widzi zmiany, bo odnosimy się do listy w liście (a tego kopii nie mamy)
print(c,k)

import copy
c=copy.deepcopy(k)
c[1]='4,5,6'
print(c,k)
print(id(c),id(k))

c[-1][1]='4,5,6' #w tym wypadku jest ok
print(c,k)
