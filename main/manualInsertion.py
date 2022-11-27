#permite a inserção manual de 3 quartos por andar, considerando 3 andares;
#futuramente será substituido por dados coletados pelo sensor.
andar_quarto=[[],[],[]]
for l in range(3):
    for c in range(3):
        andar_quarto[l].append(float(input(f"Digite volume do quarto {l+1}0{c+1}:")))