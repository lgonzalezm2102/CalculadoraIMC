while True:
    try:
        nombre=input("Ingresa tu nombre(s): ");
        if nombre == "":
            print("No ingresaste tu nombre");
            continue;
        break;
    except ValueError:
        print("Ingresa un valor correcto");
        continue;
while True:
    try:
        apellidoPaterno=input("Ingresa tu apellido Paterno: ");
        if apellidoPaterno == "":
            print("No ingresaste tu apellido Paterno");
            continue;
        break;
    except ValueError:
        print("Ingresa un valor correcto");
        continue;
while True:
    try:
        apellidoMaterno=input("Ingresa tu apellido materno: ");
        if apellidoMaterno == "":
            print("No ingresaste tu apellido Materno");
            continue;
        break;
    except ValueError:
        print("Ingresa un valor correcto");
        continue;
while True:
    try:
        edad=int(input("Ingresa tu edad: "));
        if edad <0 or edad >100:
            print("Edad no valida");
            continue;
        break;
    except ValueError:
        print("Ingresa un valor numerico");
        continue;
while True:
    try:
        peso=float(input("Ingresa tu peso en Kg: "));
        if peso <0 or peso >300:
            print("Peso no valido");
            continue;
        break;
    except ValueError:
        print("Ingresa un peso valido");
        continue;
while True:
    try:
        estatura=float(input("Ingresa tu estatura en m: "));
        if estatura <0 or estatura >2.72:
            print("Estatura no valida");
            continue;
        break;
    except ValueError:
        print("Ingresa una estatura valida");
        continue;
imc=peso/(estatura**2);

print("\n***********************************" "\nQue tal " + nombre + " " + apellidoPaterno + " " + apellidoMaterno + "\nTu peso es de: " +str(peso) +"Kg" + "\nTu estatura es de: " +str(estatura) + " Mts" +"\nTu Edad : " + str(edad) + " Años"+ "\nesto da un IMC de: " + str(imc));
