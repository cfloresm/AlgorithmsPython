### Developed by René Mariano Sanabria
### Modulo menu.py
#Se importan los modulos y bibliotecas a utilizar
import sys
from ReadFile import readFileNumbers
from QuickSort import quickSort
from MergeSort import mergeSort
from FiboIte import fibIte
from FiboRec import fibRec
from FiboMatriz import *
from FiboTramp import fibTramp
from InsertionSort import insertSort
##############################################################################

#Se declara la funcion options la cual nos muestra el menu principal
def options():
	#Ciclo while para desplegar el menu hasta que se precione la tecla 0
	count = 1
	while (count != 0):

		#Menu de opciones
		print "\n"
		print "Que algoritmo quieres implementar ?"
		print "0.- Salir del Menu"
		print "1.- MergeSort"
		print "2.- QuickSort"
		print "3.- Insertion Sort"
		print "4.- Fibonacci Iterativo"
		print "5.- Fibonacci Recursivo"
		print "6.- Fibonacci Tramposo"
		print "7.- Fibonacci con Matrices"
		print "\n"
		
		#Se lee el entero para saber que opcion se va a ejecutar
		n = int(sys.stdin.readline())
		
		#Validacion, que el numero tecleado le corresponda una opcion	
		if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7:
			
			#Funcionalidad del menu, se utiliza la sentencia de control if para ejecutar el algoritmo seleccionado en el menu de opciones
			if n == 0:
				count = n
			elif n == 1: 
				print "******************Merge Sort*********************\n"
		     		print mergeSort( readFileNumbers() )
				print "***************************************************************************************"
			elif n == 2:
				print "******************Quick Sort*********************\n"
				print quickSort( readFileNumbers() )
				print "***************************************************************************************"
			elif n == 3:
				print "******************Insertion Sort*********************\n"
		     		print insertSort( readFileNumbers() )
				print "***************************************************************************************"
			elif n == 4:
				print "******************Fibonacci Iterativo*********************\n"
				print "\nEl fibonacci de que numero quieres obtener"
		  		number = int(sys.stdin.readline())
				print "El fibonacci en la posicion "+ str(number) + " es: " + str(fibIte(number)) +"\n\n"
				for i in range (0, number+1):
					print ("Fibonacci iterativo en la posicion: "+str(i)+"--> "+str(fibIte(i)))
				print "*******************************************************************"	
			elif n == 5:
				print "******************Fibonacci Recursivo*********************\n"
				print "\nEl fibonacci de que numero quieres obtener"
		  		number = int(sys.stdin.readline())
				print "El fibonacci en la posicion "+ str(number) + " es: " + str(fibRec(number)) +"\n\n"
				for i in range (0, number+1):
					print ("Fibonacci recursivo en la posicion: "+str(i)+"--> "+str(fibRec(i)))
				print "*******************************************************************"	
			elif n == 6:
				print "******************Fibonacci Trampozo*********************\n"
				print "\nEl fibonacci de que numero quieres obtener"
		  		number = int(sys.stdin.readline())
				print "El fibonacci en la posicion "+ str(number) + " es: " + str(fibTramp(number)) +"\n\n"
				for i in range (0, number+1):
					print ("Fibonacci iterativo en la posicion: "+str(i)+"--> "+str(fibTramp(i)))
				print "*******************************************************************"	
			elif n == 7:
				print "******************Fibonacci Matriz*********************\n"
		  		print "\nEl fibonacci de que numero quieres obtener"
		  		number = int(sys.stdin.readline())
		  		print "El fibonacci en la posicion "+ str(number) + " es: " + str(fibMat(number)) +"\n\n"
				for i in range(0, number+1):
					print ("Fibonacci con matrices: "+str(i)+"--> "+str(fibMat(i)))
				print "*******************************************************************"
		else:
			print "********* Has tecleado un numero al cual no le corresponde ninguna opcion ******************"				
	print "Bye"
############################################################### Fin de este modulo #########################################################################
