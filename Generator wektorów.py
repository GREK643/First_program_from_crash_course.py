import random as rn
dim=int(input("Podaj wymiar ukladu:"))
sup=int(input("Podaj supremum zbioru:"))
v1=[]
i=0
while i< dim:
    liczba=rn.randint(1,sup)
    if v1.count(liczba)==0:
        v1.append(liczba)
        i=i+1
print("wylosowany wektor to:", v1)

