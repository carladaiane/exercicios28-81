""" algoritmo 41
Entrar com quatro números e imprimir a média ponderada, sabendo-se que os
pesos são respectivamente: 1, 2, 3 e 4.
prog leal4
real a, b, c,d, mp;
imprima "\nentre com 1 numero:
leia a;
imprima \nentre com 2 numero:
leia b;
imprima "\nentre com 3 numero:
leia c;
imprima "\nentre com 4 numero:
leia d;
mp <- (a*1 + b*2 + c*3 + d*4)/10 ;
imprima "\nmedia ponderada: ", mp;
imprima "\n";
fi mprog """


num1= int(input('Digite o primeiro número:'))
num2= int(input('Digite o segundó número:'))
num3= int(input('Digite o terceiro número:'))
num4= int(input('Digite o quarto número:'))

mp = (num1*1 + num2*2 + num3*3 + num4*4)/10

print(f'(\nA média ponderada é {mp})')

print(f'\n')





