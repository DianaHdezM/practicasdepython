#Solicitaremos los datos de la persona.

nombre = (input("Introduce tu nombre: "))
apellido1 = (input("Introduce tu apellido paterno: "))
apellido2 = (input("Introduce tu apellido materno: "))
edad = int(input("Introduce tu edad: "))
if edad <150 and >=0

peso = float(input("Introduce tu peso en kilogramos: "))
estatura = float(input("Introduce tu estatura en metros: "))

#Se realiza el cálculo del IMC
print (f"Tu IMC es: {peso / estatura ** 2: .2f}")
