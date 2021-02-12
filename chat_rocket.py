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


def ativandoCloudRocket(msgs, driver):
    http = 'https://chat.paas.pr.gov.br/'
    print("acessando rocketchat", "iniciando...")

    print("Abrir navegador")
    if driver is None:
        driver = webdriver.Firefox()
    
    #input("passe a senha e de enter aqui depois")

    print("Acessar portal do Rocket chat")
    time.sleep(2)
    driver.get('https://chat.rocket.chat.br/')

    time.sleep(3)
    print('enviar login')

    ativandoLoginRocket(driver, http)
    time.sleep(4)
    driver.get('https://chat.rocket.chat.br/group/canal_que_vai_receber_as_mensagens')
    print("acessando pagina do rocket pra enviar msg espera de 10 ")

    time.sleep(10)
    for i in range(10):
        try:
            #textarea = driver.find_element_by_class_name('rc-message-box__textarea')
            textarea = driver.find_elements_by_tag_name('textarea')
            textarea[0].send_keys('atualizando Distribuir SOC \r\n')
            time.sleep(0.4)
            textarea[0].send_keys(Keys.ENTER)
            time.sleep(1)
            for msg in msgs:
                print("???.??"+msg+"!!!.!!!")
                
                textarea[0].send_keys(msg)
                time.sleep(0.4)
                textarea[0].send_keys(Keys.ENTER)
                time.sleep(4)
            break
        except:
            print("deu ruim no enviar msg")
            time.sleep(3)


    #driver.close()
    print("Fim do python")

if __name__ == '__main__':
    ativandoCloud()









