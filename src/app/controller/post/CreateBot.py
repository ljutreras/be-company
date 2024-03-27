from src.shared.databases.MongoConnection import MongoConnection

class CreateBot:
    def create(unique_id: str, actions: list[str], responses: list[str]) -> dict[str, any]:
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
        result_dict = {action: response for action, response in zip(actions, responses)}

        if finded_bot is not None:
            database.update_many({'actions': finded_bot['actions']}, {'$set': {'actions': result_dict}}) 
            return {"id": unique_id, "actions": result_dict}
        else:
            database.insert_one({'_id': unique_id, 'actions': result_dict})
            return {"id": unique_id, "actions": result_dict}
