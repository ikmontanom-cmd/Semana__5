class Restaurante:
    def __init__(
        self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.menu = []
        self.clientes = []
        
        
    def agregar_plato(self, plato):
        self.menu.append(plato)
        

    def mostrar_menu(self):
        for plato in self.menu:
            print(f"{plato.nombre} - ${plato.precio}")
            
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)  
        
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(f"{cliente.nombre} - {cliente.correo_electronico}")      