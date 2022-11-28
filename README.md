## aguaViva
Este Projeto é referente a cadeira de Projetos 1 da faculdade Cesar School, consiste em uma solução desenvolvida para o grupo Chambres Hotéis visando diminuir o consumo
de água nos hotéis da empresa, para isso, foi desenvolvido um programa de recompensas regressivo em que o hóspede começa com uma quantidade máxima de pontos que vão
diminuindo a medida que o hóspede vai consumindo mais água do quarto, com os pontos restantes o mesmo pode troca-los por descontos em hospedagens futuras, desconto 
em empresas parceiras e produtos vendidos pelo hotel, além desse programa, possui um dashboard do gestor para visualizar o consumo em cada quarto, além de custo de cada
hospedagem em tempo real.

O projeto é dividido em 3 partes: Dispositivo físico, dashboard do gestor e programa de recompensas.

## Dispositivo Físico
Materiais utilizados:
Arduino UNO R3
Sensor de vazão YS-F201
Módulo Bluetooth HC-05
Bateria 9v
(O esquema elétrico do protótipo encontrase na pasta images e é nomeada como flowSensor)

O intuito do protótipo é conseguir obter o dado da vazão de um sistema hidráulico(Cada quarto do hotel) e esse dado é enviado pelo módulo blueooth para um computador
usando um código python através da biblioteca Serial, o código encontra-se na pasta application e é nomeada con_ino_py, para baixar a biblioteca basta digitar no terminal:
```
$ pip install serial
```
O código Arduino do dispositivo encontra-se na pasta arduinoFlowSensor com nome de codigoSensorVazao

## Dashboard do gestor
O dashboard foi construído em duas etapas, uma tela interativa mais simples para visualização do consumo em cada quarto e outro código utilizando python puro que conta
com mais funcionalidadesm, para construção das telas, foi utilizada a biblioteca Tkinter que pode ser obtida através do comando: 
´´´
$pip install tkinter
```
A tela interativa está na pasta application com nome de dashboard_screen
O código em python com todas as funcionalidades encontra-se na pasta main com nome de dahsboard

## Programa de Recompensas 
O programa de recompensas é onde os hóspedes conseguem visualizar seus gastos com água no hotel e verificar seus pontos e suas possíveis recompensas.
O código do mesmo encontra-se na pasta main e está nomeada como panelHost

## Design 
Na pasta Design está um arquivo txt que contem os links dos protótipos de alta fidelidade do dashboard do gestor e do programa de recompensas.
