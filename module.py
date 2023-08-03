from tools import getNumber, getFloat


class Paquete:
    def __init__(self, nro_id:int, title:str, medio:int, payment:float, destination:int, client:str) -> None:
        self.nro_id = nro_id
        self.title = title
        self.medio = medio
        self.payment = payment
        self.destination = destination
        self.client = client

    def __str__(self) -> str:
        return f"{self.nro_id}]- El sr. {self.client}, destino a {self.destination}. Pago el monto de {self.payment} pesos, con Id de transporte {self.medio}"


def setPackage() -> Paquete:
    """Set Manual Package"""
    id = getNumber("\nNro de Ticket:\t", min=1)
    title = input("Descripcion:\t")
    medio = getNumber("Medio de Transporte[0-9]:\t", 9, 0)
    payment = getFloat("Monto Pagado:\t", min=1)
    destination = getNumber("Destino Final[1-50]:\t", 50, 1)
    client = input("Nombre del Cliente:\t")
    return Paquete(id, title, medio, payment, destination, client)


def getIndexMinMax(list:list[Paquete], nro:int) -> int:
    izq = 0
    if len(list):
        der = len(list) - 1
        while izq <= der:
            med = (izq + der) // 2
            if list[med].nro_id == nro:
                return med
            elif list[med].nro_id < nro:
                izq = med + 1
            elif list[med].nro_id > nro:
                der = med -1
    return izq


def searchTitle(list:list[Paquete], tit:str) -> Paquete|None:
    for obj in list:
        if obj.title == tit:
            return obj
    return None


def indexTranportDestin(package: Paquete) -> tuple[int, int]:
    med = package.medio
    dest = package.destination
    return (med, dest)


def paymentByClient(list:list[Paquete], client:str) -> float:
    Tpayment = 0
    for pack in list:
        if pack.client == client:
            Tpayment += pack.payment
    return Tpayment


def getPackagesByMinAmount(list:list[Paquete], min:float) -> list[Paquete]:
    finded = []
    for pack in list:
        if pack.payment >= min:
            finded.append(pack)
    return finded
