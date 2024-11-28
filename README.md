# Desarrollo-de-aplicaciones-web-con-Django

M6S4
REBOUND EXERCISE: CREACIÓN DE PÁGINA DE INICIO AGREGANDO RUTA A UN PROYECTO
Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE: Diseño 
Responsivo.
EJERCICIO:
Crear una página de bienvenida, por medio de un HttpResponse.
Procedimiento:
1. Agregar al proyecto site_django una URL que incluya las URLs de la aplicación book, creada en la 
práctica anterior con el siguiente path: http://localhost:8000/book/.
2. Crear una vista que retorne, por medio del método HttpResponse, el mensaje “Bienvenidos a mi 
sitio de libros”.
3. Agregar que la ruta principal de book haga referencia al index, previamente creado en la URL de 
book.
4. ¿Qué observas en la ruta http://localhost:8000/?         Una página de error 404 Not Found indicando que no hay una URL asociada.
5. ¿Qué observas en la ruta http://localhost:8000/book/     El mensaje: "Bienvenidos a mi sitio de libros", ya que esta ruta está asociada con
                                                            la vista index en la aplicación book.

M6S5
REBOUND EXERCISE: VERIFICANDO UN PALÍNDROMO
Para resolver este ejercicio, anteriormente debe haber revisado la lectura y los videos del CUE: Despliegue 
de páginas con contenido dinámico.
EJERCICIO:
Se desea verificar si una palabra enviada por parámetros en la URL es un palíndromo. Una palabra o frase 
palíndroma es aquella cuyas letras están dispuestas de tal manera que resulta la misma leída de 
izquierda a derecha, que de derecha a izquierda. 
Verifique con las siguientes palabras y frases: yo hago yoga hoy, orejero, rotomotor, entre otras. 