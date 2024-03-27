from src.shared.databases.MongoConnection import MongoConnection

class CreateBot:
    def create(unique_id: str, actions: list[str], descriptions: list[str], responses: list[str]) -> dict[str, any]:
        """
        Crea un nuevo bot con las acciones y respuestas proporcionadas o actualiza un bot existente si el unique_id ya existe en la base de datos.

        Args:
            unique_id (str): El unique_id del bot.
            actions (list[str]): Una lista de acciones del bot.
            responses (list[str]): Una lista de respuestas correspondientes a las acciones del bot.

        Returns:
            dict: Un diccionario que contiene el unique_id del bot y un diccionario de acciones y respuestas asociadas.

        Ejemplo:
            CreateBot.create("123", ["saludar", "despedir"], ["Hola", "Adiós"])
            # Retorna:
            # {"id": "123", "actions": {"saludar": "Hola", "despedir": "Adiós"}}
        """
        database = MongoConnection.create()
        finded_bot = database.find_one({"_id": unique_id})
        actions.append('ia no entiende')
        descriptions.append('Cuando el usuario habla incoherencias , palabras como : asdasd, eweqwe')
        responses.append('Disculpa, no te entiendo , me lo podrías explicar de otra manera por favor.🤗')
        bot_data = {}
        for action, description, response in zip(actions, descriptions, responses):
            bot_data[action] = {'description': description, 'response': response}

        if finded_bot is not None:
            database.update_many({'actions': finded_bot['actions']}, {'$set': {'actions': bot_data}}) 
            return {"id": unique_id, "actions": bot_data}
        else:
            database.insert_one({'_id': unique_id, 'actions': bot_data})
            return {"id": unique_id, "actions": bot_data}
