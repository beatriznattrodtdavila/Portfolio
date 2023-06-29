import pyautogui
import time
import pandas as pd
import webbrowser

link = "https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema"


# abrir o navegador
chrome_path = '/usr/bin/google-chrome-stable %s'
webbrowser.get(chrome_path).open(link)

time.sleep(5)



# fazer login
#x_login, y_login = pyautogui.position()
x_login = 433
y_login = 408
pyautogui.click(x_login, y_login)
pyautogui.write("meu_login")

#x_senha, y_senha = pyautogui.position()
x_senha = 434
y_senha = 489
pyautogui.click(x_senha, y_senha)
pyautogui.write("minha_senha")


#x_acessar, y_acessar = pyautogui.position()
x_acessar = 450
y_acessar = 559
pyautogui.click(x_acessar, y_acessar)
time.sleep(3)




# baixar a base de dados
#x_selecionar_dados, y_selecionar_dados = pyautogui.position()
x_selecionar_dados = 482
y_selecionar_dados = 380
pyautogui.click(x_selecionar_dados, y_selecionar_dados, button = "right")
time.sleep(3)

x_download, y_download = pyautogui.position()
x_download = 589
y_download = 792
pyautogui.click(x_download, y_download)
time.sleep(5)



# trabalhando com a base de dados
tabela = pd.read_csv("/home/ubuntu/Downloads/Compras.csv", sep = ";")

total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade



# enviar relatorio por e-mail
pyautogui.hotkey("ctrl", "t")
pyautogui.write("gmail.com")
pyautogui.press("enter")
time.sleep(4)

#x_escrever, y_escrever = pyautogui.position()
x_escrever = 66
y_escrever = 236
pyautogui.click(x_escrever, y_escrever)
time.sleep(2)

pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
time.sleep(3)

pyautogui.write("Relatorio de Compras")
pyautogui.press("tab")


time.sleep(3)


import pyperclip
texto = f"""
Prezados,
Segue o resumo das compras:

Gasto Total: R${total_gasto:,.2f}
Quantidade: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Att.
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")

