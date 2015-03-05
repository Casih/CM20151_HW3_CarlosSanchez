# -*- coding: utf-8 -*-
"""
Created on Sun Mar 1 07:19:33 2015
@author: Carlos Sanchez
"""

def escalera(x):
	formas=[1,2]
 	if x == 1:
  		return formas[0]
 	elif x == 2:
  		return formas[1]
 	elif x == 0:
  		return 0
 	else: 
  		for i in range(x-2):
   			formas.append(formas[-1]+formas[-2])
  		return formas[-1]

#generalizando a cualquier numero de escalones
#x = input("Para cuantos escalos quieres saber cuantas formas de subir hay? ")
#print ("Escogiste " + str(x) + " escalones")
#print (str(escalera(x)) +" forma(s) de subir " + str(x) + " escalones")

print (str(escalera(13)) + " formas de escalar una escalera de 13 escalones y " + str(escalera(15)) + " formas de escalar una escalera de 15 escalones")


# A continuacion muestro 5 ejemplos ademas del puesto en el taller, de pares de vectores A y B que evidencian el funcionamiento del script.

A = [4,4,5,5,1]
B = [3,2,4,3,1]

#A = [5,6,7,8,9,1,2,3,4,5] 
#B = [1,2,3,4,4,3,2,1,2,3]

#A = [1000000,1,2,3]
#B = [1,2,3,4]

#A = [1,2]
#B = [21,5]

#A = []
#B = []

#A = [1,2,3]
#B = [1,2]

def escaleras(A,B):

	err_msg1 = "El rango de A y B no están entre 1 y 10000"
	err_msg2 = "Algun elemento de A se sale del rango de valores establecidos"
	err_msg3 = "Algun elemento de B se sale del rango de valores establecidos"
	err_msg4 = "Los arreglos ingresados no tienen la misma dimension"

	for i in range(len(A)):
		if A[i] < 1 or A[i] > len(A): 
			return err_msg2
	for i in range(len(A)):
		if B[i] < 1 or B[i] > 20:
			return err_msg3
	if len(A) > 10000 or len(A) < 1:
		return err_msg1
	elif len(B) != len(A):
		return err_msg4
	else:
		L = []
		L1 = []
		for i in range(len(A)):
			c = A[i] % (2*B[i])
			x = escalera(c)
			L.append(x)

	return L

print escaleras(A,B)
