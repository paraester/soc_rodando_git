#!/usr/bin/env python3
# -- coding: utf-8 --

import sys
import datetime, time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ativandoLogin import *
from soc import *
from chat_rocket import *
import sys
import os

driver = None


def iniciar(driver):
    msgs = ativandoCloudSoc(driver)
    if len(msgs) > 0:
        ativandoCloudRocket(msgs, driver)
        print('enviado')
    else:
        arquivo = 'ultimas_soc.txt'
        arq = open(arquivo)
        conteudo = arq.read()
        arquivosaida = open("/pasta/ultimas_soc.txt", "w")
        now = datetime.datetime.now() # Getting date and time
        msgtxt = 'Nenhuma o.s. pra distribuir agora'+ str("Hora: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second) + str("Data: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year)
        arquivosaida.writelines(str(msgtxt)+ ' ')#guardando os valores
        print('Nenhuma o.s. pra distribuir agora')
        arquivosaida.close()
        #driver.navigate().refresh

if __name__ == '__main__':
    print("Abrindo o navegador")
    driver = webdriver.Firefox()
    while True:
        iniciar(driver)
        time.sleep(600)
        time.sleep(600)
        print('em 10min lá vamos nois di novo')
            
