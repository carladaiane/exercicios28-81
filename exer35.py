""" Ler nome, endereço e telefone e imprimi-los.
prog lea8
string nome, endereco, telefone;
imprima "\nentre com nome:
leia nome;
imprima "\nentre com endereco:
leia endereco;
imprima "\nentre com telefone:
leia telefone;
imprima "\n\n\n";
imprima "\nNome : ",nome;
imprima "\nEndereco: ",endereco;
imprima \nTelefone: ",telefone;
imprima "\n";
fimprog  """

nome = input("Digite seu nome:")
ender = input("Digite seu endereço:")
tel = input("Digite seu telefone:")


print("\n\n\n")

print(f'\n Nome : {nome}')
print(f'\n Endereço : {ender}')
print(f'\n Tel : {tel}')

print("\n")