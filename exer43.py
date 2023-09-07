import math as m

""" algoritmo 43
Entrar com um número e imprimir o logaritmo desse número na base 10.
prog leal6
42 1 real num, logaritmo;
imprima "\nentre com o logaritmando:
leia num;
logaritmo <- log(num) / log(10);
imprima "\nlogaritmo: ", logaritmo;
imprima "\n";
fimprog """

num = int(input('Digite um número:'))

logaritmo = m.log(num) / m.log(10)

print(f'\nO logaritmo desse número é {logaritmo}')

print(f'\n')