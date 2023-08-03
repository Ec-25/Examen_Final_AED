from module import *
from tools import *


def menu() -> int:
    msg = f"\n{'='*60}\n\t\t\tMENU\n{'='*60}\n\t0)- Salir.\n\t1)- Cargar Datos Nuevos.\n\t2)- Mostrar los Registros.\n\t3)- Buscar por Titulo.\n\t4)- Cuantos hay Por Tipo (Medio y Transporte).\n\t5)- Buscar Pago total por Nombre.\n\t6)- Guardar Aquellos mayores a $100.000\n\t7)- Mostrar los guardados.\n{'='*60}"
    print(msg)
    return getNumber("Opcion:\t", 7, 0)


def app() -> None:
    opc = -1
    registry = []

    while opc != 0:
        opc = menu()

        if opc == 1:
            # generar nuevos datos
            registry.clear()
            cant = getNumber("\nCuantos datos desea cargar?\t", min=0)
            for i in range(cant):
                # crear el paquete
                package = setPackage()
                # agregarlo de forma ordenada segun indice
                indx = getIndexMinMax(registry, package.nro_id)
                registry.insert(indx, package)

        elif opc == 2:
            # mostrar cada registro
            cnt = 0
            print()
            for i in range(len(registry)):
                cnt += 1
                print(registry[i].__str__())
            print(f"\n=== Se mostraron {cnt} registros ===\n")

        elif opc == 3:
            # buscar titulo
            tit = input("\nTitulo a buscar:\t")
            obj = searchTitle(registry, tit)
            if isinstance(obj, Paquete):
                print(f"\nEncontrado -> ID: {obj.nro_id}, CLIENTE: {obj.client}")
            else:
                print("\nNo se encontro ningun paquete con el titulo ", tit)

        elif opc == 4:
            # cuántos paquetes hay para combinación (medio y destino)
            pack = []
            # Medio de Transporte
            for _ in range(10):
                list = []
                # Destino Fina
                for _ in range(50):
                    list.append([0])
                pack.append(list)

            # Bucle de Conteo
            for reg in registry:
                ids = indexTranportDestin(reg)
                pack[ids[0]][ids[1]][0] += 1

            for IDsublist in range(len(pack)):
                # Primera lista(medio)
                sublist = pack[IDsublist]

                print()
                for IDelement in range(len(sublist)):
                    # Segunda lista(destino)
                    element = sublist[IDelement][0]

                    if element != 0:
                        print(f"El medio {IDsublist} con Destino a {IDelement} contiene {element} pasajeros.")

        elif opc == 5:
            # Pago total por nombre
            client = input("\nIngrese el nombre de la persona a buscar:\t")
            amount = paymentByClient(registry, client)
            if amount != 0:
                print(f"\nEl cliente {client} ha pagado en total {amount} pesos.")

            else:
                print(f"\nNo se encontro ningun cliente con nombre {client}")

        elif opc == 6:
            # guardar paquetes mayores a 100.000
            correspond = getPackagesByMinAmount(registry, 100000)
            if len(correspond) != 0:
                # guardar
                saveRegistry(correspond, "findedByPayment")
                print("\nRegistros guardados correctamente")

            else:
                print("\nNo se puede guardar un regitro vacio")

        elif opc == 7:
            # mostrar paquetes guardados
            packages = loadRegistry("findedByPayment")
            amount = 0
            print()
            for id in range(len(packages)):
                print(packages[id].__str__())
                amount += packages[id].payment
            print(f"\nEl monto total pagado es de {amount} pesos.")

    return


if __name__ == '__main__':
    app()
    exit(0)
