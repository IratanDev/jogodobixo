import time
import os
import app

if __name__ == '__main__':
    contador = 0
    nome_ = input('Qual será o nome do seu pet? ')
    pet = app.Pet(nome=nome_)
    print(f'Olá! meu nome é {nome_}! *_*')
    print('******************************')
    while (pet.nivel_fome < 100) and (pet.nivel_energia > 0):
        pet.comer(+10)
        pet.brincar(-10)
        print(f'1-Alimentar {nome_}.')
        print(f'2-Brincar com {nome_}.')
        resposta = int(input('Resposta: '))
        if resposta == 1:
            pet.comer(-15)
        elif resposta == 2:
            pet.brincar(+15)
        print(f'Nivel de fome: {pet.retornar_nivel_fome()}%')
        print(f'Nivel de alegria: {pet.retornar_nivel_energia()}%')
        contador += 1
    else:
        if pet.retornar_nivel_fome() == 100:
            print(f'{nome_} morreu de fome.')
        else:
            print(f'{nome_} morreu de tristeza.')
        print('**************************************')
        print(f'Pontos: {contador}.')
        print(f'Recorde: 58 pontos (IratanDev)')




