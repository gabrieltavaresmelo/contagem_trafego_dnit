# import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def driversetup(isChrome):
    if(isChrome):
        print('Chrome')
        options = webdriver.ChromeOptions()
        #run Selenium in headless mode
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        #overcome limited resource problems
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("lang=en")
        # #open Browser in maximized mode
        # options.add_argument("start-maximized")
        # #disable infobars
        # options.add_argument("disable-infobars")
        # #disable extension
        # options.add_argument("--disable-extensions")
        # options.add_argument("--incognito")
        # options.add_argument("--disable-blink-features=AutomationControlled")
        
        driver = webdriver.Chrome(options=options)

        # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

    else:
        print('Firefox')
        option = Options()
        option.headless = True
        # option.set_preference("http.response.timeout", 5)
        # option.set_preference("dom.max_script_run_time", 5)
        driver = webdriver.Firefox(options=option)

    return driver

def pagesource(url, driver):
    driver = driver
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    driver.close()
    return soup


isChrome = True
url = 'https://servicos.dnit.gov.br/dadospnct/ContagemContinua'
# url = 'https://covid.saude.gov.br'
driver = driversetup(isChrome)

print(url)

# pagesource(url, driver).prettify()
# driver.set_page_load_timeout(500)
# driver.implicitly_wait(180)
driver.get(url)
# driver.find_element("xpath", '//*[@id="UF"]').click()
# csv_button = driver.find_element('xpath', '/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')

driver.implicitly_wait(5) #Dependente da velocidade da internet. Ideal seria um comando que entendesse quando a página fosse completamente carregada.

#Clicando nas opções de filtro para acesso dos dados de interesse:

#Seleção do estado CE
driver.find_element("xpath", '//body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/div[1]/div/select/option[6]').click()

#Seleção da va BR-020:
driver.find_element("xpath", '//body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/form/div[2]/div[2]/div/select/option[2]').click()

#Seleção de todos os postos de controle:
driver.find_element("xpath", '//body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/form/div[3]/div').click()
driver.find_element("xpath", '//body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/form/div[3]/div/div/ul/li[3]/label/input').click()
driver.implicitly_wait(1)

#Seleção do botão BUSCAR:
driver.find_element("xpath", '//body/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/form/div[4]/input').click()
driver.implicitly_wait(5)


############################################
## 2014
## 

#Seleção do ANO 2014:
driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[1]').click()
driver.implicitly_wait(3)

#Seleção da Aba Volume Total Diário:
driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[3]/ul/li[2]/a').click()
driver.implicitly_wait(3)

#Seleção do mês:
driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[3]/div/div[2]/div[1]/select/option[5]').click()
driver.implicitly_wait(3)

#Abre o modal VMD:
driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[3]/div/div[2]/div[4]/input').click()
driver.implicitly_wait(8)

#Download do arquivo Excel:
driver.find_element("xpath", '//body/div[4]/div[1]/span/span/input').click()
driver.implicitly_wait(5)

#Ler o conteúdo da Table:
element = driver.find_element("xpath", '/html/body/div[4]')
driver.implicitly_wait(5)

elementHTML = element.get_attribute('outerHTML') #gives exact HTML content of the element
elementSoup = BeautifulSoup(elementHTML,'html.parser')
# print(elementSoup)
print('----------------------')
# print(elementSoup.prettify())
print('----------------------')
# print(type(elementSoup))

with open('vmd2014.txt', 'w') as f:
    f.write(str(elementSoup))

tableElement = elementSoup.find(id='TabVtd230202')
# print(tableElement.prettify())

with open('table2014.txt', 'w') as f:
    f.write(str(tableElement))

tableStr = str(tableElement)
dfs = pd.read_html(tableStr, encoding='UTF-8')
df = dfs[0].dropna(axis=0, thresh=4)
df = df.rename(columns={'Unnamed: 0': 'Classe', 'Unnamed: 1': 'Descrição', 'Unnamed: 2': 'Sentido', 
                        'Unnamed: 3': '1', 'Unnamed: 4': '2', 'Unnamed: 5': '3', 'Unnamed: 6': '4', 
                        'Unnamed: 7': '5', 'Unnamed: 8': '6', 'Unnamed: 9': '7', 'Unnamed: 10': '8', 
                        'Unnamed: 11': '9', 'Unnamed: 12': '10', 'Unnamed: 13': '11', 'Unnamed: 14': '12', 
                        'Unnamed: 15': '13', 'Unnamed: 16': '14', 'Unnamed: 17': '15', 'Unnamed: 18': '16', 
                        'Unnamed: 19': '17', 'Unnamed: 20': '18', 'Unnamed: 21': '19', 'Unnamed: 22': '20', 
                        'Unnamed: 23': '21', 'Unnamed: 24': '22', 'Unnamed: 25': '23', 'Unnamed: 26': '24', 
                        'Unnamed: 27': '25', 'Unnamed: 28': '26', 'Unnamed: 29': '27', 'Unnamed: 30': '28',
                        'Unnamed: 31': '29', 'Unnamed: 32': '30', 'Unnamed: 33': '31', 'Unnamed: 34': 'Total'})

df.to_csv('table2014.csv', sep=';', encoding='utf-8')

############################################
## 2015
## 

# #Seleção do ANO 2015:
# driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[2]').click()
# driver.implicitly_wait(3)


############################################
## 2016
## 

# #Seleção do ANO 2016:
# driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[3]').click()
# driver.implicitly_wait(3)


############################################
## 2017
## 

# #Seleção do ANO 2017:
# driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[4]').click()
# driver.implicitly_wait(3)


############################################
## 2018
## 

# #Seleção do ANO 2018:
# driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[5]').click()
# driver.implicitly_wait(3)


############################################
## 2021
## 

# #Seleção do ANO 2021:
# driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[6]').click()
# driver.implicitly_wait(3)


############################################
## 2022
## 

# #Seleção do ANO 2022:
# driver.find_element("xpath", '//body/div[2]/div[4]/div/div/div/div[3]/div/div/div[2]/div/a[7]').click()
# driver.implicitly_wait(3)

