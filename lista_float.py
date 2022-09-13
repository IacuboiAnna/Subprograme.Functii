n=int(input('Dati numarul de elemente ale listei:'))

def lista_float():
    l_float=[]
    for i in range(n):
        elem=float(input('Elementul '+str(i)+' este:'))
        l_float.append(elem)
    return l_float

print(lista_float())