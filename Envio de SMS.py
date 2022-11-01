#!/usr/bin/env python
# coding: utf-8

# #### 1. Vamos criar um login no Twilio
# 
# https://www.twilio.com/docs/libraries/python

# #### 2. Depois do Login, vamos pegar 3 informações:
# 
# - ID da Conta
# - Token
# - Número de Envio

# #### 3. Agora vamos validar um número porque no Twilio, enviar SMS para um número válido é de graça

# #### 4. Agora podemos fazer o nosso código de acordo com as orientações do Twilio

# In[1]:


from twilio.rest import Client

account_sid = 'AC30173e6f2f658497a58ee801be39f1c2'
token = '42a9b63b7d5c12fb75b563dc741923ef'

client = Client(account_sid, token)

remetente = '+19894558959'
destino = '+551199999-9999'


message = client.messages.create(
    to=destino, 
    from_=remetente,
    body="Teste de envio de mensagem pelo Python!")

print(message.sid)

