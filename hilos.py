import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(messge)s')

def consultar(id_persona):
    logging.info("Consultando para el ID "+ str(id_persona))
    time.sleep(2)
    return

def guardar(id_persona, data):
    logging.info("Consultando para el ID "+ str(id_persona) + " data " + data)
    time.sleep(5)
    return

tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo_1", target=consultar, args=(1, ))
t2 = threading.Thread(name="hilo_2", target=guardar, args=(1, " Suscribete!"))

t1.start()
t2.start()

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()

print ("Tiempo transcurrido "+str(tiempo_fin.second - tiempo_ini.second))
print ("Ha concluido el programa")



