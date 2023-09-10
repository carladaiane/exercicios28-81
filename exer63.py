""" Criar um algoritmo que efetue o cálculo do salário líquido de um professor. Os da￾dos fornecidos serão: valor da hora aula, número de aulas dadas no mês e per￾centual de desconto do INSS. 
prog 1ea36 
int na; 
real vha, pd, td, sb, si; 
imprima "\nhoras trabalhadas: 
leia na 
imprima "\nvaior da hora-aula: 
leia vha 
imprima "\npercentuai de desconto: H; 
leia pd 
sb <- na * vha; 
td <- ( pd / 100) * sb; 
501 s] <- sb — td; 
imprima "\nsalario liquido: ",sl; 
imprima U\flhl; """

na = int(input('\nhoras trabalhadas: '))
vha = float(input('\nvalor da hora-aula:'))
pd = float(input('\npercentual de desconto: '))
sb = na * vha
td = ( pd / 100) * sb
sl = sb - td

print(f"\nsalario liquido: {sl}")
print(f"\n")



