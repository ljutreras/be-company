import numpy as np

class FeelingData:
    def create(user_message: str, model: any):
        """
        Determina si un mensaje del usuario evoca sentimientos positivos o negativos.

        Args:
            user_message (str): El mensaje del usuario para analizar.
            model (any): El modelo de procesamiento de lenguaje natural a utilizar.

        Returns:
            str: 'positivo' si se detectan sentimientos positivos,
                 'negativo' si se detectan sentimientos negativos,
                 'No detecto una emoción clara' si no se detecta claramente ningún sentimiento.
        """

        feeling_data = [
            {
                'description': 'felicidad, alegría, amor, gratitud, esperanza, paz, satisfacción, orgullo, aprecio, entusiasmo',
                'response': 'positivo'
            },
            {
                'description': 'tristeza, enojo, miedo, desesperanza, odio, desprecio, desilusión, preocupación, inseguridad, frustración',
                'response': 'negativo'
            },
        ]
        embeddings = {} 
        assignments = []
        descriptions = [item['description'] for item in feeling_data]


        all_phrases = descriptions + [user_message]
        all_embeddings = model(all_phrases) 

        for i, text in enumerate(all_phrases):
            embeddings[text] = all_embeddings[i]    

        for text in [user_message]:
            similarities = {cat: 0 for cat in descriptions}

            for cat in descriptions:
                sim = np.dot(embeddings[text], embeddings[cat])
                if sim > 0.1:
                    similarities[cat] = sim
                else:
                    similarities[cat] = 0   
            if max(similarities.values()) > 0:
                assigned_category = max(similarities, key=similarities.get)
            else:
                assigned_category = 'No detecto una emoción clara'
            assignments.append(assigned_category) 
        
        response = None
        for item in feeling_data:
            if item['description'] == assignments[0]:
                response = item['response']
                break
        
        return response
