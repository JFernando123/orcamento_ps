import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

chrome_install = ChromeDriverManager().install()
folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")
service = ChromeService(chromedriver_path)

# Iniciar navegador Chrome
driver = webdriver.Chrome(service=service)

# Navegar até a url
driver.get("https://virtualstorerc.pontosys.com:4433/") 
driver.maximize_window()

# Preencher o CNPJ
campo_cnpj = driver.find_element(By.XPATH, '//input[@name="input-cnpj"]')
driver.execute_script("""
    var input = arguments[0];
    input.value = '11111111111111';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", campo_cnpj)

# Clicar em avançar
driver.find_element(By.XPATH, "//button[@name='btn-avancar']").click()

# Selecionar Filial
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//select'))
)
select = Select(select_element)
select.select_by_value("3")

# Clicar em avançar
driver.find_element(By.XPATH, "//button[@name='btn-avancar']").click()
#driver.find_element(By.XPATH, "//button[@class='button button-md button-default button-default-md").click()

# Radio button Transação padrão
driver.find_element(By.ID, "rb-14-0").click()

# Desmarcar o checkbox "Todas" de Transações permitidas
driver.find_element(By.ID, "checkbox-17-0").click()

# Verificar se o checkbox Orçamento está marcado
combobox_prevenda = driver.find_element(By.ID, "checkbox-20-0")
is_selected = combobox_prevenda.get_attribute("aria-checked") == "true"

# Clicar em avançar
driver.find_element(By.XPATH, "//button[@name='btn-avancar']").click()

# Botão Salver as configurações
driver.find_element(By.NAME, "btn-salvar").click()

# Verificar se a caixa de permissão de supervisor apareceu
text = driver.find_element(By.CLASS_NAME, 'titulo').text
assert text == "Permissão de supervisor"

# Informar usuario
usuario_supervisor = driver.find_element(By.XPATH, "//input[@name='input-login-usuario']")
driver.execute_script("""
    var input = arguments[0];
    input.value = '15';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", usuario_supervisor)

# Informar senha supervidor
senha_supervisor = driver.find_element(By.XPATH, "//input[@name='input-senha-usuario']")
driver.execute_script("""
    var input = arguments[0];
    input.value = '2';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", senha_supervisor)

sleep(2)

# Clicar no botão Entrar
entrar = driver.find_element(By.XPATH, "//button[@name='btn-entrar']")
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
""", entrar)

sleep(5)
# Login do sistema
usuario_login = driver.find_element(By.NAME,'input-login')
driver.execute_script("""
    var input = arguments[0];
    input.value = 'elvis@pontosys.com';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", usuario_login)

usuario_senha = driver.find_element(By.NAME, 'input-senha')
driver.execute_script("""
    var input = arguments[0];
    input.value = 'Elv@135790';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", usuario_senha)

sleep(2)

# Clicar no botão Entrar
entrar = driver.find_element(By.XPATH, "//button[@name='btn-entrar']")
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
""", entrar)

sleep(2)

try:
    # Aguarde por alguns segundos para verificar se a mensagem aparece
    mensagem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'alert-hdr-0'))       
    )

    # Verifique se o usuário está logado em outro dispositivo
    if mensagem:
        print("Mensagem apareceu. Clicando no botão 'Sim'.")
        botao_sim = driver.find_element(By.XPATH, '//button[@class="alert-button alert-button-md btn-opcao-sim alert-button-default alert-button-default-md"]')  
        driver.execute_script("""
            var button = arguments[0];
            button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
            button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
            button.click();
        """, botao_sim)
    else:
        print("Mensagem não apareceu. Continuando a execução...")
except:
    # Mensagem não apareceu dentro do tempo limite
    print("Mensagem não encontrada.")

sleep(10)

# Acessar menu lateral
menu_lateral = driver.find_element(By.XPATH, '//button[@class="bar-buttons bar-buttons-md bar-button bar-button-md bar-button-default bar-button-default-md bar-button-menutoggle bar-button-menutoggle-md"]')  
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
    """, menu_lateral)

sleep(5)

# Clicar no botão Vendas do menu lateral
btn_venda = driver.find_element(By.XPATH, '/html/body/ion-app/ng-component/ion-menu/div/ion-content/div[2]/ion-list/button[2]/div[1]/div/ion-label/span')
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
    """, btn_venda)

# Verificar se está na tela de Orçamentos

text = driver.find_element(By.ID, 'tituloTopo').text
assert text == "Orçamento"

# Adicionar produto 'Salmão'
sleep(10)

produto_add = driver.find_element(By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-venda/ion-content/div[2]/div/ion-row/ion-col[1]/autocomplete/ion-item/div[1]/div/ion-input/input')
driver.execute_script("""
    var input = arguments[0];
    input.value = 'SALMÃO';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", produto_add)

# Depois de informado a descrição do produto, simulando o enter para pesquisar e carregar a lista de produtos
produto_add.send_keys(Keys.RETURN)

sleep(5)
# Enter novamente para selecionar o primeiro produto da lista carregada
produto_add.send_keys(Keys.ENTER)

# Adicionar a quantidade
qtd = driver.find_element(By.XPATH, '/html/body/ion-app/ng-component/ion-nav/page-venda/ion-content/div[2]/div/ion-row/ion-col[2]/ion-item/div[1]/div/ion-input/input')
driver.execute_script("""
    var input = arguments[0];
    input.value = '1';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", qtd)

sleep(2)

# Enter para adicionar o produto no orçamento
qtd.send_keys(Keys.ENTER)

sleep(5)

# Clicar no botão Finalizar Venda
btn_finalizar = driver.find_element(By.NAME, 'btn-finalizar-venda')
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
    """, btn_finalizar)

sleep(5)

# Informar o Vendedor "NENHUM".
vendedor = driver.find_element(By.XPATH, '/html/body/ion-app/ion-modal/div/ng-component/ion-content/div[2]/div/ion-row/ion-col[2]/autocomplete/ion-item/div[1]/div/ion-input/input')
driver.execute_script("""
    var input = arguments[0];
    input.value = 'NENHUM';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", vendedor)

vendedor.send_keys(Keys.ENTER)

sleep(3)

vendedor.send_keys(Keys.ENTER)

sleep(3)

# Adicionar Cliente "Consumidor".
cliente = driver.find_element(By.XPATH, '/html/body/ion-app/ion-modal/div/ng-component/ion-content/div[2]/div/ion-row/ion-col[3]/autocomplete/ion-item/div[1]/div/ion-input/input')
driver.execute_script("""
    var input = arguments[0];
    input.value = 'Consumidor';
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
""", cliente)

cliente.send_keys(Keys.ENTER)

sleep(2)

cliente.send_keys(Keys.ENTER)

sleep(2)

# Clicar em continuar para finalizar o orçamento.
btn_continuar = driver.find_element(By.XPATH, '/html/body/ion-app/ion-modal/div/ng-component/ion-content/div[2]/ion-row[2]/ion-col/div/button')
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
    """, btn_continuar)

# Aguardar impressão do cupom na tela, e depois fechar pela seta <- localizada no header da aplicação.

sleep(10)

btn_voltar = driver.find_element(By.XPATH, '/html/body/ion-app/ion-modal[2]/div/ng-component/ion-header/ion-navbar/div[2]/ion-buttons/button')
driver.execute_script("""
    var button = arguments[0];
    button.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
    button.dispatchEvent(new MouseEvent('mouseup', { bubbles: true }));
    button.click();
    """, btn_voltar)

# Aguardar voltar para a tela inicial do Orçamento e aguardar limpar todos os dados da tela para finalizar o teste.
sleep(15)

print('Testes Finalizados!')

driver.close()
driver.quit()
