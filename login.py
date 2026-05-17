usuario_correcto = "admin"
contrasena_correcta = "1234"

intentos = 0
autenticado = False

while intentos < 3:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("¡Bienvenido!")
        autenticado = True
        break
    else:
        intentos += 1
        if intentos < 3:
            print(f"Credenciales incorrectas. Intento {intentos} de 3.")
        else:
            print("Ha excedido el número máximo de intentos. Acceso denegado.")

if not autenticado and intentos >= 3:
    print("Cuenta bloqueada por seguridad.")