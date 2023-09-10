"""
Entrar com um nome e imprimir: 
todo nome: 
primeiro caractere: 
ultimo caractere: 
do primeiro ate o terceiro: 
quarto caractere: 
todos menos o primeiro: 
os dois ultimos: 
prog 1ea22 
string nome;
int n; 
imprima 11 \nentre com nome: 
leia nome; 
imprima "\ntodo nome: " , nome; 
imprima "\nprimeiro caractere: ", strprim(nome); 
imprima "\nultinio caractere: ", strult(nome); 
imprima " \nprimeiro ao terceiro caractere: ", strnprim(nome,3); 
imprima "\nquarto caractere: ", strelem(nome,3); 
imprima "\ntodos menos o primeiro: ", strresto ( nome); 
n <-strtam(nome) —2; 
imprima "\nos dois ultimos " , strnresto(nome,n), 
imprima " \n " ; 
fimprog 

"""

nome = input('\n Entre com nome: ')

print(f"\ntodo nome: {nome}" )
print(f"\nprimeiro caractere: {nome[0]}")
print(f'\nultimo caractere: {nome[-1]}')
print(f"\nprimeiro ao terceiro caractere: {nome[0:3]}" )
print(f"\nquarto caractere: {nome[3]} ")
print(f"\ntodos menos o primeiro: {nome[1:]}")
print(f"\nos dois ultimos: {nome[-2:]}" )

print("\n")















