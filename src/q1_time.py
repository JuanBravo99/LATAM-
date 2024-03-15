from typing import List, Tuple
from datetime import datetime
import collections

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    fechas_tw = collections.defaultdict(list)

#Leo el archivo completo
    with open(file_path, 'r') as file:
        lines = file.readlines()

#Se procesa y se divide cada linea (considerando que cada linea es un tweet)
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            try:
                date = datetime.datetime.strptime(parts[0], '%Y-%m-%d').date()
                username = parts[1]
                fechas_tw[date].append(username)
            except ValueError:
                pass
#Se obtienen y orden las fechas de cada tweet
    fechas_ord = sorted(fechas_tw.items(), key=lambda x: len(x[1]), reverse=True)
    top_10_fechas = fechas_ord[:10]
    
    return list(zip([(date, max(users, key=users.count)) for date, users in top_10_fechas]))
