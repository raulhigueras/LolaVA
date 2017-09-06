# -*- coding: utf-8 -*-
# Módulo que realiza operaciones matemáticas (suma, resta, multiplicación, división, raiz y potencia)

def get_numeros_from_frase(frase):
  frase = frase.split(" ")
  i = 0
  for p in frase:
    if p == "mas" or p == "menos" or p == "por" or p == "entre":
      return [int(frase[i-1]), int(frase[i+1])]
    if p == "elevado":
      return [int(frase[i-1]), int(frase[i+2])]
    if p == "raiz" or p == "raíz":
      return[int(frase[i+3]), int(frase[i+1])]
    i += 1

def sumar(frase):
  num = get_numeros_from_frase(frase)
  return "El resultado es: " + str(num[0] + num[1])

def restar(frase):
  num = get_numeros_from_frase(frase)
  return "El resultado es: " + str(num[0] - num[1])

def multiplicar(frase):
  num = get_numeros_from_frase(frase)
  return "El resultado es: " + str(num[0] * num[1])

def dividir(frase):
  num = get_numeros_from_frase(frase)
  return "El resultado es: " + str(num[0] / float(num[1]))

def potencia(frase):
  num = get_numeros_from_frase(frase)
  return "El resultado es: " + str(num[0] ** num[1])

def raiz(frase):
  num = get_numeros_from_frase(frase)
  return "El resultado es: " + str(num[0] ** (1/float(num[1])))