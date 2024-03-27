Feature: Crear un bot

	Scenario: Creacion de un bot a partir de sus acciones y respuestas
		GIVEN que la aplicacion esta en ejecucion en el puerto 8000
		WHEN hago una solicitud POST a "http://127.0.0.1:8000/chatbots/" con el body
			"""
			{
				"questions": ["saludando al bot", "menciona un animal"],
				"responses":["Hola, soy tu asistente virtual, en que te puedo ayudar?", "Los perros son geniales"],
				"unique_id": "0092dfef-0819-4927-a498-f39953af8f52"
			}
			"""
		THEN deberia recibir una respuesta exitosa de status 200
		AND debería contener la respuesta
			"""
			{
				"data": {
					"id": "0092dfef-0819-4927-a498-f39953af8f52",
					"actions": {
						"saludando al bot": "Hola, soy tu asistente virtual, en que te puedo ayudar?",
						"menciona un animal": "Los perros son geniales"
					}
				}
			}
			"""
    