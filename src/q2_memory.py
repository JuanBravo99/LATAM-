import json
from collections import Counter
from typing import List, Tuple
from emoji import emoji_list
from memory_profiler import profile

def q2_memory(file_path: str) -> List[Tuple[str, int]]:

#Inicializo un contador para los emojis
    emoji_counter = Counter()
    with open(file_path, 'r') as f:

#Lectura linea por linea del archivo
        for line in f:

#Guardo cada linea en tweet (cada linea representa un tweet)
            tweet = json.loads(line)

#Extraigo los emojis usando 'emojis_list' y lo almaceno y actualizo 'emojis'
            emojis = [emoji['emoji'] for emoji in emoji_list(tweet['content'])]
            emoji_counter.update(emojis)
    
#Creo el top 10 de los emojis mas usados
    return emoji_counter.most_common(10)