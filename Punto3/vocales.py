# -*- coding: utf-8 -*-
"""
Created on Sun Mar 1 07:19:33 2015
@author: Carlos Sanchez
"""
Vocales = 'aeiouy'
lista = []

m = input("Cuantas Lineas?")
f = open('Sainte-Beuve.txt','r')

for i in range(m):
	n = f.readline()
	n = n.lower()
	n = n.replace("á","a")
	n = n.replace("à","a")
	n = n.replace("ä","a")
	n = n.replace("â","a")
	n = n.replace("ë","e")
	n = n.replace("ë","e")
	n = n.replace("è","e")
	n = n.replace("é","e")
	n = n.replace("î","i")
	n = n.replace("ï","i")
	n = n.replace("í","i")
	n = n.replace("ì","i")
	n = n.replace("ô","o")
	n = n.replace("ö","o")
	n = n.replace("ò","o")
	n = n.replace("ó","o")
	n = n.replace("û","u")
	n = n.replace("ü","u")
	n = n.replace("ù","u")
	n = n.replace("ú","u")
	n = n.replace("ÿ","y")
	p = 0
	for i in n:
		if i in Vocales:
	   		p += 1
	lista.append(p)
 	
print "Los siguientes son los números de vocales por línea, desde la primera, hasta el número que usted indico respectivamente " + str(lista)   

f.close()

