# Chatbot

El objetivo es crear un chatbot de manera dinamica que se pueda eliminar, modificar e interactuar con el mediante sus diferentes endpoint

## Primeros pasos

1. Se recomienda trabajar en un entorno virtual. Para ello, utiliza el siguiente comando desde tu consola:

    ```bash
    python3.11 -m venv venv
    ```

2. ¿Ya tienes tu entorno virtual? ¡Perfecto! Ahora solo falta activarlo:

    ## GIT BASH
    ```
    source venv/Script/activate
    ```
    ## POWER SHELL
    ```
    .\venv\Scripts\activate
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

# TEST

1. Ya teniendo el servidor levantado en una consola, tedras que abrir una nueva terminal y activar el entorno virtual

2. Una vez activado el entorno virtual, deberás ejecutar el comando

    ```bash
    behave test/
    ```
**Nota: Los tests están diseñados para hacer referencia a elementos específicos en la base de datos, por lo que se recomienda utilizar los unique_id proporcionados en los features de los tests para realizar pruebas del backend. Esto facilita la implementación de pruebas de Acceptance Test Driven Development (ATDD) con Cucumber.**

## Documentacion

puedes ver la documentacion en el siguiente [Enlace](https://documenter.getpostman.com/view/20768242/2sA35D74CX)
