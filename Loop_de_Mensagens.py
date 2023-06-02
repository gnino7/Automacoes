import pyautogui as pg
import random
import time

time.sleep(5) # Tempo de espera para executar o código

mensagens = ["Oi", "Tudo bem?", "Como vai?", "Olá"] # Palavras chave para envio

for i in range(32): # Quantidade de envios
    msg = random.choice(mensagens)
    pg.write(msg)
    pg.press("enter")