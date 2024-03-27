Feature: Buscar a todos los bots

	Scenario: Se buscan todos los bots disponibles
		GIVEN que la aplicacion se encuentra en ejecucion
		WHEN hago una peticion GET a "http://127.0.0.1:8000/chatbots/" 
		THEN recibire una respuesta de status 200
    