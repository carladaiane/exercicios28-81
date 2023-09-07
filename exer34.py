""" Ler um número inteiro e imprimir seu sucessor e seu antecessor.
prog lea7
int numero, suc, ant;
imprima " \n entre com um numero:
leia numero;
ant <- numero —1;
suc <- numero +1;
imprima " \no sucessor e 1", suc,"b o antecessor e b", ant;
imprima " \n " ;
fimprog  """

numero = int(input("\n Entre com um numero:"))

suc = numero+1

ant = numero-1

print(f'\nO Sucessor de {numero} é {suc} e o antecessor é {ant}')

print(f'\n')
