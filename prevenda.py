from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

        
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Ocultar alguns Logs, Bug de USB no ChromeDriver 88
navegador = webdriver.Chrome(options=options)

navegador.get('https://virtualstore.pontosys.com/')
navegador.maximize_window()


campo_cnpj = navegador.find_element(By.XPATH, '//input[@name="input-cnpj"]')
campo_cnpj.send_keys('11111111111111')

print('passou')

sleep(5)
