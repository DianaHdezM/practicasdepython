#Solicitaremos los datos de la persona.

nombre = (input("Ingresa tu nombre: "))
if nombre == "":
  print  ("Error. No ingresaste tu nombre")
  quit()
apellido1 = (input("Ingresa tu apellido paterno: "))
if apellido1 == "":
  print  ("Error, No ingresaste tu apellido paterno.")
  quit()
apellido2 = (input("Ingresa tu apellido materno: "))
if apellido2 == "":
  print  ("Error, No ingresaste tu apellido materno.")
  quit()
edad = int(input("Ingresa tu edad: "))
if edad<0 or edad>150:
  print ("Error, ingresa tú edad correcta.")
  quit()
peso = float(input("Ingresa tu peso en kilogramos: "))
if peso<0 or peso>370:
  print ("Error, ingresa tú peso correcto en kilogramos.")
  quit()
estatura = float(input("Ingresa tu estatura en metros: "))
if estatura<0 or estatura>3:
  print ("Error, ingresa tú estatura correcta en metros.")
  quit()

#Se realiza el cálculo del IMC y se imprime el resultado.
print ("\nResultados:\n")
print ("Nombre: ", nombre .capitalize(), apellido1 .capitalize(), apellido2 .capitalize())
print ("Edad:", edad, "años.")
print ("Peso:", peso, "kg.")
print ("Estatura:", estatura, "m.")
print (f"Tu IMC es:{peso / estatura ** 2: .2f}")
