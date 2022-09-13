n=int(input('Dati numarul de elemente ale listei:'))

def lista_int():
    l_int=[]
    for i in range(n):
        elem=int(input('Elementul '+str(i)+' este:'))
        l_int.append(elem)
    return l_int

print(lista_int())