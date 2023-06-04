#Solicitaremos los datos de la persona.

nombre = (input("Introduce tu nombre: "))
if nombre == "":
  print  ("Error. No introduciste tu nombre")
  quit()
apellido1 = (input("Introduce tu apellido paterno: "))
if apellido1 == "":
  print  ("Error, No introduciste tu apellido paterno.")
  quit()
apellido2 = (input("Introduce tu apellido materno: "))
if apellido2 == "":
  print  ("Error, No introduciste tu apellido materno.")
  quit()
edad = int(input("Introduce tu edad: "))
if edad<0 or edad>150:
  print ("Error, introduce tú edad correcta.")
  quit()
peso = float(input("Introduce tu peso en kilogramos: "))
if peso<0 or peso>370:
  print ("Error, introduce tú peso correcto en kilogramos.")
  quit()
estatura = float(input("Introduce tu estatura en metros: "))
if estatura<0 or estatura>3:
  print ("Error, introduce tú estatura correcta en metros.")
  quit()

#Se realiza el cálculo del IMC y se imprime el resultado.
print ("\nResultados:\n")
print ("Nombre: ", nombre .capitalize(), apellido1 .capitalize(), apellido2 .capitalize())
print ("Edad:", edad, "años.")
print ("Peso:", peso, "kg.")
print ("Estatura:", estatura, "m.")
print (f"Tu IMC es:{peso / estatura ** 2: .2f}")
