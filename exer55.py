""" algoritmo 55 
Criar um algoritmo que calcule e imprima a área de um losango. 
prog 1ea28 
real diagmaior, diagmenor, area; 
imprima "\nmedida da diagonal maior: 
leia diagmaior; 
imprima "\nmedida da diagonal menor: 
leia diagmenor; 
area <- (diagmaior * diagmenor)/2; 
imprima "\narea =", area; 
imprima "\n"; 
fi mprog """

diagmaior = float (input("\nDigite a medida da diagonal maior: "))
diagmenor = float (input("\nDigite a medida da diagonal menor: "))
area = (diagmaior * diagmenor)/2

print( f"\narea = {area:.2f}")
print(f"\n")

