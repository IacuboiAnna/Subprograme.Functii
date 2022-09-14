a=int(input("Dati numaratorul primei fractii:"))
b=int(input("Dati numitorul primei fractii:"))
c=int(input("Dati numaratorul fractiei a doua:"))
d=int(input("Dati numitorul fractiei a doua:"))

def suma(x,y,z,t):
    s=((x*t)+(y*z))/(y*t)
    return s

def produs(x,y,z,t):
    p=(x*z)/(y*t)
    return p

print("Rezultatul adunarii fractiilor este:", suma(a,b,c,d))
print("Rezultatul inmultirii fractiilor este:", produs(a,b,c,d))