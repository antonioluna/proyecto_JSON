#-*- coding: utf-8 -*-

import json

#1. Lista de distritos
#2. Lista de instituciones por distritos
#3. Departamento gestor de la institución
#4. Cantidad de instituciones privadas / públicas por distrito solicitado
#5. Información sobre una institución en concreto

##########################################################
#                                                        #
#                Abriendo fichero json                   #
#                                                        #
##########################################################


with open("./DATA/educacion.json", "r") as educacion:
    educacionr = json.load(educacion)