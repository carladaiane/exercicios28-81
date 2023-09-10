""" algoritmo 67 
Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula: 
prestação = valor + (valor*(taxa/100)*tempo). 
prog lea4O 
real prest, valor, taxa; 
int tempo; 
imprima "\ndigite o valor da prestação: 
leia valor; 
imprima "\ndigite a taxa: 
leia taxa; 
imprima "\ndigite o tempo(numero de meses): 
leia tempo; 
prest <- valor+(valor*(taxa/100)*tempo); 
imprima "\no valor da prestacao em atraso e =", prest; 
imprima "\n"; 
fi mprog """

tempo = int(input('\ndigite o tempo(numero de meses): '))
valor = float(input('\ndigite o valor da prestação: '))
taxa = float(input('\ndigite a taxa: '))

prest = valor+(valor*(taxa/100)*tempo)


print(f'\no valor da prestacao em atraso é {prest:.2f}')

print(f"\n")