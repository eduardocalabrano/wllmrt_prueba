# Prueba Full Stack Developer - Wallmart

Aplicativo web que contiene un buscador y una sección de resultados que muestra productos almacenados en una base de datos MongoDB.

## Puntos a considerar

* Cuando se realiza la búsqueda de un producto debe considerarse lo siguiente:
    * Si la búsqueda es sobre un identificador, se deberá retornar el producto exacto
    * Si la búsqueda es de marca o descripción, basta con que la búsqueda sea de más de 3 caracteres y que estos estén incluidos en los campos antes mencionados.
    * Si el número o palabra a buscar es un palíndromo se deberá aplicar un descuento del 50% al precio del producto cuando se liste en la sección de resultados.
