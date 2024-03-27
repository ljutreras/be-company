Feature: Hablar con un bot

	Scenario: Hablar con un bot mediante los mensajes del usuario
		GIVEN que la aplicacion esta en ejecucion
		WHEN hago una peticion POST a "http://127.0.0.1:8000/chatbots/0092dfef-0819-4927-a498-f39953af8f52/ask" con el body
			"""
			{
				"message": "buenos dias"
			}
			"""
		THEN recibire una respuesta exitosa de status 200
		AND contiene la respuesta
			"""
			{
				"data": {
					"id": "0092dfef-0819-4927-a498-f39953af8f52",
					"response": "Hola, soy tu asistente virtual, en que te puedo ayudar?"
				}
			}
			"""
    