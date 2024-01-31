#Encontrar nombres en el dataset

###Como creo una carpeta desde colab? 
###Como crear subcarpetas?
###Buscando los codigos de estado, como hago para crear una regla de busqueda pero que sea excluyente? es decir, que no lo imprima pero sin embargo lo tenga en cuenta


import requests
import re
import os

r = requests.get('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-Regular-Expressions/data.txt')
texto = r.text
print(texto)

##ENCONTRAR EMAILS##

def encontrar_emails(texto):
  regla_de_busqueda = r"([a-zA-Z0-9]+@+[a-z]+.com)"
  return  re.findall(regla_de_busqueda, texto)

#print(encontrar_emails(texto))

##ENCONTRAR NOMBRES##

def encontrar_nombres(texto):
  regla_de_busqueda = r"([A-Z][a-z]+\s[A-Z][a-z]+\n)"
  return  re.findall(regla_de_busqueda, texto)

#print(encontrar_nombres(texto))

##ENCONTRAR NUMEROS##

def encontrar_numeros(texto):
  regla_de_busqueda = r"([0-9]+-[0-9]+-[0-9]+\n)"
  return  re.findall(regla_de_busqueda, texto)

#print(encontrar_numeros(texto))

##ENCONTRAR CODIGO DE ESTADO##

def encontrar_codigo_de_estado(texto):
  regla_de_busqueda = r"([0-9]\d+\s[A-Z])"
  return  re.findall(regla_de_busqueda, texto)

#print(encontrar_codigo_de_estado(texto))
