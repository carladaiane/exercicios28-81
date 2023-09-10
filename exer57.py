""" algoritmo 57 
Entrar com as notas da PR 1 e PR2 e imprimir a média final: 
m truncada: 
arredondada: 
prog lea3O 
real pri, pr2, mf; 
imprima "\ndigite pri: 
leia pri; 
imprima "\ndigite pr2: 
leia pr2; 
mf <- ( pri + pr2 ) / 2; 
imprima "\nmedia truncada = , realint((mf- 0.5)+0.001); 
imprima "\nmedia arredondada = ", realint( mf+0.001); 
imprima 11 \n"; 
fi mprog """

pri = float(input('\ndigite pr1:'))
pr2 = float(input('\ndigite pr2:'))
mf = ( pri + pr2 ) / 2

print(f"\nmedia truncada = {round((mf- 0.5)+0.001)}")

print(f"\nmedia arredondada = {round( mf+0.001)}")

print (f"\n") 

