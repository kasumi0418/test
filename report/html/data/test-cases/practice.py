
def arrp(n):
    Arra = [i**3 for i in range(1, n+1)]
    Arrb = [i**2 for i in range(1, n+1)]
    Arrc = []

    for i in range(n):
        Arrc.append(Arra[i]+Arrb[i])
    return Arrc


print(arrp(3))
