## API Backend Django

> Se solicita implementar un prototipo de sistema web para el control de los empleados de una
> empresa que se organiza en unidades (por ejemplo: operaciones, administración), y cada unidad
> en departamentos (por ejemplo: la unidad de operaciones se divide en los departamentos de
> producción y logística).  
> Para cada entidad debe implementar las siguientes funcionalidades:  
> ● Listar todos los registros en una tabla  
> ● Crear un nuevo registro  
> ● Actualizar un registro existente  
> ● Eliminar un registro.

## Configuración de compilación

```bash
# Instalar Python3 segun sistema operativo y comprobar instalacion
python3 --version

# Instalar pip3, por lo regular se instala junto con Python,
pip3 --version

# Instalacion del software del entorno virtual
https://docs.python.org/3/library/venv.html

# Creacion de ambiente virtual dentro de la raiz del proyecto
python -m venv ${nombre_entorno}

# Activar el nuevo ambiente virtual dentro de la raiz del proyecto (referencia archivo manage.py)
source activate

# Verificar si ya esta activado, aparecera dentro de "()"
(${nombre_entorno})

# Instalar todas las dependencias de archivo requirements.txt dentro de la raiz del proyecto
pip install -r requirements.txt

# Correr migraciones, para crear nuestra BD
python manage.py makemigrations
python manage.py migrate

# De ser necesario, crear un superusuario para interactuar con el admin django
python manage.py createsuperuser

# Arrancar el servidor web de desarrollo
python manage.py runserver

# Una vez funcionando el servidor se puede ver la siguiente URL
http://127.0.0.1:8000/

# Para ingresar al admin django con usuario y contrasena creada anteriormenteL
http://127.0.0.1:8000/admin/
```
