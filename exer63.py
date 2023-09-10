na = int(input('\n Horas trabalhadas: '))
vha = float(input('\n Valor da hora-aula:'))
pd = float(input('\n Percentual de desconto: '))
sb = na * vha
td = ( pd / 100) * sb
sl = sb - td

print(f"\nsalario liquido: {sl}")
print(f"\n")



