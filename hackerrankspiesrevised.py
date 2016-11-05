from random import shuffle

def spies(N):
    """ makes sure all there are no two spies in any row or column and no three 
        spies in any 45 or 135 degree line"""
    
    lista = range(1,N+1)
    shuffle(lista)

    print lista
    count = 1
    while count > 0:
        count = 0
        for i in range(N-2):
            if i == N-3:
                if lista[i] == lista[i+1] + 1 and lista[i] == lista[i+2] + 2:
                    temp = lista[i]
                    lista[i] = lista[0]
                    lista[0] = temp
                    count += 1
                elif lista[i] == lista[i+1] - 1 and lista[i] == lista[i+2] - 2:
                    temp = lista[i]
                    lista[i] = lista[0]
                    lista[0] = temp
                    count += 1

            elif lista[i] == lista[i+1] + 1 and  lista[i] == lista[i+2] + 2:
                
                temp = lista[i]
                lista[i] = lista[i + 3]
                lista[i+3] = temp
                count += 1
            elif lista[i] == lista[i+1] - 1 and lista[i] == lista[i+2] - 2:
                
                temp = lista[i]
                lista[i] = lista[i+3]
                lista[i+3] = temp
                count += 1
    print lista

spies(5)
spies(15)
spies(7)
spies(9)
