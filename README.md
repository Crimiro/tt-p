# Prueba

Aplicación web desarrollada con FastAPI que permite a los usuarios subir archivos y escanearlos en busca de virus utilizando la API v2 de VirusTotal.

## Requisitos

- Python 3.9 o superior
- Docker (opcional, para ejecutar la aplicación en un contenedor)

## Instalación sin Docker

1. Clona el repositorio:

    ```sh
    git clone https://github.com/Crimiro/tt-p.git
    cd tt-p
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Crea un archivo `.env` en el directorio raíz del proyecto y añade tu clave de API de VirusTotal:

    ```env
    VIRUSTOTAL_API_KEY=tu_clave_de_api
    ```

## Uso

Para ejecutar la aplicación localmente, usa el siguiente comando:

```sh
uvicorn main:app --reload
```

La aplicación estará disponible en http://127.0.0.1:8000.

## Uso con Docker

1. Construye la imagen de Docker:

    ```sh
    docker-compose build
    ```

2. Inicia el contenedor:

    ```sh
    docker-compose up
    ```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Endpoints

- `GET /`: Devuelve un mensaje de bienvenida.
- `POST /upload/`: Permite subir un archivo y escanearlo en busca de virus. **Nota: Solo se permiten archivos PDF, JPEG y PNG de hasta 32 MB.**

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.