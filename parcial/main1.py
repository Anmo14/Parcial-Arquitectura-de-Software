from clase import Cliente_usuario, Cuenta_cliente, Transaccion_cliente, Proveedor_Beneficio, Beneficio, Autenticacion, Recomendacion_beneficios

def main():
    # Crear usuarios de ejemplo
    user1 = Cliente_usuario("1", "Juan", "password123")
    user2 = Cliente_usuario("2", "María", "secreto456")

    # Crear cuentas para los usuarios
    account1 = Cuenta_cliente("1", user1.id_cliente, 200.0)
    account2 = Cuenta_cliente("2", user2.id_cliente, 60.0)

    # Simular transacciones
    transaction1 = Transaccion_cliente("1", account1.id_cuenta, 120.0)
    transaction2 = Transaccion_cliente("2", account2.id_cuenta, 10.0)

    # Agregar transacciones a las cuentas
    account1.agregar_transaccion(transaction1)
    account2.agregar_transaccion(transaction2)

    # Crear proveedores de beneficios
    provider1 = Proveedor_Beneficio("1", "Proveedor 1")
    

    # Crear beneficios
    benefit1 = Beneficio("1", "Beneficio 1", "Descripción del Beneficio 1", 50.0)
    benefit2 = Beneficio("2", "Beneficio 2", "Descripción del Beneficio 2", 30.0)

    # Agregar beneficios a los usuarios
    user1.agregar_beneficio(benefit1)
    user2.agregar_beneficio(benefit2)

    # Crear tokens de autenticación
    auth1 = Autenticacion(user1.id_cliente, "token123")
    auth2 = Autenticacion(user2.id_cliente, "token456")

    # Crear recomendaciones de beneficios
    recommendation1 = Recomendacion_beneficios(user1.id_cliente, [benefit2])
    recommendation2 = Recomendacion_beneficios(user2.id_cliente, [benefit1])

    # Imprimir los resultados
    print("ID:", user1.id_cliente)
    print("Nombre de Usuario:", user1.nombre)
    print("Contraseña:", user1.contrasena)
    print("Beneficios:", [beneficio.nombre for beneficio in user1.beneficios])
    print()

    print("ID de Cuenta:", account1.id_cuenta)
    print("Saldo:", account1.saldo)
    print("Transacciones:", [(transaccion.id_transaccion, transaccion.monto) for transaccion in account1.transacciones])
    print()

    print("ID:", provider1.id_proveedor)
    print("Nombre:", provider1.nombre)
    print()

    print("Beneficio:")
    print("ID:", benefit1.id_beneficio)
    print("Nombre:", benefit1.nombre)
    print("Descripción:", benefit1.descripcion)
    print("Valor:", benefit1.valor)
    print()

    print("Autenticación:")
    print("ID de Usuario:", auth1.id_cliente)
    print("Token:", auth1.token)
    print()

    print("Recomendación de Beneficios:")
    print("ID de Usuario:", recommendation1.id_cliente)
    print("Beneficios Recomendados:", [beneficio.nombre for beneficio in recommendation1.beneficios_recomendados])
    print()

# Invocar la función principal
if __name__ == "__main__":
    main()