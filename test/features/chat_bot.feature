Feature: Hablar con un bot

	Scenario: Hablar con un bot mediante los mensajes del usuario
		GIVEN que la aplicacion esta en ejecucion
		WHEN hago una peticion POST a "http://127.0.0.1:8000/chatbots/c1c24da0-a41e-417b-bf2c-081b0565e3f7/ask" con el body
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
					"id": "c1c24da0-a41e-417b-bf2c-081b0565e3f7",
					"response": "Hola, soy tu asistente virtual, en que te puedo ayudar?",
					"feeling": "El sentimiento del usuario es de carácter positivo"
				}
			}
			"""
    