from typing import List, Tuple
from datetime import datetime
import collections
import heapq
from memory_profiler import profile

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

#Creacion de un diccionario para contar tweets por fecha
    tweets_count = {}

#Creacion de un diccionario para contar tweets segun user y fecha
    users_count = {}

#Lectura el archivo y actualizamos los contadores
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                try:

#Extracción de la fecha y el nombre de usuario
                    date = datetime.datetime.strptime(parts[0], '%Y-%m-%d').date()
                    username = parts[1]

#Actualizo el contador de tweets por fecha
                    tweets_count[date] = tweets_count.get(date, 0) + 1

#Actualizo el contador de tweets por usuario en cada fecha
                    users_count[date] = users_count.get(date, {})
                    users_count[date][username] = users_count[date].get(username, 0) + 1
                except ValueError:
                    pass

#Usando un heap para mantener las top 10 fechas con más tweets
    top_10_dates = heapq.nlargest(10, tweets_count.items(), key=lambda x: x[1])

#Lista de resultados
    return list(zip([(date, max(users_count[date], key=users_count[date].get)) for date, _ in top_10_dates]))

    
