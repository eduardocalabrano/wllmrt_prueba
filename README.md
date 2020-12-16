# Prueba Full Stack Developer - Wallmart

Aplicativo web que contiene un buscador y una sección de resultados que muestra productos almacenados en una base de datos MongoDB.

##Demo

[Link Heroku](https://ancient-bayou-17381.herokuapp.com/)

[Github Heroku](https://git.heroku.com/ancient-bayou-17381.git)

[Github Personal](https://github.com/eduardocalabrano/wllmrt_prueba)

## Puntos a considerar

* Cuando se realiza la búsqueda de un producto debe considerarse lo siguiente:
    * Si la búsqueda es sobre un identificador, se deberá retornar el producto exacto
    * Si la búsqueda es de marca o descripción, basta con que la búsqueda sea de más de 3 caracteres y que estos estén incluidos en los campos antes mencionados.
    * Si el número o palabra a buscar es un palíndromo se deberá aplicar un descuento del 50% al precio del producto cuando se liste en la sección de resultados.

## Pruebas

Solo hay tres pruebas y se ejecutan con la linea de comandos "pytest"

## Capturas

![](https://i.postimg.cc/Z5wXy0Vd/wall1.png)
![](https://i.postimg.cc/ydcfnNXn/wall2.png)
![](https://i.postimg.cc/wTHrfDrN/wall3.png)
