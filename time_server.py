import socket
from datetime import datetime

def iniciar_servidor_tiempo():
    servidor = socket.socket()
    puerto = 8000
    servidor.bind(('0.0.0.0', puerto))
    print(f"Servidor de tiempo activo en 0.0.0.0:{puerto}")
    servidor.listen(5)

    while True:
        cliente, direccion = servidor.accept()
        print(f"Conexión desde: {direccion}")

        # Enviar la hora actual
        tiempo_servidor = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(f"Tiempo enviado: {tiempo_servidor}")
        cliente.send(tiempo_servidor.encode())
        cliente.close()

if __name__ == "__main__":
    iniciar_servidor_tiempo()
