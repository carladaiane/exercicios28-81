""" Criar um algoritmo que leia um valor de hora e informe quantos minutos se pas -
saram desde o iníciõ do dia. 
prog lea44 
int hora, tminuto, minuto, 
imprima "\nentre com hora atual: 
leia hora; 
imprima "\nentre com minutos: 
leia minuto; 
tminuto <- hora * 60 + minuto; 
imprima "\nAte agora se passaram: ", tminuto, " minutos"; 
imprima "\n";

 """


hora = int (input(f'\nentre com hora atual:'))
minuto = int (input(f'\nentre com minutos: '))
tminuto = hora * 60 + minuto

print(f'\nAte agora se passaram: {tminuto} minutos')

print(f"\n")