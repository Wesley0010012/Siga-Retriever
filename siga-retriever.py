from getpass import getpass

import pyautogui as pag

from src.consts import *
from src.browser_adapter import BrowserAdapter
from src.retriever import Retriever

username = input("Digite seu usuário: ")
password = getpass("Digite sua senha: ")

browserAdapter = BrowserAdapter.generate()

pag.sleep(1)

retriever = Retriever(browserAdapter['adapter'], browserAdapter['by'].XPATH)
retriever.goTo(URL)

pag.sleep(1)

retriever.writeInElement(retriever.findElement(USERINPUT), username)
retriever.writeInElement(retriever.findElement(PASSWORDINPUT), password)
retriever.clickInElement(retriever.findElement(LOGINBUTTON))

pag.sleep(1)

if retriever.findElement(LOGINERROR) and retriever.findElement(LOGINERROR).get_attribute('innerHTML'):
    print("Usuário ou senha inválidos!")
    retriever.close()
    quit()

pag.sleep(1)
retriever.goTo(FALTASURL)
pag.sleep(1)

i = 1

data = []

while True:
    tempQuery = f"//*[@id=\"span_vACD_DISCIPLINANOME_{str(i).zfill(4)}\"]"
    nomeSpan = retriever.findElement(tempQuery)
    
    if not nomeSpan:
        break
        
    data.append({})
    data[i - 1]['nome'] = nomeSpan.get_attribute('innerHTML')
    tempQuery = f"//*[@id=\"span_vAUSENCIAS_000{i}\"]"
    data[i - 1]['faltas'] = retriever.findElement(tempQuery).get_attribute('innerHTML').strip(" ")
    i += 1

pag.sleep(1)
retriever.goTo(NOTASURL)
pag.sleep(1)

for i in range(1, len(data) + 1):
    tempQuery = f"//*[@id=\"span_vACD_ALUNOHISTORICOITEMMEDIAFINAL_{str(i).zfill(4)}\"]"
    notaSpan = retriever.findElement(tempQuery)
    
    if not notaSpan:
        break

    data[i - 1]['nota'] = notaSpan.get_attribute('innerHTML').strip(" ")


print()

printSize = len(data[0]['nome'])

for i in range(1, len(data)):
    testSize = len(data[i]['nome'])

    if printSize < testSize:
        printSize = testSize

for i in range(len(data)):
    print(f"Nome: {data[i]['nome'].ljust(printSize)} || Nota: {data[i]['nota']} || Faltas: {data[i]['faltas']}")
        
        
retriever.close()