Feature: Crear un bot

	Scenario: Creacion de un bot a partir de sus acciones y respuestas
		GIVEN que la aplicacion esta en ejecucion en el puerto 8000
		WHEN hago una solicitud POST a "http://127.0.0.1:8000/chatbots/" con el body
			"""
			{
				"actions": ["saludar", "animal"],
				"descriptions": ["el usuario esta saludando con un buenas, hola, como esta", "el usuario esta preguntando por un animal"],
				"responses":["Hola, soy tu asistente virtual, en que te puedo ayudar?", "Los perros son geniales"],
				"unique_id": ""
			}
			"""
		THEN deberia recibir una respuesta exitosa de status 200
    