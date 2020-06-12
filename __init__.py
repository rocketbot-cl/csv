# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import csv

"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "read":
    path = GetParams("path")
    result = GetParams("result")
    delimiter = GetParams("delimiter")

    if not delimiter:
        delimiter = ","
    try:
        csv_result = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            for row in csv_reader:
                csv_result.append(row)

        if result:
            SetVar(result, csv_result)
    except Exception as e:
        print("\x1B[" + "31;40m" + str(e) + "\x1B[" + "0m")
        PrintException()
        raise e

if module == "export":
    path = GetParams("path")
    data = GetParams("data")
    delimiter = GetParams("delimiter")

    try:
        if not delimiter:
            delimiter = ","
        data = eval(data)

        if type(data[0]) is tuple:
            data = [list(da) for da in data]
        elif type(data[0]) is not list:
            data = [data]

        with open(path, mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                csv_writer.writerow(row)
    except Exception as e:
        print("\x1B[" + "31;40m" + str(e) + "\x1B[" + "0m")
        PrintException()
        raise e

