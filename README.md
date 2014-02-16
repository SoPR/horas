# :clock3: Horas

Una plataforma para facilitar la [mentoría](http://es.wikipedia.org/wiki/Mentoria).

![Horas Screenshot](https://raw2.github.com/SoPR/horas/design/png/01.png)

### Idea

En Puerto Rico hay cientos de personas que quieren empezar un negocio, una organización benéfica, una liga deportiva, un programa educativo entre muchas otras iniciativas. Las personas que asumen estos proyecto necesitan ayuda para lograr realizar estas cosas que tanto nos hacen falta.

Este proyecto pretende conectar a estas personas que quieren cambiar el mundo con los mentores que los ayudarán a lograrlo.


### Mecánica

Los mentores se registran e indican en que momento de la semana pueden donar **1 hora** de su tiempo para reunirse con alguien que quiere pedirle ayuda, consejo o simplemente conocerle.

Las personas que quieren hablar con mentores (protegidos, discípulos o aprendices) buscan en el directorio de mentores y seleccionan uno de los espacios disponibles. El mentor recibirá un correo electrónico con todos los detalles de la reunión.

Las reuniones se pueden realizar de la manera que sea más conveniente para el mentor. Las opciones son:

- En persona
- [Google Hangout](http://www.google.com/+/learnmore/hangouts/)
- [Skype](http://www.skype.com/)
- [Jitsi](https://jitsi.org/)
- Por teléfono


### Reglas

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


### Reportar errores, sugerencias y otros comentarios

Si tienes una idea de como mejorar esta plataforma o si has encontrado algún error déjanos saber creando un "issue" en el repositorio.

:beetle: [Issues](https://github.com/SoPR/horas/issues) - para reportar problemas, errores, sugerencias, etc.

#### Cómo usar "issues" en GitHub

Aquí un [vídeo](http://www.youtube.com/watch?v=TJlYiMp8FuY) que explica como crear "issues". Recuerda que primero necesitas [crear una cuenta de GitHub](https://github.com/join), es gratis.

[![link](http://i.imgur.com/eN07Qqu.png)](http://www.youtube.com/watch?v=TJlYiMp8FuY)


### Developers

Este proyecto no sería posible sin la colaboración de otros developers que han donado su tiempo para crear esta aplicación. Si  encuentras un error por favor crea un [issue](https://github.com/SoPR/horas/issues) y si puedes arreglarlo te invitamos a hacer y someter un pull request.

Tenemos un [chat room](https://www.hipchat.com/g3IXLRctN) para facilitar la comunicación y coordinación del equipo.

[Chat Room](https://www.hipchat.com/g3IXLRctN)

Si necesitas ideas de como ayudar puede ver la lista de tareas pendientes.

:white_check_mark: [TO-DO](TODO.md)


### Diseñadores

Tenemos un branch dedicado para compartir y colaborar sobre el diseño de la plataforma. Mantendremos el diseño más reciente en ese branch.

:art: [Design](https://github.com/SoPR/horas/tree/design) - Branch dedicado al diseño de este proyecto.


#### Para correr el proyecto

Es necesario tener instalado Python 3.3 y [Brunch](http://brunch.io) para poder correr el proyecto.

```bash
$ git clone https://github.com/SoPR/horas.git
$ cd horas/static/src
$ npm install
$ cd ../..
$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py migrate
$ python manage.py loaddata apps/profiles/fixtures/admin.json
$ python manage.py brunchserver
```
Abre tu browser en [http://localhost:8000/](http://localhost:8000/). Para accesar la sección de administración ve a [http://localhost:8000/admin/](http://localhost:8000/admin/), y usa el username **admin** y el password **abc123**.


### License

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
