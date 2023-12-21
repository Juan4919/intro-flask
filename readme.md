# Aplicación de introducción a Flask

Propgrama hecho en Python con el framework Flask, Hello World

# Instalación 

- Crear un entorno en Python y ejecutar el comando

``pip install -r requirements.txt``

la librería utilizada en flask https://flask-wtf.readthedocs.io/en/1.2.x/

# Ejecución del programa 

 - inicializar parametros para servidor de flask 
 - En Mac:
    ``export FLASK_APP=main.py``
 - En Windows: 
    ``set FLASK_APP=main.py``

 - Comando para ejecutar el servidor 
    ``flask --app main run``

 - Comando para ejecutar servidor en otro puerto (default 5000)
    ``flask --app main run -p 5002``

 - Comando para ejecutar el servidor en modo debug, y realizar cambios en tiempo real 
    ``flask --app main --debug run``