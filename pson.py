#-*- coding: utf-8 -*-

import json

#1. Lista de distritos
#2. Lista de instituciones por distritos
#3. Departamento gestor de la institución
#4. Cantidad de instituciones privadas / públicas por distrito solicitado
#5. Información sobre una institución en concreto


#Obtiene los codigos de los distritos
def recorrer(dato1, dato2):
    datos = {}
    for x in educacionr:
        datos[x[dato1]] = x[dato2]
    return datos


def instituciones(codigo):
    datos = {}
    for x in educacionr:
        if x[cod_dist] == codigo:
            datos[x[cod_est]] = x[nom_inst]
    return datos


def gestor(cod):
    datos = []
    gestor = []
    institucion = []
    for x in educacionr:
        if x[cod_est] == cod:
            gestor.extend([x[cod_dept], x[nom_dept]])
            institucion.extend([x[cod_inst], x[nom_inst]])
            datos.extend([gestor])
            datos.extend([institucion])
    return datos

##########################################################
#                                                        #
#                Abriendo fichero json                   #
#                                                        #
##########################################################


with open("./DATA/educacion.json", "r") as educacion:
    educacionr = json.load(educacion)


##########################################################
#                                                        #
#                 Valores fichero json                   #
#                                                        #
##########################################################


cod_dept = "codigo_departamento"
cod_dist = "codigo_distrito"
cod_est = "codigo_establecimiento"
cod_inst = "codigo_institucion"
cod_zona = "codigo_zona"
nom_barrio = "nombre_barrio_localidad"
nom_dept = "nombre_departamento"
nom_dist = "nombre_distrito"
nom_inst = "nombre_institucion"
nom_zona = "nombre_zona"
gestion = "sector_o_tipo_gestion"


##########################################################
#                                                        #
#                    Menú principal                      #
#                                                        #
##########################################################

print "\nBienvenido a mi proyecto de JSON"

while True:

    print "\n¿Que quieres hacer?\n\n1 Listar distritos\n2 Listar de \
instituciones de un distrito\n3 Ver el departamento gestor de una \
institución\n4 Ver la cantidad de instituciones privadas / públicas de un \
distrito\n5 Ver información detallada sobre una institución en concreto\n6 \
Salir"

    opcion = raw_input("\nElija opción: ")

    ##########################################################
    #                                                        #
    #            Impresión de lista de distritos             #
    #                                                        #
    ##########################################################

    if opcion == "1":
        distritos = recorrer(cod_dist, nom_dist)
        print "\nCód   ---       Nombre dst\n"
        for x in distritos:
            print x + "  ---  " + distritos[x]

    ##########################################################
    #                                                        #
    #           Impresión de lista de instituciones          #
    #                                                        #
    ##########################################################

    if opcion == "2":
        elec = raw_input("\nIntroduzca el código del distrito")
        insti = instituciones(elec)
        print "En el distrito %s se encuentran las siguientes instituciones:"\
        % (elec)
        print "\nCód      ---      Nombre dst\n"
        for x in insti:
            print x + "  ---  " + insti[x]

    if opcion == "3":
        cod = raw_input("\nIntroduzca el código de la institución: ")
        gest = gestor(cod)
        print "\nDepartamento: %sc - %s\nGestor: %s - %s"\
        % (str(gest[1][0]), str(gest[1][1]),
        str(gest[0][0]), str(gest[0][1]))

    ##########################################################
    #                                                        #
    #                Cantidad pública/privada                #
    #                                                        #
    ##########################################################

    if opcion == "3":
        None

    if opcion == "6":
        break