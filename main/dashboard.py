#importa dados da aplicação de inserção manual de dados
from manualInsertion import *

#menu de opções de visualização   
menu=int(input('''
Digite [1] para Consumo Geral
Digite [2] para Consumo por Quarto
Digite [3] para Painel de Recompensas
Digite: '''))
#mostra o consumo geral do hotel.
if menu==1:
      print('''
                Consumo Geral
                
          ''')
      a1=andar_quarto[0]
      a2=andar_quarto[1]
      a3=andar_quarto[2]
      total=sum(a1)+sum(a2)+sum(a3)
      print(f"O Hotel está consumindo {total}")
      #os calculos de valores de consumo foi utilizado a partir da estrutura tarfifária da CASAL
      if total>10000:
            print(f'O valor total do hotel é R${(total-10000)*19.74+124.20}')
      else:
            print(f'O valor total do hotel é R${total*12.42}')

    
#mosta o consumo por quarto, sendo necessário que o usuário indique o quarto e o andar 
elif menu==2:
      print('''
          
                Consumo por Quarto
    
          ''')
      escolhaandar=int(input("Escolha Andar: "))
      escolhaquarto=int(input(f"Escolha o quarto do {escolhaandar}: "))
      print(f"O consumo do quarto {escolhaquarto}0{escolhaandar} é {andar_quarto[escolhaandar-1][escolhaquarto-1]} litros.")
    
            
        
#nesta opção, o gestor pode acessar o painel de recompensas       
elif menu==3:
      print('''
      Painel de Recompensas do Hóspede
          ''')
      #será aberto outro menu onde ele pode verificar as recompensas que está disponiblizando ou
      #pode ser visto a pontuação por hóspede
      menu_recompensa=int(input('''
                              
    Digite [1] para visualizar pontos do hospedes
                              
    Digite [2] para visualizar recompensas disponíveis
                              
    Digite: '''))
      if menu_recompensa==1:
            meta = 350
            andar=int(input("Digite o andar: "))
            quartoselecionado=int(input("Digite o quarto:"))
            consumo=andar_quarto[andar-1][quartoselecionado-1]
            pontos=meta-consumo
      
            if pontos>=80:
                  print(f"O Hóspede do quarto {andar}0{quartoselecionado} tem direito a Recompensa 1")
            elif pontos>49 and pontos<80:
                  print(f"O Hóspede do quarto {andar}0{quartoselecionado} tem direito a Recompensa 2")
            else:
                  print(f"O Hóspede do quarto {andar}0{quartoselecionado} não tem direito a recompensa.")
            
      elif menu_recompensa==2:
            print('''
      Painel de Recompensa dos Hóspedes
      Recompensa 1 para economia de 80 a 100 litros de água
      Recompensa 2 para economia de 50 a 79 litros de água
            ''')   
      