import json
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:

#Empiezo un contador para los nombres de usuarios mencionados
    username_counter = Counter()

#Lectura del archivo
    with open(file_path, 'r') as f:
        tweets = [json.loads(line)['mentionedUsers'] for line in f.readlines()]

#Identificar usuarios mencionados en 'tweets' y extraigo 'username'
        usernames = [user['username'] for obj in tweets 
                     if obj is not None for user in obj]
#Actualizo el contador
        username_counter.update(usernames)
#Obtengo el top 10
        return username_counter.most_common(10)

 