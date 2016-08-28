import numpy as np
import random
from time import time

#tiempo_ejecucion = 0

def Producto2Mayores(a,n):	
	if(a[0]>a[1]):		#indices
		mayor1=a[0]
		mayor2=a[1]	
	else:
		mayor1=a[1]
		mayor2=a[0]
	i=2
	while(i<=n):
		if (a[i]>mayor1):
			mayor2 = mayor1
			mayor1 = a[i]
		elif(a[i] > mayor2):
			mayor2 = a[i]
		i = i + 1
	return mayor1 * mayor2

def OrdenamientoIntercambio(a,n):	
	#a = [4,5,3,1,10]
	#n=4;	
	for i in xrange(0,n):
		for j in xrange(1,n+1):
			if(a[j]<=a[i]):
				temporal = a[i]
				a[i]=a[j]
				a[j]=temporal	
	return a

def MaximoComunDivisor(m,n):	
	a=max(n,m)
	b=min(n,m)
	residuo = 1;
	while(residuo >0):		
		residuo =  a % b
		a = b
		b = residuo
	MaximoComunDivisor = a
	return MaximoComunDivisor

def BurbujaSimple(a,n):
	for i in xrange (1, n):
		for j in xrange(0, n):  #rango
			if (a[j] > a[j+1]):
				temp = a[j]
				a[j] = a[j+1]
				a[j+1] = temp
	return a

def BurbujaMejorada(a,n):
	for i in xrange(1,n+1):		#rango
		for j in xrange(0,i):
			if (a[i] < a[j]):
				temp = a[j]
				a[j] = a[i]
				a[i] = temp
	return a

def CreaMatriz(M):
	Matriz = [ ]
	for i in range(n):
		Matriz.append(random.randint(0,10000))	
	return Matriz

def TiempoTxt(i,tiempo):	 
	cadena = ""
	for y in xrange(1,i+1):		
		cadena = str(y) + '\t' + str(tiempo) + '\n'
	archivo = open('valores.txt','a')
	archivo.write(cadena)
	archivo.close()    
	return cadena

n = int(raw_input("Ingrese la dimension de la matriz: \n"))
for i in xrange(1,51):
	print 'Ciclo #', i 
	Ma = CreaMatriz(n)
	print Ma
	
	tiempo_inicial = time() 	
	#Resultado = Producto2Mayores(Ma,n-1)
	#Resultado = OrdenamientoIntercambio(Ma,n-1)
	# verificar Resultado = MaximoComunDivisor(m,n);
	#Resultado = BurbujaSimple(Ma,n-1)
	Resultado = BurbujaMejorada(Ma,n-1)	
	tiempo_final = time()  
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	print Resultado
	print 'El tiempo de ejecucion fue (seg):',tiempo_ejecucion #En segundos	
	
	#Guardo los resultados en un txt:::::::::::::::::::::	
	TiempoTxt(i,tiempo_ejecucion)

#for i in xrange(1,11):
#	print i 