"""
CONSTANTE = "vARIAVEIS" que não vão mudar
muitas condições no msmo if (ruim)
    <- contagem de complexidade (ruim)
"""
velocidade = 67 #velocidade atual do carro
local_carro = 102 #local do carro na estrada

RADAR_1 = 60 #VELO MAX DO RADAR 1
LOCAL_1 = 100 #LOC ONDE O RADAR 1 ESTA
RADAR_RANGE = 1 # A DIST ONDE O RADAR PEGA

if velocidade > RADAR_1:
    print('Velo car passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
          velocidade > RADAR_1:
    print('car mutado em radar 1')

#contra barra servo para pular linha 
