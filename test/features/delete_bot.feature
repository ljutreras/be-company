Feature: Eliminacion de un bot
    Scenario: Intentar eliminar un bot que no existe
        GIVEN que la aplicación se esta ejecutando
        WHEN hago una petición DELETE a "http://127.0.0.1:8000/chatbots/123"
        THEN la respuesta tiene que ser 404
