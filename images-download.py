# encoding: utf-8

import DuckDuckGoImages as ddg		#pip install DuckDuckGoImages


filtro = 'Construção'
destino = './images-test/'

print('Iniciando downloads...')
try:
    ddg.download(filtro, folder=destino, remove_folder=False, parallel=True)
except Exception as e:
    print("type error: ", e)
print('Downloads concluidos...')