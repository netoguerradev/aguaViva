from manualInsertion import *
#essa aplicação servirá para o hóspede acompanhar seu consumo e ver a recompensa na qual tem direito

andar=int(input('''
Bem-vindo ao programa de recompensas!
Aqui você pode acompanhar seu consumo
e trocar por recompensas!
                        
Para começar, digite o andar do seu quarto: '''))
quartoselecionado=int(input("Agora, digite seu quarto: "))
if andar==1 or andar==2 or andar==3 and quartoselecionado==1 or quartoselecionado==2 or quartoselecionado==3:
    consumoquarto=andar_quarto[andar-1][quartoselecionado-1]
else:
    print("Quarto ou andar Indisponível!")
    
print('''      
    Recompensa 1 para economia de 80 ou mais litros de água
    Recompensa 2 para economia de 50 a 79 litros de água
    ''')
#a meta estabelecida é de acordo com o valor médio por quarto consumido pelo gestor atualmente
meta=350
pontos=meta-consumoquarto
if pontos>=80:
    print(f'Hóspede do quarto {andar}0{quartoselecionado}, você consumiu {consumoquarto} no total!')
    print(f'Isso significa que você economizou {pontos}! Obrigado por participar')
    print(f'Você tem direito a Recompensa 1!')

elif pontos<80 and pontos>=50:
    print(f'Hóspede do quarto {andar}0{quartoselecionado}, você consumiu {consumoquarto} no total!')
    print(f'Isso significa que você economizou {pontos} litros! Obrigado por participar')
    print(f'Você tem direito a Recompensa 2!')
elif pontos>0 and pontos<50:
    print(f'Hóspede do quarto {andar}0{quartoselecionado}, você consumiu {consumoquarto} no total!')
    print(f'Isso significa que você economizou {pontos} litros! Obrigado por participar')
    print(f'Entretanto, infelizmente você não atingiu a pontuação necessária para trocar por recompensas... :/')

else:
    print(f'Hóspede do quarto {andar}0{quartoselecionado}, você consumiu {consumoquarto} no total!')
    print(f'Infelizmente, você acabou ultrapassando a meta e não conseguindo somar pontos...')  
    print(f'Tente novamente na próxima!')