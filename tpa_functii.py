import math

a=int(input("Dati primul numar:"))
b=int(input("Dati al doilea numar:"))

def suma(x,y):
    s=0
    s=x+y
    return s

print("Suma numerelor este:", suma(a,b))

def produs(x,y):
    p=1
    p=x*y
    return p

print("Produsul numerelor este:", produs(a,b))

def m_a(x,y):
    m_a=0
    m_a=(x+y)/2
    return m_a

print("Media aritmetica a numerelor este:", m_a(a,b))

def cmmdc(x,y):
    div=math.gcd(x,y)
    return div

print("Cel mai mare divizor comun al numerelor este:", cmmdc(a,b))

def cmmmc(x,y):
    mul=abs(x*y)//cmmdc(x,y)
    return mul

print("Cel mai mic multiplu comun al numerelor este:", cmmmc(a,b))

def nr_min(x,y):
    min=0
    if x<y:
        min=x
    if x>y:
        min=y
    if x==y:
        min="Numerele sunt egale"
    return min

print("Numarul minim este:", nr_min(a,b))

def nr_max(x,y):
    max=0
    if x>y:
        max=x
    if x<y:
        max=y
    if x==y:
        max="Numerele sunt egale"
    return max

print("Numarul maxim este:", nr_max(a,b))

def suma2():
    s2=str(a)+'+'+str(b)+'='+str(suma(a,b))
    return s2

print("Suma numerelor in formatul a+b=c este:", suma2())

def produs2():
    p2=str(a)+'*'+str(b)+'='+str(produs(a,b))
    return p2

print("Produsul numerelor in formatul a*b=c este:", produs2())

def all_dc(x,y):
    dc=[]
    for i in range(1,(nr_max(a,b)+1)):
        if (x%i==0) and (y%i==0):
            dc.append(i)
    return dc

print("Toti divizorii comuni ai numerelor sunt:", all_dc(a,b))

def mul_com(x,y):
    mc=[]
    for i in range(1,6):
        mc.append(cmmmc(x,y)*i)
    return mc

print("Cinci multipli comuni ai numerelor sunt:", mul_com(a,b))

def cifre_comune(x,y):
    cc=[]
    for i in str(x):
        if i in str(y):
            cc.append(i)
        else:
            cc=cc
    return cc

print("Cifrele comune din numere sunt:", cifre_comune(a,b))

def cifre_prnr(x,y):
    c1n=[]
    for i in str(x):
        if i not in str(y):
            c1n.append(i)
        else:
            c1n=c1n
    return c1n

print("Cifrele care se gasesc in primul numar si nu se gasesc in al doilea sunt:", cifre_prnr(a,b))

def nr_div(x):
    nr=0
    for i in range(1,x+1):
        if x%i==0:
            nr+=1
        else:
            nr=nr
    return nr

def prietene(x,y):
    if nr_div(x)==nr_div(y):
        rez="sunt"
    if nr_div(x)!=nr_div(y):
        rez="nu sunt"
    return rez

print("Numerele date", prietene(a,b), "PRIETENE")