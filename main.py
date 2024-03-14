bandas=[]

opcion=100
while(opcion != 5):
    print("***FESTIVAL ALTAVOZ***")
    print("**********************")
    print("1.Resgistrar Banda")
    print("2.Ver cartel del festival")
    print("3.Buscar banda")
    print("4.Modificar banda")
    print("5.Finalizar")


    opcion=int(input("Digita una opcion: "))

    if opcion == 1:
        banda={}
        #se llena el objeto
        banda["id"]=int(input("Digite el id: "))
        banda["nombre"]=input("Nombre")
        banda["genero"]=input("Genero")
        print(banda)

        #como agrego un diccionrio a una lista 
        bandas.append(banda)
        print(bandas)
    elif opcion == 2:
        #Recorriendo una lista pata imprimir sus elementos
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")
    elif opcion == 3:
        #Buscando un elemento dentro de una lista
        bandaBuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar  ["nombre"] == bandaBuscada:
                print("Lo encontro")
            else:
                print("No lo encontro")
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else: 
        print("Opcion invalida")
