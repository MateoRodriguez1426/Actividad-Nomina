import re
print("Cordial saludo empleado")

document = input("Digite su numero de identificacion \n")


if document.isdigit() == True and len(document) == 10:
    print("Se ha registrado correctamente el Numero de Documento \n")
else:
    while document.isdigit() != True or len(document) < 10 or len(document) > 10:
        print("Ha digitado incorrectamente el Numero de Documento, Repita el  proceso \n (Recuerde que el numero de documento debe contener 10 digitos numericos sin puntos ni comas)\n")
        document = input("Digite su numero de identificacion \n")
        if document.isdigit() == True and len(document) == 10:
            print("Se ha registrado correctamente el Numero de Documento \n")


Name = str(input("Digite su primer nombre \n"))
vef = re.findall(r'[a-zA-Z]{2,20}', Name)
if vef:
    print("Se ha registrado correctamente su nombre \n")
else:
    while not vef:
        print("Ha digitado de manera incorrecta su Nombre (recuerde digitarlo sin caracteres especiales ni espacios)\n")
        Name = str(input("Digite su primer nombre\n"))
        vef = re.findall(r'[a-zA-Z]{2,20}', Name)
        if vef:
            print("Se ha registrado correctamente su nombre \n")

sName = str(input("Digite su segundo nombre (Si no tiene digite NA)\n"))
vef1 = re.findall(r'[a-zA-Z]{2,20}', sName)

if vef1:
    print("Se ha registrado correctamente su nombre \n")
else:
    while not vef1:
        print("Ha digitado de manera incorrecta su Nombre (recuerde digitarlo sin caracteres especiales ni espacios)\n")
        Name = str(input("Digite su segundo nombre\n"))
        vef1 = re.findall(r'[a-zA-Z]{2,20}', sName)
        if vef1:
            print("Se ha registrado correctamente su nombre \n")


lName = str(input("Digite sus Apellidos completos \n"))

vef2 = re.findall(r'[a-zA-Z]{2,40}\s', lName)
if vef2:
    print("Se han registrado correctamente sus apellidos \n")
else:
    while not vef2:
        print("Ha digitado de manera incorrecta los apellidos \n")
        lName = str(input("Digite sus Apellidos completos \n"))
        vef2 = re.findall(r'[a-zA-Z]{2,40}\s', lName)
        if vef2:
            print("Se han registrado correctamente sus apellidos\n")


wage = str(input("Digite su salario base \n"))

vef3 = re.findall('^\d[0-9]{6,8}',wage)
if vef3:
    print("Se ha registrado correctamente su salario \n")
else:
    while not vef3:
        print("Ha digitado de manera incorrecta el salario base (puede digitar 7 u 8 digitos, sin puntos ni comas.)\n")
        wage  = str(input("Digite su salario base \n"))
        vef3 = re.findall('^\d[0-9]{6,8}',wage)
        if vef3:
            print("Se ha registrado correctamente su salario \n")

workedDays = int(input("Digite el numero de dias laborados\n"))

if workedDays >= 10 or workedDays <= 31:
    workedDaysT = str(workedDays)
    vef4 = re.findall('^\d[0-9]{2}', workedDaysT)
    if vef4:
        print("Se han registrado correctamente sus Dias Trabajados \n")
    else:
        while workedDays < 10 or workedDays > 31:
            print("Debe registrar un numero entre 10 a 31, de lo contrario sera tomado como invalido\n")
            workedDays = int(input("Digite el numero de dias laborados\n"))
            workedDaysT = str(workedDays)
            vef4 = re.findall('\d[0-9]{2}', workedDaysT)
            if vef4:
                print("Se han registrado correctamente sus Dias Trabajados\n")

else:
    workedDaysT = str(workedDays)
    while workedDaysT.isdigit() == False:
        print("Debe registrar un numero entre 10 a 31, de lo contrario sera tomado como invalido\n")
        workedDays = int(input("Digite el numero de dias laborados\n"))
        workedDaysT = str(workedDays)
        vef4 = re.findall('^\d[0-9]{2}', workedDaysT)
        if vef4:
            print("Se han registrado correctamente sus Dias Trabajados\n")



'''






transporte = 0
if (SalarioBase <= 2000000):
    transporte = 117100

SalarioNeto = int((SalarioBase/30)*DT)
pension = int((SalarioNeto*0.04))
salud = int((SalarioNeto*0.04))
Nomina = int(SalarioNeto-(pension+salud))
transporte = int(transporte/30)*DT
Nomina = int(Nomina+transporte)


YN = input("sun datos son " + Nombre + documento + " Confirme escribiendo un YES de lo contrario escriba NO \n")

if (YN == "YES"):
    print("Su descuento por pension es:", pension)
    print("Su descuento por salud es:", salud)
    print("Su subsidio por transorte es de",transporte)
    print("Su salario neto por trabajar", DT, "dias, es de ", Nomina)
while (YN !="YES"):
    YN = input("sun datos son " + Nombre + documento + "Confirme escribiendo un YES de lo contrario escriba NO \n")
'''