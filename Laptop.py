import DataBase.Conocimientodb as DB

#La base de datos de Conocimiento
#Base de datos:
ConocimientoDB = DB.generarBD()
Aceptados = ConocimientoDB.copy()
Rechazados = []
alreadyAsked = set()

# METODOS
def actualizarTablasSi(aceptados,attributoAceptado,i):
    global Rechazados
    aux = []
    for row in aceptados:
        if row[i] == attributoAceptado:
            aux.append(row)
        else:
            Rechazados.append(row)
    return aux

def actualizarTablasNo(aceptados,attributoRechazado,i):
    global Rechazados
    aux = []
    for row in aceptados:
        if row[i] == attributoRechazado:
            Rechazados.append(row)
        else:
            aux.append(row)
    return aux

#Atributos de comienzo
ROW=0
COLUMN=1
FOUND = False
MODELO = COLUMN-1 #Por si se agrega una indice numerico al csv para ordernarlos

#MAIN LOGIC
#Corre mientras que la tabla de aceptados tenga datos
while not FOUND:

    #Si la tabla ya no tiene datos, no se pudo encontrar
    if len(Aceptados) == 0:
        print("\nERROR: No se pudo encontrar lo que busca")
        break

    #Si llega al final, Quiere decir que se encontro
    if COLUMN == len(Aceptados[0]):
        FOUND = True
        break

    #Para preguntar sobre los atributos SSS
    row = Aceptados[ROW]
    ROW+=1
    attributo = row[COLUMN] 

    #Si ya pregunto cierto atributo, lo brinca
    if(attributo in alreadyAsked):
        #print(f"DEBUG: Already asked {attributo}")
        continue

    #La pregunta
    respuesta = input(f"Su laptop tiene/es? (si/no): {attributo}\t")

    #Si la respuesta es si, cambia de columna
    #Pone los laptops aceptados en una tabla
    #Rechaza todos los demas
    #y pregunta desde el primer renglon
    if respuesta.lower() == "si":
        Aceptados = actualizarTablasSi(Aceptados,attributo,COLUMN)
        COLUMN+=1
        ROW=0
    #Alreves de si la respuesta es si
    #Pero para no preguntar lo mismo, lo mete a un set
    elif respuesta.lower() == "no":
        Aceptados = actualizarTablasNo(Aceptados,attributo,COLUMN)
        alreadyAsked.add(attributo)
        ROW=0
    else:
        #si no pregunta ni si o no, pregunta lo mismo
        ROW -=1
    continue

#Si se encontro uno (o varios) los imprime
if FOUND:
    print("\nEl modelo del cual habla es:")
    [print(row[MODELO]) for row in Aceptados]




