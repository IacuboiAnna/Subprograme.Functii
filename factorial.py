n=int(input("Dati n:"))
m=int(input("Dati m:"))

def factorial(x):
    f=1
    for i in range(1,x):
        f=f*i
    return f

if n>=m:
    print("Numarul de combinari este:", factorial(n)/(factorial(m)*factorial(n-m)))
else:
    print("Restartati si introduceti un n, astfel incat n>m")