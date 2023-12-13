# Criar função que vai perguntar o nome e idade do usuário e retornar isso em uma mensagem de boas vindas.

# Resolução do exercício:
def boas_vindas():
    nome = input('Qual o seu nome? ')
    idade = input('Qual a sua idade? ')
    return f'Olá {nome}! Você tem {idade} anos.'

print(boas_vindas())

# Aula 002 - Resolvido
# Aula https://www.youtube.com/watch?v=FNqdV5Zb_5Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=8