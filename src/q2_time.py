import json
from collections import Counter
from typing import List, Tuple
from emoji import emoji_list

def q2_time(file_path: str) -> List[Tuple[str, int]]:

#Almaceno los tweets en una lista
    emojis = []
    
#Lectura del archivo 
    with open(file_path, 'r') as f:
        for line in f:

#Guardo cada linea en tweet (cada linea representa un tweet)
            tweet = json.loads(line)

#Extraigo y almaceno los emojis del archivo en la lista 'emojis' al extenderla 
            emojis.extend(emoji['emoji'] for emoji in emoji_list(tweet['content']))

#Se crea un contador para el top 10
    return Counter(emojis).most_common(10)