# proyecto_lobo
## Instrucciones django
### Crear proyecto

´django-admin startproject lobo_app´

### crear aplicación
Tenemos que estar dentro de la carpeta de la aplicación, donde está el archivo, ´manage.py´.

´python manage.py startapp´


### migraciones iniciales de la base de datos

´´´sh 
cd lobo_app
python manage.py makemigrations
python manage.py migrate

´´´

### crear superusuario
Esto no funciona sin las instrucciones anteriores

´´´sh 
python manage.py createsuperuser

´´´

### agregar paquetes con pip

Nota: Debe estar activado el ambiente virtual

´´´sh 
pip install python-decouple
´´´

### Liga para configurar cuenta de gmail
https://myaccount.google.com/

### Crear el password
https://myaccount.google.com/apppasswords
