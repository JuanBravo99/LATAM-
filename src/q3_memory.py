import json
from collections import Counter
from typing import List, Tuple
from memory_profiler import profile

def q3_memory(file_path: str) -> List[Tuple[str, int]]:

#Inicio contador para los nombres de usuario
    username_counter = Counter()

#Lectura linea por linea del archivo
    with open(file_path, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            
#Extraccion de los usuarios mencionados
            mentioned_users = tweet.get('mentionedUsers', [])
            if mentioned_users is None:
                continue
            
#Actualizo el contador
            for user in mentioned_users:
                if user:
                    username_counter.update([user['username']])

#Obtengo el top 10
    return username_counter.most_common(10)