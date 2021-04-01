import random
x=random.randint(1,10)
y=random.randint(1,2)
liczba=x*y
#print("wylosowana liczba" , x**y)
for i in range(10):
    odp=input ("o jakiej liczbie podniesionej do 1 lub 2 potegi mysle z zakresu od 1-10  mysle?")
    if liczba== int(odp):
        print("super! umiesz czytac w myslach")
        break

    else:
        print("oj, sproboj raz jeszcze")
        print()
