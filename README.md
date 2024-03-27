# Chatbot

El objetivo es crear un chatbot de manera dinamica que se pueda eliminar, modificar e interactuar con el mediante sus diferentes endpoint

## Primeros pasos

1. Se recomienda trabajar en un entorno virtual. Para ello, utiliza el siguiente comando desde tu consola:

    ```bash
    python3.11 -m venv venv
    ```

2. ¿Ya tienes tu entorno virtual? ¡Perfecto! Ahora solo falta activarlo:

    Desde VSCode, sigue estos pasos:
    ```
    CTRL + SHIFT + P
    Python: Select Interpreter
    ⭐​Python 3.11 ('venv': venv) Recommended
    ```

3. A continuación, realiza la instalación de las librerías para nuestro proyecto. Se proporciona un archivo `requirements.txt` que se instala de la siguiente manera:

    ```bash
    pip install -r requirements.txt
    ```

**Nota: Necesitaras tener acceso a MongoDB para poder continuar**

4. ¡Perfecto! Casi lo tienes. Solo falta generar un archivo `.env` para agregar el token que permitirá utilizar la aplicación:

    ```
    MONGO_URL='mongodb+srv://<user>:<password>@cluster0.qbdfyki.mongodb.net/'
    DB_NAME='chat'
    DB_COLLECTION='bot'
    ```

## Ahora solo queda ejecutar nuestra aplicación

1. Desde la consola, levanta el servidor con el siguiente comando:

    ```bash
    uvicorn main:app --port 8000
    ```
    ⛔​ **Por defecto se levantará en el puerto 8000, pero para que arriesgarnos😊​** ⛔​


## 🥳 ¡Felicidades! Ya tienes todo lo necesario para levantar tu servidor 🥳

## Documentacion

puedes ver la documentacion en el siguiente [Link](https://documenter.getpostman.com/view/20768242/2sA35D74CX)
