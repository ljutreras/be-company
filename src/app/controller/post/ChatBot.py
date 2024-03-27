import numpy as np
from src.shared.functions.FeelingData import FeelingData
from src.shared.databases.MongoConnection import MongoConnection

class ChatBot:
    def create(unique_id: str, user_message: str, model: any) -> dict[str, any]:
        """
        Realiza una consulta al bot identificado por su ID único utilizando el mensaje del usuario para determinar la respuesta más apropiada.

        Args:
            unique_id (str): El ID único del bot al que se hace la consulta.
            user_message (str): El mensaje del usuario para el que se busca una respuesta.
            model (any): El modelo utilizado para generar incrustaciones de texto.

        Returns:
            dict: Un diccionario que contiene la ID del bot y la respuesta generada para el mensaje del usuario.

        Raises:
            No se levantan excepciones en esta función.

        Ejemplo:
            ChatBot.create("123", "Hola", use_model)
            # Retorna:
            # {"id": "123", "response": "Hola, soy tu asistente virtual, en qué puedo ayudarte?"}
        """
        database = MongoConnection.create()
        feeling = FeelingData.create(user_message, model)
        finded_bot = database.find_one({"_id": unique_id})
        actions = [action['description'] for action in finded_bot['actions'].values() if action['description'] != 'Cuando el usuario habla incoherencias , palabras como : asdasd, eweqwe']

        embeddings = {} 
        assignments = []

        all_phrases = actions + [user_message]
        all_embeddings = model(all_phrases) 

        for i, text in enumerate(all_phrases):
            embeddings[text] = all_embeddings[i]    

        similarities = {cat: 0 for cat in actions}

        for cat in actions:
            sim = np.dot(embeddings[user_message], embeddings[cat])
            if sim > 0:
                similarities[cat] = sim
            else:
                similarities[cat] = 0
    
        if max(similarities.values()) > 0.15:
            assigned_category = max(similarities, key=similarities.get)
        else:
            assigned_category = 'Cuando el usuario habla incoherencias , palabras como : asdasd, eweqwe'
        assignments.append(assigned_category) 
        
        response = None
        for value in finded_bot["actions"].values():
            if value["description"] == assignments[0]:
                response = value["response"]
                break
        return {"id": unique_id, "response": response, "feeling": f'El sentimiento del usuario es de carácter {feeling}'}
