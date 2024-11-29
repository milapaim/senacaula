import tk
import requests
from tkinter import *

def pegar_cotacoes():
    requesicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requesicao.json()
    
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar:{cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''


janela = Tk()
janela.title("cotação atual de Moedas")
texto = Label (janela, text= "clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button ( janela,text= "buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela,text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)
janela.mainloop()
