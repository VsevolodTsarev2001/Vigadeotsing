from math import*  #слова в неправельном порядке
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu ümbermõõt", round(P,1))  #либо оденарные или двойные ковычки
di=a*sqrt(2)  #math не надо
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #лишняя скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => "))# float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))# float
S=b*c
print("Ristküliku pindala", round(S,1))
P=2*(b+c) # *
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b**2+c**2) #**
print("Ristküliku diagonaal", round(di,1)) # не закрыта скобка
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => '))#float + ковычки
d=2*r       #*
print("Ringi läbimõõt "+ str(round(d,1)))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2)) # не закрыта скобка
