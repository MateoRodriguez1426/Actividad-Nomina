import re

wage = str(input("Digite su salario base \n"))

vef3 = re.findall('^\d{6,8}',wage)

start = wage.startswith("0")

if start == True:
    print("Error 404")