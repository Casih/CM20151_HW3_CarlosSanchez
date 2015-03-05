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

formas=[1,2]
#generalizando a cualquier numero de escalones
#x = input("Para cuantos escalos quieres saber cuantas formas de subir hay? ")
#print ("Escogiste " + str(x) + " escalones")
#print (str(escalera(x)) +" forma(s) de subir " + str(x) + " escalones")

print (str(escalera(13)) + " formas de escalar una escalera de 13 escalones y " + str(escalera(15)) + " formas de escalar una escalera de 15 escalones")

A = [4,4,5,5,1]
B = [3,2,4,3,1]

def escaleras(A,B):

	err_msg1 = "El rango de A no está entre 1 y 10000"
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
