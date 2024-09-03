class Pasajero:
    def __init__(self, id, nombres, apellidos, correo):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.correo = correo

    def mostrar_datos(self):
        return f"ID: {self.id}, Nombres: {self.nombres}, Apellidos: {self.apellidos}, Correo: {self.correo}"

class Vuelo:
    def __init__(self, codigo_vuelo, fecha, ciudad_origen, ciudad_destino):
        self.codigo_vuelo = codigo_vuelo
        self.fecha = fecha
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.lista_pasajeros = []

    def agregar_pasajero(self, pasajero):
        self.lista_pasajeros.append(pasajero)

    def listar_datos_vuelo(self):
        return f"Vuelo: {self.codigo_vuelo}, Fecha: {self.fecha}, Origen: {self.ciudad_origen}, Destino: {self.ciudad_destino}"

    def listar_datos_pasajeros(self):
        return [pasajero.mostrar_datos() for pasajero in self.lista_pasajeros]

def menu():
    vuelos = []

    while True:
        print("\nMenú:")
        print("1. Crear un vuelo")
        print("2. Listar todos los datos de los vuelos del día")
        print("3. Agregar pasajero a un vuelo")
        print("4. Listar todos los datos de los pasajeros de un vuelo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo_vuelo = input("Código del vuelo: ")
            fecha = input("Fecha del vuelo: ")
            ciudad_origen = input("Ciudad de origen: ")
            ciudad_destino = input("Ciudad de destino: ")
            vuelos.append(Vuelo(codigo_vuelo, fecha, ciudad_origen, ciudad_destino))

        elif opcion == "2":
            for vuelo in vuelos:
                print(vuelo.listar_datos_vuelo())

        elif opcion == "3":
            codigo_vuelo = input("Código del vuelo: ")
            vuelo_encontrado = next((vuelo for vuelo in vuelos if vuelo.codigo_vuelo == codigo_vuelo), None)
            if vuelo_encontrado:
                id_pasajero = input("ID del pasajero: ")
                nombres = input("Nombres del pasajero: ")
                apellidos = input("Apellidos del pasajero: ")
                correo = input("Correo electrónico del pasajero: ")
                pasajero = Pasajero(id_pasajero, nombres, apellidos, correo)
                vuelo_encontrado.agregar_pasajero(pasajero)
            else:
                print("Vuelo no encontrado.")

        elif opcion == "4":
            codigo_vuelo = input("Código del vuelo: ")
            vuelo_encontrado = next((vuelo for vuelo in vuelos if vuelo.codigo_vuelo == codigo_vuelo), None)
            if vuelo_encontrado:
                for datos_pasajero in vuelo_encontrado.listar_datos_pasajeros():
                    print(datos_pasajero)
            else:
                print("Vuelo no encontrado.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
