# MQTT-App

MQTT-App is a Django application to use MQTT (Message Queuing Telemetry Transport) concepts in Python.

## Description

This project aims to integrate the MQTT protocol into a Django application, allowing efficient communication between IoT (Internet of Things) devices and the web application.

## Features

- MQTT message publishing
- MQTT topic subscription
- MQTT connection management
- Web interface for monitoring and control

## Requirements

- Python 3.x
- Django 3.x
- Paho-MQTT

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/davi-ga/mqtt-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd mqtt-app
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. ADD a `.env` file in the project root directory with the following content:
    ```env
    DEBUG=on
    SECRET_KEY=custom-secret-key-test-here
    API_PORT=8383

    DB_HOST=
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_ENGINE=django.db.backends.postgresql
    DB_PORT=

    REDIS_CELERY_URL=redis://redis:6379/1
    REDIS_CHANNELS_URL=redis://redis:6379/2

    MQTT_BROKER_HOST=mosquitto
    ```

### Using Docker

1. Run the Docker Compose:
    ```bash
    docker-compose up --build
    ```
3. Access the application in your browser:
    ```
    http://127.0.0.1:{PORT}/
    ```

## Contribution

Contributions are welcome! Feel free to open issues and pull requests.

## Contributors

Special thanks to my love:

- [@Ana Carolina](https://github.com/mxtqnt)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.