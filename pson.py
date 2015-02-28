#-*- coding: utf-8 -*-

import json

#1. Lista de distritos
#2. Lista de instituciones por distritos
#3. Departamento gestor de la institución
#4. Cantidad de instituciones privadas / públicas por distrito solicitado
#5. Información sobre una institución en concreto


def recorrer(dato1, dato2, dato3, dato4, dato5, dato6, dato7):
    lista_o = []
    lista_t = []
    #datos = {"cod_dist": {"nom-dist": {"cod-inst": ["nom_inst", "cod_dept"
    #, "nom_dept", "gestion"]}}}
    datos = {}
    for x in educacionr:
        dic_t = {}
        lista_t = [x[dato1]]
        dic_t[x[dato3]] = [x[dato2], x[dato4], x[dato5], x[dato6], x[dato7]]
        lista_t.append(dic_t)
        lista_o.append(lista_t)
    for y in lista_o:
        for z in range(len(y)):
            datos[y[0]] = y[1]
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


distritos = recorrer(cod_dist, nom_dist, cod_inst, nom_inst, cod_dept,
    nom_dept, gestion)


##########################################################
#                                                        #
#            Impresión de lista de distritos             #
#                                                        #
##########################################################


print "\nBienvenido a mi proyecto de JSON"

print "\n\n Cód  ---       Nombre dst\n"

#for x in distritos:
    #print x + "  ---  " + distritos[x]