# ODOO 17 Community Edition

Este repositorio contiene la configuración necesaria para ejecutar un ambiente de Odoo 17.0 para probar el módulo personalizado para gestion de inscripciones de alumnos.

## Requisitos

Contar con la ultima version de `docker` y `docker compose` instalados en el ambiente destino.

## Levantando el ambiente

1. $ docker-compose up -d

Despues de ejecutar el comando anterior, se descargaran las imagenes necesarias y se ejecutaran los contenedores correspondientes.

## Ambiente

La configuracioon por defecto levanta los siguientes servidores en el host:

1. Postgres, corriendo en el puerto 5432
2. Oddo, corriendo en el puerto 8069

Nota: El master password de Odoo es admin123, de igual modo esto lo puedes cambiar desde el directorio config.

## Modelos

1. unam.student --> Modelo para gestion de Alumnos. 

* Se utilizó el mecanismo de herencia delegada hacia res.partner, de modo que cada vez que se crea un nuevo alumno tambien se crea un contacto de forma automática, a su vez que se garantiza el uso de todos los campos y métodos disponibles en el modelo padre.
* Se agrego el método onchange _onchage_student_age para calcular la edad del alumno de forma automática.
* Por defecto el grupo nativo de Odoo "Internal User" tendra acceso de lectura al modulo, esto garantiza la visualización del módulo luego de su instalación.
* El grupo de acceso "Profesor" solo tiene permisos de lectura, mientras que el grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."

2. unam.subject --> Modelo para registro de materias. 

* Se creó un modelo sencillo con acceso a tres campos para la definición de las materias.
  - Nombre
  - Descripción
  - Límite de crédito
* Esta funcionalidad sera visible desde el menu de "Ajustes" del modulo.
* Los grupos de acceso "Profesor" y "Alumno" no tienen acceso a este modelo, mientras que el grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."

3. unam.teacher --> Modelo para gestion de Profesores. 

* Se utilizó el mecanismo de herencia delegada hacia res.partner, de modo que cada vez que se crea un nuevo profesor tambien se crea un contacto de forma automática, a su vez que se garantiza el uso de todos los campos y métodos disponibles en el modelo padre.
* Se creó un campo o2m para asociar todas las materias que puede dictar el profesor. Esta relacion esta formada con el modelo unam.teacher.subject
* El grupo de acceso "Alumno" no tiene acceso a este modelo.
* El grupo de acceso "Profesor" solo tiene permisos de lectura, mientras que el grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."

4. unam.teacher.subject --> Modelo para asignación de materias a los profesores. 

* Se creó un campo m2o para que el usuario pueda seleccionar las materias que desea asignar al profesor. Esta relacion esta formada con el modelo unam.subject
* El grupo de acceso "Profesor" solo tiene permisos de lectura, mientras que el grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."

5. unam.interval.time --> Modelo para registro de intervalos de tiempo. 

* Se creó este modelo con la finalidad de que el usuario sea quien cree y modifique de forma dinámica los distintos períodos de duración de cada curso, de este modo evitamos realizar ajustes en el código para agregar o modificar posibles períodos de tiempo que no hayan sido contemplados desde un principio.
* La configuración es sencilla, en total existen dos campos:
  - interval_number de tipo entero para definir un numero fijo que indique la duración.
  - interval_type de tipo selection para definir el intervalo de tiempo que puede ser (Horas, Días, Semanas, Meses o Años)
* El grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."

6. unam.course --> Modelo para registro y gestion de cursos

* Se utilizó el mecanismo de herencia delegada hacia product.template, de modo que cada vez que se crea un nuevo curso tambien se crea un producto de forma automática, a su vez que se garantiza el uso de todos los campos y métodos disponibles en el modelo padre.
* Se extendió el método default_get para garantizar el valor "Consumible" cuando se cree un nuevo producto de forma automática.
* Se creo un campo m2o para asociar el tiempo de duración del curso. Esta relacion esta formada con el modelo unam.interval.time.
* Tambien se agregó un campo para indicar la fecha de incio del curso y otro campo para definir la cantidad máxima de alumnos que podrán tomar el curso.
* Se creó un campo o2m para asociar todas las materias y seleccionar el profesor que estará encargado de dictarla. Esta relacion esta formada con el modelo unam.course.teacher.subject
* El grupo de acceso "Profesor" solo tiene permisos de lectura, mientras que el grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."

7. unam.course.teacher.subject --> Modelo para asignar materias y profesores a los cursos. 

* Se creó un campo m2o para que el usuario pueda seleccionar las materias que desea asignar al curso. Esta relacion esta formada con el modelo unam.subject
* Se creó un campo m2o para que el usuario pueda seleccionar el profesor que va a dictar la materia en el curso. Esta relacion esta formada con el modelo unam.teacher
* El grupo de acceso "Profesor" solo tiene permisos de lectura, mientras que el grupo de acceso "Coordinador" tiene permisos de lectura, creación y modificacion pero no de eliminación. El único grupo con total acceso y control de los datos es el grupo "Administrador."