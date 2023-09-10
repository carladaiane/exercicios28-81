""" Dado um polígono convexo de n lados, podemos calcular o número de diagonais 
diferentes (nd) desse polígono pela fórmula : nd = n (n —3)! 2. Fazer um algorit￾mo que leia quantos lados tem o polígono, calcule e escreva o número de diago￾nais diferentes (nd) do mesmo. 
56 
prog lea5l 
real nd; 
int n; 
imprima "\ndigite o numero de lados do poligono II, 
leia n, 
nd<_n* (n-3) /2; 
imprima "\nnumero de diagonais: ", nd; 
imprima hI\H; 
fi mprog
 """


n = int (input(f'\ndigite o numero de lados do poligono: '))
nd = n* (n-3) /2

print(f"\nnumero de diagonais: {nd:.2f}")

print(f"\n")