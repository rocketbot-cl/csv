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
import xlwings as xw
import openpyxl
import numpy as np
import time
import csv

"""
    Obtengo el modulo que fueron invocados
"""
def csv_read(path, encoding):
    import csv
    delimiter = GetParams("delimiter")
    csv_result = []
    if not delimiter:
        delimiter = ","
    with open(path, "r", encoding=encoding, ) as csv_file:
        data = csv_file.read()
        csv_file.close()
    if (data.startswith(("'","\""))):
        with open(path, "w", encoding=encoding, ) as csv_file:
            csv_file.write(data.replace("\"", ""))
            csv_file.close()
        time.sleep(2)
    
    with open(path, "r", encoding=encoding, ) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)
        for row in csv_reader:
            csv_result.append(row)
    return csv_result

module = GetParams("module")

if module == "read":
    path = GetParams("path")
    result = GetParams("result")
    delimiter = GetParams("delimiter")
    encoding = GetParams("encoding")

    if not delimiter:
        delimiter = ","
          
    if delimiter == "\\t":
        delimiter = "\t"

    if not encoding:
        encoding = "utf-8"
    try:
        
        csv_result = csv_read(path, encoding)
                
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
            print("Data is tuple")
            data = [list(da) for da in data]
        elif type(data[0]) is not list:
            print("Data is not list")
            data = [data]

        with open(path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                print(row)
                csv_writer.writerow(row)
    except Exception as e:
        print("\x1B[" + "31;40m" + str(e) + "\x1B[" + "0m")
        PrintException()
        raise e

if module == "csvToxlsx":
    path = GetParams("path")
    delimiter = GetParams("delimiter")
    encoding = GetParams("encoding")
    path_xlsx = GetParams("path_xlsx")

    if not delimiter:
        delimiter = ","
          
    if delimiter == "\\t":
        delimiter = "\t"

    if not encoding:
        encoding = "utf-8"
    try:
        try:
            app = xw.App(visible=False)
            book = xw.Book()
            csv_result = csv_read(path, encoding)
            book.sheets[0]["A1"].value = csv_result
            book.save(path_xlsx)
            book.close()
            app.quit()
        except:
            PrintException()
            app = openpyxl.Workbook()
            sheet = app.active
            csv_result = csv_read(path, encoding)
            for row in csv_result:
                sheet.append(row)
            app.save(path_xlsx)
            app.close()

    except Exception as e:
        print("\x1B[" + "31;40m" + str(e) + "\x1B[" + "0m")
        PrintException()
        raise e