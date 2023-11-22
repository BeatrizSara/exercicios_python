""" 
Catetos e Hipotenusa 
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot

cateto_oposto = float(input("Informe o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")