from src.shared.databases.MongoConnection import MongoConnection

class AllBots:
    def create() -> list[dict[str, any]]:
        """
        Obtiene todos los bots almacenados en la base de datos y los devuelve como una lista de objetos.

        Returns:
            list[dict]: Una lista que contiene todos los bots almacenados en la base de datos, cada uno representado como un diccionario.

        Ejemplo:
            AllBots.create()
            # Retorna:
            # [
            #     {"_id": "123", "actions": {"saludar": "Hola", "despedir": "Adiós"}},
            #     {"_id": "456", "actions": {"saludar": "Hello", "despedir": "Goodbye"}}
            # ]
        """
        database = MongoConnection.create()
        response = [element for element in database.find()]
        return response
