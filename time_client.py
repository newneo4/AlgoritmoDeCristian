import socket
from datetime import datetime, timedelta  # Importar timedelta
from dateutil import parser
from timeit import default_timer as timer

def sincronizar_reloj():
    s = socket.socket()
    puerto = 8000
    s.connect(('127.0.0.1', puerto))

    tiempo_inicio = timer()

    # Recibir hora del servidor
    tiempo_servidor = parser.parse(s.recv(1024).decode())
    tiempo_fin = timer()
    tiempo_local = datetime.now()

    print(f"Tiempo del servidor: {tiempo_servidor}")
    latencia = (tiempo_fin - tiempo_inicio) / 2
    print(f"Latencia estimada: {latencia:.6f} segundos")

    # Ajustar el reloj local
    tiempo_sincronizado = tiempo_servidor + timedelta(seconds=latencia)  # Usar timedelta correctamente
    print(f"Reloj sincronizado del sensor: {tiempo_sincronizado}")
    s.close()

if __name__ == "__main__":
    sincronizar_reloj()
