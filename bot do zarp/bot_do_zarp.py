import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

workbook = openpyxl.load_workbook('contatos.xlsx')
pagina_contatos = workbook['Sheet1']

for linha in pagina_contatos.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    
    mensagem = f"Olá {nome}, gostariamos de te convidar para participar da próxima edição do OZ Valley Networking. Veja como se inscrever e mais informações https://p2.trrsf.com/image/fget/cf/774/0/images.terra.com/2023/02/18/919177108-brasileirao-a.jpg"
    
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(15)
        pyautogui.hotkey('enter')
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}{os.linesep}')
    