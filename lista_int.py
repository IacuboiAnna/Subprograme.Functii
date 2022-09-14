n=int(input('Dati numarul de elemente ale listei:'))

def lista_int():
    l_int=[]
    for i in range(n):
        elem=int(input('Elementul '+str(i)+' este:'))
        if isinstance(elem,int)==True:
            l_int.append(elem)
        else:
            print("Restartati si introduceti un numar intreg")
    return l_int

print(lista_int())
