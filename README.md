# proyecto_lobo
## Instrucciones django
### Crear proyecto

´django-admin startproject lobo_app´

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