""" algoritmo 40
Entrar com dois numeros inteiros e imprimir a seguinte saída:
dividendo
divisor:
quociente:
resto
prog leal3
int quoc, rest, vali, va12;
imprima "\nentre com o dividendo:
leia vali;
imprima "\nentre com divisor.-
leia val2,
quoc <- vali div val2,
rest <- vali % va12;
imprima "\n\n\n",
imprima "\ndividendo ", vali,
imprima "\ndivisor ", va12,
imprima "\nquociente ", quoc,
imprima "\nresto ", rest,
imprima "\n",
fimprog  """


num1 = int(input('Digite o primeiro número:'))

num2 = int(input('Digite o segundo número:'))


dividendo= num1
divisor= num2
quociente= num1//num2
resto= num1%num2

print(f'\nO dividendo é {dividendo}')
print(f'\nO divisor é {divisor}')
print(f'\nO quociente é {quociente}')
print(f'\nO resto é {resto}')


print(f'\n')
