from cryptography.fernet import Fernet

with open("clave.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

def leer_credenciales():
    credenciales = {}
    with open("credenciales.txt", "r") as file:
        for line in file:
            correo, contrasena, tipo_usuario, aprobado = line.strip().split(",")
            correo = cipher_suite.decrypt(correo.encode()).decode()
            contrasena = cipher_suite.decrypt(contrasena.encode()).decode()
            tipo_usuario = cipher_suite.decrypt(tipo_usuario.encode()).decode()
            aprobado = cipher_suite.decrypt(aprobado.encode()).decode()
            credenciales[correo] = (contrasena, tipo_usuario, aprobado)
    return credenciales

def escribir_credenciales(correo, contrasena, tipo_usuario, aprobado="False"):
    correo_encrypted = cipher_suite.encrypt(correo.encode()).decode()
    contrasena_encrypted = cipher_suite.encrypt(contrasena.encode()).decode()
    tipo_usuario_encrypted = cipher_suite.encrypt(tipo_usuario.encode()).decode()
    aprobado_encrypted = cipher_suite.encrypt(aprobado.encode()).decode()
    with open("credenciales.txt", "a") as file:
        file.write(f"{correo_encrypted},{contrasena_encrypted},{tipo_usuario_encrypted},{aprobado_encrypted}\n")

def aprobar_usuario(correo):
    credenciales = leer_credenciales()
    if correo in credenciales:
        contrasena, tipo_usuario, _ = credenciales[correo]
        credenciales[correo] = (contrasena, tipo_usuario, "True")
        with open("credenciales.txt", "w") as file:
            for correo, (contrasena, tipo_usuario, aprobado) in credenciales.items():
                correo_encrypted = cipher_suite.encrypt(correo.encode()).decode()
                contrasena_encrypted = cipher_suite.encrypt(contrasena.encode()).decode()
                tipo_usuario_encrypted = cipher_suite.encrypt(tipo_usuario.encode()).decode()
                aprobado_encrypted = cipher_suite.encrypt(aprobado.encode()).decode()
                file.write(f"{correo_encrypted},{contrasena_encrypted},{tipo_usuario_encrypted},{aprobado_encrypted}\n")

def desaprobar_usuario(correo):
    credenciales = leer_credenciales()
    if correo in credenciales:
        contrasena, tipo_usuario, _ = credenciales[correo]
        credenciales[correo] = (contrasena, tipo_usuario, "False")
        with open("credenciales.txt", "w") as file:
            for correo, (contrasena, tipo_usuario, aprobado) in credenciales.items():
                correo_encrypted = cipher_suite.encrypt(correo.encode()).decode()
                contrasena_encrypted = cipher_suite.encrypt(contrasena.encode()).decode()
                tipo_usuario_encrypted = cipher_suite.encrypt(tipo_usuario.encode()).decode()
                aprobado_encrypted = cipher_suite.encrypt(aprobado.encode()).decode()
                file.write(f"{correo_encrypted},{contrasena_encrypted},{tipo_usuario_encrypted},{aprobado_encrypted}\n")