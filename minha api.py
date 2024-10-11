#!/usr/bin/env python
# coding: utf-8

# In[44]:


import requests
from flask import Flask
import pandas as pd


# In[55]:


link = "https://7b541ab4-7c21-4944-9b7d-88a23906e6db-00-2d4m06mnlxtw7.picard.replit.dev/vendas/produtos/Pulseira Xadrez"
requisicao = requests.get(link)
print(requisicao.json())


# In[48]:


app = Flask(__name__)
tabela = pd.read_excel('Vendas - Dez.xlsx')

@app.route("/")
def faturamento():
    fat = float(tabela['Valor Final'].sum())
    return {'Faturamento':fat}

@app.route("/vendas/produtos")
def vendas_produtos():
    vendas_cada_pro = tabela[['Produto','Valor Final']].groupby('Produto').sum()
    dic_vendas_cada_pro = vendas_cada_pro.to_dict()
    return dic_vendas_cada_pro

@app.route("/vendas/produtos/<produto>")
def fat_produtos(produto):
    vendas_cada_pro = tabela[['Produto','Valor Final']].groupby('Produto').sum()
    if produto in vendas_cada_pro.index:
        tabela_produto = vendas_cada_pro.loc[produto]
        dic_vendas_prod = tabela_produto.to_dict()
        return dic_vendas_prod
    else:
        return {produto: 'Inexistente'}
                        


app.run()


# In[ ]:




