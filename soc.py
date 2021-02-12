#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime, time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ativandoLogin import *

import sys
import os



def ativandoCloudSoc(driver):
    arquivo = 'ultimas_soc.txt'
    print("Atualizar as o.s.", "iniciando..."+arquivo)
    http = 'https://extresso.seu.domino.br'
    print("Abrir navegador")
    if driver is None:
        driver = webdriver.Firefox()

    print("Acessar portal")
    time.sleep(2)
    driver.get(http)

    time.sleep(7)
    print('enviar login')

    ativandoLoginSoc(driver, http)
    time.sleep(4)

    print("acessando pagina de distribuicao de ordem de servico")
    time.sleep(2)

    driver.get(http)
    time.sleep(2)

    #driver.close()
    print("Fim do python SOC")
    #listaarquivos = os.listdir('/home/coffeM18/bots/soc_rodando')

    arq = open(arquivo)
    conteudo = arq.read()
    arquivosaida = open("/pasta/ultimas_soc.txt", "w")
    msg=[]
    msgtxt = ''
    arquivosaida.writelines(str(msgtxt))#guardando os valores no arquivo 
    
    linhasTable = driver.find_elements_by_tag_name('tr')
    for linha in linhasTable:
        if 'Distribuir' in linha.text:
            celulas = linha.find_elements_by_tag_name('td')
            print("Na coluna 4 temos:", celulas[4].text)
            if celulas[4].text != 'Distribuir':
                print("Linha errada, desculpa rss")
                continue
            print(linha.text)
            celulas[1].click() # Clicado em linha de DISTRIBUIR
            time.sleep(0.4)
    time.sleep(4)
    iframes = driver.find_elements_by_tag_name('iframe')
    i = 0
    msg=[]
    for iframe in iframes:
        i = i + 1
        print("Iframe " + str(i))
        try:
            driver.switch_to.frame(iframe)
            ## Insert text via xpath ##
            #elem = driver.find_element_by_xpath("/html/body/")
            linhasTable = driver.find_elements_by_tag_name('tr')
            msgtxt = '```'
            for linha in linhasTable: 
                msgtxt += linha.text.replace("Esta solicitação foi ", " ").replace("- - -","-").replace("e Extensão Rural"," ").replace("Informações do Contato ","").replace("que originou esta clique aqui", "").replace("Solicitação que originou:", "").replace("Departamento de Estradas de Rodagem do Estado do Paraná", "").replace("deve ser atendida", " ").replace("Cliente", " Cliente").replace("É faturavel? Não", " ").replace("Cidade de atendimento", " ").replace("Autor", " ").replace("E-mail", " ").replace("Tipo de Serviço ", "").replace(r"\r\n", " ").replace(r"\n", " ").replace('\n', '  ').strip().strip() + ' -'
                print(linha.text)
                    
                if 'Tipo de Serviço' in linha.text:
                    now = datetime.datetime.now() # Getting date and time

                    msgtxt = msgtxt + '```'
                    print('encontrado tipo de serviço - saindo do loop')
                    break
            #msgtxt=msgtxt.split('Autor')
            if msgtxt != '```':
                arquivosaida.writelines(str(msgtxt)+ ' ')#guardando os valores
                msg.append(msgtxt)
            
            ## Switch back to the "default content" (that is, out of the iframes) ##
            driver.switch_to.default_content()
        except:
            driver.switch_to.default_content()
            
    return msg 
    
if __name__ == '__main__':
    ativandoCloudSoc()
