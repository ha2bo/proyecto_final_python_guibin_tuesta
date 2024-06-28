# Strong Canary Gym - Django Project

## Alumno

TEOFILO SAMUEL GUIBIN TUESTA

## Video explicativo

Link: https://youtu.be/AHXYCeY9bYQ

## Descripción

Bienvenido al proyecto de la página web de **Strong Canary Gym**, un gimnasio que se destaca por ofrecer diferentes categorías de servicios para satisfacer las necesidades de nuestros clientes. Este proyecto ha sido desarrollado utilizando el framework Django.

## Estructura del Proyecto

El proyecto está organizado en varias secciones clave:

1. **Inicio**: Esta sección presenta la información del estudiante desarrollador del proyecto.
2. **Sobre Nosotros**: Aquí se encuentra la información detallada del gimnasio, su misión, visión y los valores que lo caracterizan.
3. **Sedes**: En esta sección se muestran todas las sedes del gimnasio. Los usuarios pueden filtrar las sedes según la categoría del gimnasio: Prime, Classic, y Plus.
4. **Contáctanos**: Una página de contacto donde los usuarios pueden ingresar su nombre, teléfono, email y comentario sobre cualquier consulta o necesidad que tengan.

## Instalación

Sigue los siguientes pasos para configurar el proyecto en tu máquina local:

1. Clona este repositorio:
    ```bash
    git clone https://github.com/ha2bo/Tercera_pre_entrega_Guibin_Tuesta.git
    ```

2. Accede al directorio del proyecto

3. Crea un entorno virtual:
    ```bash
    pipenv shell
    ```

4. Instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

5. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador web:
    ```plaintext
    http://127.0.0.1:8000
    ```

## Uso

### Usuario staff
Usuario: coder
Contrasena: Coderhouse1!

### Inicio
La página de inicio muestra la información del estudiante desarrollador del proyecto.

### Sobre Nosotros
En esta sección se proporciona información sobre el estudiante

### Sedes
Aquí se listan todas las sedes del gimnasio. Los usuarios pueden filtrar las sedes según las categorías: Prime, Classic, y Plus.

### Contáctanos
En esta sección, los usuarios pueden llenar un formulario con su nombre, teléfono, email y un comentario o consulta que deseen hacer.

## Permisos

### Modo usuario
#### Mi cuenta

El usuario puede editar solo su propia información (Correo, Nombre, Apellido, Sede, Contraseña)

### Modo administrador
#### Sedes

Se puede editar informacion de las sedes, asi como agregar sedes o eliminar

#### Usuarios

Permite buscar a los usuarios registrados por su nombre

## Pruebas

El test case de pruebas lo puede hallar en: Pruebas_Guibin_Tuesta.xlsx

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (feature/nueva-caracteristica).
3. Realiza tus cambios y haz commit de los mismos.
4. Envía un pull request describiendo los cambios realizados.

## Licencia

Este proyecto esta sin licencia porque es para aprobar

