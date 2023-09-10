""" algoritmo 60 
Entrar com a razão de uma PA e o valor do 1 2 termo. Calcular imprimiro 10 termo da serie 
prog 1ea33 
int dec, razao, termo, 
imprima "\nEntrar com o lo termo: 
leia termo, 
imprima "\nEntrar com a razao 
leia razao, 
dec <- termo + 9 razao, 
imprima "\nO 10 termo desta P.A. e ", dec, 
imprima " \n, 
fi mprog """


razao = int(input('\nEntrar com a razao:'))
termo = int(input('\nEntrar com o termo:'))
dec =  termo + 9 *razao
print(f"\nO 10 termo desta P.A. é {dec}")
print(f" \n")


