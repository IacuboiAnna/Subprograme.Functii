n=int(input('Dati numarul de elemente ale listei:'))

def lista_float():
    l_float=[]
    for i in range(n):
        elem=float(input('Elementul '+str(i)+' este:'))
        if isinstance(elem,float)==True:
            l_float.append(elem)
        else:
            print("Restartati si introduceti un numar real")
    return l_float

print(lista_float())
