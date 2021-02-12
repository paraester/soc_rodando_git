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

usuario = 'seu_usuario_por_enquanto'
senha = 'sua_senha_por_enquanto'

def ativandoLoginRocket(driver, http):
    user = None
    passwd = None
    try:
        user = driver.find_element_by_name('emailOrUsername')
        passwd = driver.find_element_by_name('pass')
    except:
        print("Faltando campo de Usuario e senha")
        return
    if user and passwd:
        user.send_keys('usuario_do_bot')
        passwd.send_keys('senha_do_bot')
        passwd.send_keys(Keys.RETURN)
    else:
        print("Faltando campo de Usuario e senha")

def ativandoLoginSoc(driver, http):
    user = None
    passwd = None
    try:
        user = driver.find_element_by_name('user')
        passwd = driver.find_element_by_name('passwd')
    except:
        print("Faltando campo de Usuario e senha")
        return
    if user and passwd:
        user.send_keys(usuario)
        passwd.send_keys(senha)
        passwd.send_keys(Keys.RETURN)
    else:
        print("Faltando campo de Usuario e senha")

