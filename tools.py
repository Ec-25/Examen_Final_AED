from pickle import dump, load


def getNumber(msg:str, max:int|None=None, min:int|None=None)->int:
    """Max & Min includes"""
    num = ""
    Cmax = isinstance(max, int)
    Cmin = isinstance(min, int)
    while not isinstance(num, int):
        inp = input(msg)
        try:
            if Cmin and Cmax:
                if min <= int(inp) <= max:
                    num = int(inp)
                else:
                    print(f"Error, el nro debe ser entre {min} y {max}")

            elif Cmin:
                if min <= int(inp):
                    num = int(inp)
                else:
                    print(f"Error, el nro debe ser mayor a {min}")

            elif Cmax:
                if int(inp) <= max:
                    num = int(inp)
                else:
                    print(f"Error, el nro debe ser menor a {max}")

            else:
                num = int(inp)

        except ValueError:
            print("Error, debe ingresar un nro valido...")
            continue

    return num


def getFloat(msg:str, max:float|None=None, min:float|None=None)->float:
    """Max & Min includes"""
    num = ""
    Cmax = isinstance(max, float|int)
    Cmin = isinstance(min, float|int)
    while not isinstance(num, float):
        inp = input(msg)
        try:
            if Cmin and Cmax:
                if min <= float(inp) <= max:
                    num = float(inp)
                else:
                    print(f"Error, el nro debe ser entre {min} y {max}")

            elif Cmin:
                if min <= float(inp):
                    num = float(inp)
                else:
                    print(f"Error, el nro debe ser mayor a {min}")

            elif Cmax:
                if float(inp) <= max:
                    num = float(inp)
                else:
                    print(f"Error, el nro debe ser menor a {max}")

            else:
                num = float(inp)

        except ValueError:
            print("Error, debe ingresar un nro valido...")
            continue

    return num


def saveRegistry(registry:list, name:str="registry") -> None:
    """name = Name of the File"""
    file = open(f"{name}.pickle", 'wb')
    dump(registry, file)
    file.close()
    return


def loadRegistry(name:str="registry") -> list:
    """name = Name of the File"""
    file = open(f"{name}.pickle", 'rb')
    list = load(file)
    file.close()
    return list
