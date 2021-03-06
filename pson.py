#-*- coding: utf-8 -*-

import json


#Obtiene los codigos de los distritos
def recorrer(dato1, dato2):
    datos = {}
    for x in educacionr:
        datos[x[dato1]] = x[dato2]
    return datos


#Obtiene las instituciones por distrito
def instituciones(codigo):
    datos = {}
    for x in educacionr:
        if x[cod_dist] == codigo:
            datos[x[cod_est]] = x[nom_inst]
    return datos


#Obtiene el gestor de una institucion en concreto
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


#Función que obtiene el tipo de gestión de las instituciones de un distrito
def tipo(codigo):
    datos = [""]
    publica = {}
    privada = {}
    concertada = {}
    for x in educacionr:
        datos[0] = x[nom_dist]
        if x[cod_dist] == codigo:
            if x[gestion] == "OFICIAL":
                publica[x[cod_est]] = x[nom_inst]
            if x[gestion] == "PRIVADA":
                privada[x[cod_est]] = x[nom_inst]
            if x[gestion] == "PRIV.SUBVENCIONADA":
                concertada[x[cod_est]] = x[nom_inst]
    datos.extend([publica])
    datos.extend([privada])
    datos.extend([concertada])
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
        elec = raw_input("\nIntroduzca el código del distrito: ")
        insti = instituciones(elec)
        print "En el distrito %s se encuentran las siguientes instituciones:"\
        % (elec)
        print "\nCód      ---      Nombre dst\n"
        for x in insti:
            print x + "  ---  " + insti[x]

    if opcion == "3":
        cod = raw_input("\nIntroduzca el código de la institución: ")
        gest = gestor(cod)
        print "\nInstitución: %s - %s\nGestor: %s - %s"\
        % (str(gest[1][0]), str(gest[1][1]),
        str(gest[0][0]), str(gest[0][1]))

    ##########################################################
    #                                                        #
    #                Cantidad pública/privada                #
    #                                                        #
    ##########################################################

    if opcion == "4":
        num = raw_input("\nIntroduzca el código del distrito: ")
        ppc = tipo(num)

        print "Distrito: %s --- %s:" % (num, ppc[0])

        print "\nInstituciones Oficiales: %d\n" % (len(ppc[1]))
        print "  Cod   ---   Nombre Ins."
        for ofi in ppc[1]:
            print ofi + " --- " + ppc[1][ofi]

        print "\nInstituciones Privadas: %d" % (len(ppc[2]))
        print "  Cod   ---   Nombre Ins."
        for pri in ppc[2]:
            print pri + " --- " + ppc[2][pri]

        print "\nInstituciones Concertadas: %d" % (len(ppc[3]))
        print "  Cod   ---   Nombre Ins."
        for con in ppc[3]:
            print con + " --- " + ppc[3][con]

    ##########################################################
    #                                                        #
    #          Información detallada de institución          #
    #                                                        #
    ##########################################################

    if opcion == "5":
        num = raw_input("\nIntroduzca el código de la institución: ")
        for institucion in educacionr:
            if institucion[cod_est] == num:
                print "\nCódigo de distrito: %s"\
                % (str(institucion[cod_dist]))
                print "Nombre de distrito: %s"\
                % (str(institucion[nom_dist]))
                print "Tipo de gestión: %s"\
                % (str(institucion[gestion]))
                print "Código de departamento gestor: %s"\
                % (str(institucion[cod_dept]))
                print "Nombre de departamento gestor: %s"\
                % (str(institucion[nom_dept]))
                print "Código de institucion gestora: %s"\
                % (str(institucion[cod_inst]))
                print "Nombre de institución: %s"\
                % (str(institucion[nom_inst]))
                print "Código de institución: %s"\
                % (str(institucion[cod_est]))
                print "Código de zona: %s"\
                % (str(institucion[cod_zona]))
                print "Zona: %s"\
                % (str(institucion[nom_zona]))
                print "Nombre del barrio: %s"\
                % (str(institucion[nom_barrio]))

    if opcion == "6":
        print "\n\nAdiós\n\n"
        break