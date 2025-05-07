""""Peça ao usuário o tamanho da senha.
Pergunte se ele quer incluir números, letras maiúsculas, minúsculas e caracteres especiais.
Gere a senha aleatória com base nas opções escolhidas.
Exiba a senha gerada."""

import random
import string

senha_do_usuario = int(input('Digite o tamanho da sua senha: '))
print(f'Seua senha tera:{senha_do_usuario} Caracteres') 

incluir_letras = input('Deseja incluir letras ou numeros?(Sim/Não) ').lower() == 'sim'
incluir_numeros = input('Deseja incluir números? (Sim/Não) ').lower() == 'sim'
incluir_especiais = input('Deseja incluir caracteres especiais? (Sim/Não)' ).lower() == 'sim'


chars = ''
if incluir_letras:
    chars += string.ascii_letters
if incluir_numeros:
    chars += string.digits
if incluir_especiais:
    chars += string.punctuation        


def gerar_senha(comprimento=12):
    senha = []
    for i in range (comprimento):
        senha.append(random.choice(chars))
    senha = ''.join (senha) 
    return ''.join(senha)

if chars:
    print(f'Sua senha gerada é: {gerar_senha(senha_do_usuario)}')

else:
    print('Nenhuma opção de caractere foi selecionada para gerar senha.')
      
       




