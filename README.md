# Pasos a realizar para el levantamiento del proyecto

## Tecnologias a utilizar 

 * python
 * Django
 * sql server

### Paso 1: Crear base de datos en sql server de ser posible crear usuario especifico para la base de datos
    una vez que que se crea la base de datos  agregar los datos  en el archivo settings.py a continuacion un ejemplo, 


    DATABASES = {
    'default': { 
        'ENGINE': 'mssql',
        'NAME': 'seguros_django ',
        'USER':'sa',
        'PASSWORD':'ChangeMe1$',
        'HOST':'127.0.0.1',
        'PORT':'1433',
        'OPTIONS':{
            'driver':'ODBC Driver 17 for SQL Server', #
           }
    }
}

### Paso 2:  ejecutar el siguiente comando  "pip3 install -r  requirements.txt"  
    En caso de ser necesario incluir la ruta  completa del archivo(se encuentra en este mismo  repositorio) este permitira instalar las librerias necesaria para correr el proyecto

### Paso 3: Ejecutar los siguientes comandos
    python manage.py makemigrations
    python manage.py migrate

    Estos permitiran crear las tablas de las base de datos  con la estructura definida en los modelos. De igual manera se pudiera ejecutar la sentencia SQL en la base de datos para la creacion de las tablas.

### paso 4: ejecutar el siguiente  comando 
    python manage.py create_procedures

    Estes script permitira crear los procedures en la base de datos para el correcto funcionamiento 

### paso 5: Si se quiere cargar una pequeña muesta de datos ejecutar el siguiente comando
    python manage.py loaddata data/* 

    cargara 6 objetos en base de datos solo es una muestra representativa,  de igual manera se pudiera hacer restaurando un backup de base de datos


### paso 6: Ejecutar el proyecto de manera local
    python manage.py runserver 

### Se adjunta coleccion postman de los servicios

    https://documenter.getpostman.com/view/24845288/2s9YXk31b3

### ***Falto la parte de Docker debido a que no se alcazo a trabajar en ella debido a la falta de tiempo, asi como tambien falto depurar lo setting para que se tome mediante variables de entorno y no directanmente seteadas en el codigo ***