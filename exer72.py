""" algoritmo 72 
Criar um algoritmo que leia o valor de um depósito e o valor da taxa de juros. Calcular e imprimir o valor do rendimento e o valor total depois do rendimento. 
prog 1ea45 
real deposito, taxa, valor, total; 
imprima "\nentre com depósito: ; 
leia deposito; 
imprima "\nentre coma taxa de juros: "; 
leia taxa; 
valor <- deposito*taxa/100 ; 
total <- deposito + valor; 
imprima "\nRendimentos: II valor, "\nTotal: ", total; 
imprima "\n"; 
fi mprog """


deposito = float (input(f'\nentre com hora atual:'))
taxa = float (input(f'\nentre coma taxa de juros: '))
valor = deposito*taxa/100
total = deposito + valor

print(f'\nRendimentos: {valor}, \nTotal:{total}')

print(f"\n")