class Cliente_usuario:

    def __init__(self, id_cliente, nombre, contrasena):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contrasena = contrasena
        self.beneficios = []

    def agregar_beneficio(self, beneficio):

        self.beneficios.append(beneficio)

class Cuenta_cliente:


    def __init__(self, id_cuenta, id_cliente, saldo):
        self.id_cuenta = id_cuenta
        self.id_cliente = id_cliente
        self.saldo = saldo
        self.transacciones = []

    def agregar_transaccion(self, transaccion):
  
        self.transacciones.append(transaccion)

class Transaccion_cliente:
 

    def __init__(self, id_transaccion, id_cuenta, monto):
        self.id_transaccion = id_transaccion
        self.id_cuenta = id_cuenta
        self.monto = monto

class Proveedor_Beneficio:

    def __init__(self, id_proveedor, nombre):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.beneficios = []

class Beneficio:

    def __init__(self, id_beneficio, nombre, descripcion, valor):
        self.id_beneficio = id_beneficio
        self.nombre = nombre
        self.descripcion = descripcion
        self.valor = valor

class Autenticacion:

    def __init__(self, id_cliente, token):
        self.id_cliente = id_cliente
        self.token = token

class Recomendacion_beneficios:

    def __init__(self, id_cliente, beneficios_recomendados):
        self.id_cliente = id_cliente
        self.beneficios_recomendados = beneficios_recomendados