from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

servico =Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=options)

meuLogin = "*********" 
minhaSenha = "********"

navegador.get("https://sei.univem.edu.br/")
navegador.find_element(By.ID, 'form:usuario').send_keys(meuLogin)
navegador.find_element(By.ID, 'form:senha').send_keys(minhaSenha)
navegador.find_element(By.ID, 'form:loginBtn:loginBtn').click()


