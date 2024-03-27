from fastapi import HTTPException
from src.shared.databases.MongoConnection import MongoConnection


class DeleteBot:
    def create(unique_id: str) -> dict[str, str]:
        """
        Elimina un bot de la base de datos utilizando su ID único.

        Args:
            unique_id (str): El ID único del bot que se desea eliminar.

        Returns:
            dict: Un diccionario que contiene un mensaje de confirmación si el bot fue eliminado correctamente.

        Raises:
            HTTPException: Se levanta una excepción HTTP con un código de estado 404 si el bot no se encuentra en la base de datos.

        Ejemplo:
            DeleteBot.create("123")
            # Retorna:
            # {"message": "Bot with ID 123 deleted successfully"}
        """
        database = MongoConnection.create()
        response = database.delete_one({'_id': unique_id})
        
        if response.deleted_count == 1:
            return {"message": f"Bot with ID {unique_id} deleted successfully"}
        else:
            raise HTTPException(status_code=404)
