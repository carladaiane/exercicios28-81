import math as m

""" algoritmo 44
Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo.
prog leal7
real num, base, logaritmo;
imprima "\nentre com o logaritmando: II;
leia num;
imprima \nentre com a base: ";
leia base;
logaritmo <- log(num) / log(base);
imprima "\no logaritmo deb", num, "bna baseb",base, "be:b", logaritmo;
imprima "\n";
fi mprog """

num = float(input('Digite um número:'))

base = float(input('Digite o numero base:'))

logaritmo = m.log(num) / m.log(base)

print(f'\nO logaritmo do número digitado é {logaritmo}')

print(f'\n')