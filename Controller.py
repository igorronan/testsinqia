from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime as dt
import os

class Controller:
    def __init__(self, url ,tempo):
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        options.add_argument("--start-maximized")
        options.add_argument("log-level=3")
        
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
        self.driver.get(self.url)
        self.tempoespera = tempo
        os.system("cls")
        time.sleep(self.tempoespera)
        
    def valida_item(self, tipo, nome, valor):
        driver = self.driver
        try:
            saida = driver.find_element(By.XPATH, value="//" + tipo + "[@" + nome + "='" + valor + "']").text
            if saida:
                time.sleep(self.tempoespera)
                return True
            print(f"{valor} nao encontrado")
            return False
        except:
            print(f"{valor} nao encontrado")
            return False
        

    def clicar(self, tipo, nome, valor):
        try:
            driver = self.driver
            botao_enviar =  driver.find_element(By.XPATH, value="//" + tipo + "[@" + nome + "='" + valor + "']")
            botao_enviar.click()
            time.sleep(self.tempoespera)
            return True
        except:
            print("Erro ao realizar clique")
            return False

    def preencher(self, tipo, nome, valor, dado):
        driver = self.driver
        preenche = driver.find_element(By.XPATH, value="//" + tipo + "[@" + nome + "='" + valor + "']")
        preenche.clear()
        preenche.send_keys(dado)

    def fechar(self):
        self.driver.close()





