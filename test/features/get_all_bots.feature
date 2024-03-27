Feature: Buscar a todos los bots

	Scenario: Se buscan todos los bots disponibles
		GIVEN que la aplicacion se encuentra en ejecucion
		WHEN hago una peticion GET a "http://127.0.0.1:8000/chatbots/" 
		THEN recibire una respuesta de status 200
		AND contendra la respuesta
			"""
			{
				"data": [
					{
						"_id": "0092dfef-0819-4927-a498-f39953af8f52",
						"actions": {
							"saludando al bot": "Hola, soy tu asistente virtual, en que te puedo ayudar?",
							"menciona un animal": "Los perros son geniales"
						}
					}
				]
			}
			"""
    