import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_install = ChromeDriverManager().install()
folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")
service = ChromeService(chromedriver_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Ocultar alguns Logs, Bug de USB no ChromeDriver 88

# Iniciar navegador Chrome
driver = webdriver.Chrome(service=service)


# Navegar até a url
driver.get("https://virtualstore.pontosys.com/#/configlocal")
# driver.get("https://virtualstore.pontosys.com:4433/") 
driver.maximize_window()
# Espera o elemento ficar visível
wait = WebDriverWait(driver,10)
input_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='input-cnpj']")))

# Verifica se o elemento está habilitado
if input_element.is_enabled():
    input_element.send_keys("11111111111111")
else:
    print("Elemento não está habilitado para interação.")



# Timer para a tela ficar aberta
time.sleep(2)
print(input_element)
