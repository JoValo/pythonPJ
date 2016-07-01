#!/usr/bin/python
import mysql.connector as mariadb
import os

 
 
mariadb_connection = mariadb.connect(user='root', password='', database='conexion')
cursor = mariadb_connection.cursor()
os.system('cls')
ciclo = 1
opcion = input("CONEXION PYTHON & MARIA DB \n [Presione 1 para continuar...]")
while ciclo == 1:
     
    if opcion == 1 :
        os.system('cls')
        opcion_consola = input ("[1]INSERTAR   [2]ACTUALIZAR   [3]BORRAR   [4]CONSULTAR   [5]MOSTRAR TABLAS\n>:")
        if opcion_consola == 1:
            os.system('cls')
            print "########INSERTAR DATOS#############"
            var1 = raw_input("\nIngresa nombre:")
            var2 = raw_input("\nIngresa domicilio:")
            try:
                cursor.execute("INSERT INTO SOCIOS (NOMBRE,DOMICILIO) VALUES (%s,%s)", (var1,var2))
                print "\tDATO INSERTADO CORRECTAMENTE"
                ciclo =input("[1]SEGUIR\n[2]SALIR\n")
            except mariadb.Error as error:
                print("Error: {}".format(error))
            mariadb_connection.commit() 
        elif opcion_consola == 2:
            os.system('cls')
            print "########ACTUALIZAR DATOS#############"
            var4 = input("\nIngresa numero de curso:")
            var1 = raw_input("\nIngresa deporte:")
            var2 = raw_input("\nIngresa dia:")
            var3 = input("\nIngresa numero de profesor:")
            try:
                cursor.execute( "UPDATE CURSOS SET deporte=%s,dia=%s,num_profesor_f=%s WHERE num_cursos = %s",(var1,var2,var3,var4))
                print "\tDATO ACTUALIZADO CORRECTAMENTE"
                ciclo =input("[1]SEGUIR\n[2]SALIR\n")
            except mariadb.Error as error:
                print("Error: {}".format(error))
            mariadb_connection.commit() 
        elif opcion_consola == 3:
            os.system('cls')
            print "########BORRAR DATOS#############"
            var1 = input("\nIngresa numero de socio :")
            try:
                cursor.execute("DELETE FROM SOCIOS WHERE num_socios = %s", (var1,))
                print "\t\n\nDATO ELIMINADO CORRECTAMENTE"
                ciclo =input("[1]SEGUIR\n[2]SALIR\n")
            except mariadb.Error as error:
                print("Error: {}".format(error))
            mariadb_connection.commit() 
        elif opcion_consola == 4:
            os.system('cls')
            print "########CONSULTAR DATOS#############"
            cursor.execute("SELECT * FROM vista_1 ")
            for nombre, deporte, dia in cursor:
                print("NOMBRE: {}, DEPORTE: {}, DIA: {}").format(nombre,deporte,dia)
            print "\n\n\tCONSULTA DE DATOS REALIZADA  CORRECTAMENTE"
            ciclo =input("[1]SEGUIR\n[2]SALIR\n")
            mariadb_connection.commit() 
        elif opcion_consola == 5:
            os.system('cls')
            print "########CONSULTAR DATOS#############"
            cursor.execute("show tables")
            for tablas in cursor:
                print("TABLAS: {}").format(tablas)
            print "\n\n\tCONSULTA REALIZADA  CORRECTAMENTE"
            ciclo =input("[1]SEGUIR\n[2]SALIR\n")
            mariadb_connection.commit() 
mariadb_connection.close()