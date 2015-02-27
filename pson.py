#-*- coding: utf-8 -*-

import json

#1. Lista de distritos
#2. Lista de instituciones por distritos
#3. Departamento gestor de la institución
#4. Cantidad de instituciones privadas / públicas por distrito solicitado
#5. Información sobre una institución en concreto


def recorrer(dato1, dato2):
    #datos = {"1254": ["nom-dist", {"cod-inst": ["nom_inst", "cod_dept", "nom_dept", "gestion"]}]}
    datos = {}
    for x in educacionr:
        datos[x[dato1]] = [x[dato2]]
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

distritos = recorrer(cod_dist, nom_dist)
int_dist = dis_inf(distritos, cod_inst, nom_inst)

##########################################################
#                                                        #
#            Impresión de lista de distritos             #
#                                                        #
##########################################################


print "\nBienvenido a mi proyecto de JSON"

print "\n\n Cód  ---       Nombre dst\n"

for x in distritos:
    print x + "  ---  " + distritos[x]