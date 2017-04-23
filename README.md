# Horas [![Build Status](https://travis-ci.org/SoPR/horas.svg)](https://travis-ci.org/SoPR/horas) [![Dependency Status](https://gemnasium.com/badges/github.com/SoPR/horas.svg)](https://gemnasium.com/github.com/SoPR/horas) [![Can I Use Python 3?](https://caniusepython3.com/check/8ec27297-1f0c-4d40-a4d3-8503eda3debe.svg)](https://caniusepython3.com/check/8ec27297-1f0c-4d40-a4d3-8503eda3debe)

Una plataforma para facilitar la [mentoría](http://es.wikipedia.org/wiki/Mentoria).

[![Regístrate](http://i.imgur.com/dN5Qz4w.png)](http://eepurl.com/OFTOv)


![Horas Screenshot](https://raw.githubusercontent.com/SoPR/horas/design/png/01.png)

## Idea

En Puerto Rico hay cientos de personas que quieren empezar un negocio, una organización benéfica, una liga deportiva, un programa educativo entre muchas otras iniciativas. Las personas que asumen estos proyecto necesitan ayuda para lograr realizar estas cosas que tanto nos hacen falta.

Este proyecto pretende conectar a estas personas que quieren cambiar el mundo con los mentores que los ayudarán a lograrlo.


## Mecánica

Los mentores se registran e indican en que momento de la semana pueden donar **1 hora** de su tiempo para reunirse con alguien que quiere pedirle ayuda, consejo o simplemente conocerle.

Las personas que quieren hablar con mentores (protegidos, discípulos o aprendices) buscan en el directorio de mentores y seleccionan uno de los espacios disponibles. El mentor recibirá un correo electrónico con todos los detalles de la reunión.

Las reuniones se pueden realizar de la manera que sea más conveniente para el mentor. Las opciones son:

- En persona
- [Google Hangout](http://www.google.com/+/learnmore/hangouts/)
- [Skype](http://www.skype.com/)
- [Jitsi](https://jitsi.org/)
- Por teléfono


## Reglas

Para que este sistema sea efectivo debemos plantear algunas reglas simples a las que todos nos comprometeremos a respetar.

1. Este proyecto es y será 100% gratuito tanto para los mentores como para los aprendices.
2. De ser necesario conseguir financiamiento para pagar los gastos relacionados a la plataforma se aceptarán donaciones y el 100% de los recaudos deben ir a cubrir los gastos y nunca al bolsillo de ninguna persona o compañía involucrada en la creación o mantenimiento de este servicio.
3. 100% transparente
    - Toda la comunicación relacionada a este proyecto se llevará a cabo en foros públicos.
    - Todo documento relacionado a la creación, mantenimiento, financiamiento o cualquier otra actividad relacionada a esta plataforma se hará público sin excepciones. Esto incluye contratos, recibos, acuerdos de colaboración, auspicios, donaciones, absolutamente todo.
    - El código de la aplicación será abierto y libre para siempre.
    - Todas las personas que se registren como mentores o como aprendices tendrán un perfil público donde aparecerá su disponibilidad y otras estadísticas que ayuden a resumir su envolvimiento en la plataforma.
4. Los **mentores** deben comprometerse a donar 1 hora a la semana para ayudar reunirse y hablar con alguien que lo requiera sin excepción de persona.
5. Los **aprendices** deben comprometerse a ser respetuosos del tiempo de los mentores siendo puntuales y estando preparados para la reunión. Una vez terminada la reunión es importante completar el "review" de esa reunión para que otros sepan como te fue.


## Reportar errores, sugerencias y otros comentarios

Si tienes una idea de como mejorar esta plataforma o si has encontrado algún error déjanos saber creando un "issue" en el repositorio.

[Issues](https://github.com/SoPR/horas/issues) - para reportar problemas, errores, sugerencias, etc.

### Cómo usar "issues" en GitHub

Aquí un [vídeo](http://www.youtube.com/watch?v=TJlYiMp8FuY) que explica como crear "issues". Recuerda que primero necesitas [crear una cuenta de GitHub](https://github.com/join), es gratis.

## Developers

Este proyecto no sería posible sin la colaboración de otros developers que han donado su tiempo para crear esta aplicación. Si  encuentras un error por favor crea un [issue](https://github.com/SoPR/horas/issues) y si puedes arreglarlo te invitamos a hacer y someter un pull request.

Tenemos un [chat room](https://www.hipchat.com/g3IXLRctN) para facilitar la comunicación y coordinación del equipo.

[Chat Room](https://www.hipchat.com/g3IXLRctN)

Si necesitas ideas de como ayudar puede ver la lista de tareas pendientes.

[TO-DO](TODO.md)


### Para correr el proyecto

Hay dos opciones para correr el proyecto la primera usando Vagrant y la segunda instalando en tu ambiente local.

#### Opción 1: Vagrant
Para esta opción debes tener instalado [VirtualBox](https://www.virtualbox.org/) y [Vagrant](http://www.vagrantup.com/). Ambos son fáciles de instalar, gratis y disponibles para varias plataformas. Esta es la opción recomendada para colaboradores nuevos.

```bash
$ git clone https://github.com/SoPR/horas.git
$ cd horas
$ vagrant up
```
Este paso tomará varios minutos dependiendo de su conexión de internet. Luego.

```bash
$ vagrant ssh
$ cd horas
$ runhoras
```

Abre tu browser en [http://localhost:8000/](http://localhost:8000/). Para accesar la sección de administración ve a [http://localhost:8000/admin/](http://localhost:8000/admin/), y usa el username **admin** y el password **abc123**.


#### Opción 3: Docker

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

#### Opción 3: Local

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


## Prensa
[Mentoría gratis para la innovación boricua](http://www.elnuevodia.com/mentoriagratisparalainnovacionboricua-1731302.html) - El Nuevo Día


## Donaciones

100% de las donaciones hechas irán a pagar los gastos de hosting y mantenimiento de la plataforma que en este momento son **$29.00 USD mensual**. Pronosticamos que en poco tiempo este número debe subir así que por eso estamos apuntando a asegurar $40.00 mensual. La idea es que la comunidad que se beneficia del proyecto pueda financiar los gastos recurrentes.

[![Support via Gittip](https://rawgithub.com/twolfson/gittip-badge/0.2.0/dist/gittip.png)](https://www.gittip.com/gcollazo/)

[![Donate Bitcoins](http://i.imgur.com/bMKkFH4.png)](https://coinbase.com/checkouts/2c4c170ecd0e2981e7fe16ca3d3e994d)


## License

All of "Horas" is licensed under the MIT license.

Copyright (c) 2014 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
