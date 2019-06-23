## Developers

Este proyecto no sería posible sin la colaboración de otros developers que han donado su tiempo para crear esta aplicación. Si encuentras un error por favor crea un [issue](https://github.com/SoPR/horas/issues) y si puedes arreglarlo te invitamos a hacer y someter un pull request.

Tenemos un [chat room - #horas-project](https://startupsofpr.slack.com/messages/C4HAXGZL5) para facilitar la comunicación y coordinación del equipo. Si necesitas una cuenta puedes [crearla aqui](https://bit.ly/sopr-slack).

* [Creación de Cuenta para Slack de SoPR](https://bit.ly/sopr-slack)
* [Chat Room - #horas-project](https://startupsofpr.slack.com/messages/C4HAXGZL5)

Si necesitas ideas de como ayudar puede ver la lista de tareas pendientes.

[Github issues](https://github.com/SoPR/horas/issues)


### Para correr el proyecto

Hay dos opciones para correr el proyecto, la primera usando Docker y la segunda instalandolo en tu ambiente local.

#### Opción 1: Docker

**Instalación**

**Linux**

Puedes encontrar instrucciones de como instalar Docker para diferentes distribuciones de Linux [aqui](https://docs.docker.com/engine/installation/#docker-editions).

Distribuciones populares:

- [Ubuntu](https://docs.docker.com/engine/installation/linux/ubuntu/)
- [Debian](https://docs.docker.com/engine/installation/linux/debian/)
- [Fedora](https://docs.docker.com/engine/installation/linux/fedora/)

**Mac OS**

La mejor manera de utilizar Docker en Mac Os es utilizando [Docker for Mac](https://www.docker.com/docker-mac).

**Windows**

La mejor manera de utilizar Docker en Mac Os es utilizando [Docker for Windows](https://www.docker.com/docker-windows).

** Como crear imagenes de Horas con Docker **

```bash
# Clonear repositorio
$ git clone https://github.com/SoPR/horas.git

# Instalar dependencias para el build de JS / CSS
$ cd horas/static
$ npm install  # 'yarn' si lo tienes instalado

# Crear la imagen de Docker.
$ cd ..
$ docker-compose build

# Once the image is created you can create the container
$ docker-compose up -d

# When the containers are created and running you can then run Django manage commands
$ docker-compose exec web python manage.py collectstatic

# Migración y data inicial
$ python manage.py migrate
$ python manage.py loaddata apps/profiles/fixtures/admin.json
```

El archivo docker-compose.yml contiene toda la configuración de los servicios de Docker necesarios tener una instancia de Horas corriendo.

Abre tu browser en [http://localhost:8000/](http://localhost:8000/). Para accesar la sección de administración ve a [http://localhost:8000/admin/](http://localhost:8000/admin/), y usa el username **admin** y el password **abc123**.

#### Opción 2: Local

**Requisitos**

- [Python 2.7](https://www.python.org/)
- [Node.js LTS](https://nodejs.org) (incluye npm)
- [Yarn](https://yarnpkg.com) (opcional)

```bash
# Clonear repositorio
$ git clone https://github.com/SoPR/horas.git

# Instalar dependencias para el build de JS / CSS
$ cd horas/static
$ npm install  # 'yarn' si lo tienes instalado

# Copiar archivo de variables de ambiente
$ cd ..
$ cp .env.example .env

# Instalar dependencias python
$ pip install -r requirements.txt

# Migración y data inicial
$ python manage.py migrate
$ python manage.py loaddata apps/profiles/fixtures/admin.json

# Correr server de django y webpack --watch
$ python manage.py webpackserver
```

Abre tu browser en [http://localhost:8000/](http://localhost:8000/). Para accesar la sección de administración ve a [http://localhost:8000/admin/](http://localhost:8000/admin/), y usa el username **admin** y el password **abc123**.

##### Para los usuarios de Mac OSX
Durante la instalacion de los requerimientos con pip:

```bash
$ pip install -r requirements.txt
```
Es posible que se encuentren con este error:

```
src/_pylibmcmodule.h:42:10: fatal error: 'libmemcached/memcached.h' file not found
    #include <libmemcached/memcached.h>
             ^
    1 error generated.
```

Esto se puede dar cuando __libmemcached__ no esta instalada en su sistema. La solucion es instalar __libmemcached__ de una de las siguientes maneras:

__Homebrew__

```bash
$ brew install libmemcached
```

__Ports__

```bash
$ sudo port install libmemcached
```

Una vez hecho esto pueden volver al paso ```$ pip install -r requirements.txt``` y continuar con las instrucciones.

#### Para correr tests
```
$ python manage.py test --configuration=Testing --verbosity=3 --noinput
```

## Diseñadores

Tenemos un branch dedicado para compartir y colaborar sobre el diseño de la plataforma. Mantendremos el diseño más reciente en ese branch.

[Design](https://github.com/SoPR/horas/tree/design) - Branch dedicado al diseño de este proyecto.