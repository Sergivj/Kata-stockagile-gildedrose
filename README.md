# Kata-stockagile-gildedrose 

## Introducción
Este repositorio engloba la kata de Gilded Rose, hecha por Sergi Villa para StockAgile.

_[v2] He decidido ir un paso más allá y completar la kata usando arquitectura hexagonal._

## Objetivo
El objetivo era implementar una nueva funcionalidad en el sistema de Gilded Rose, que permitiera gestionar los artículos conjurados.

Los requerimientos que he seguido son los del siguiente enlace: https://github.com/Sergivj/Kata-stockagile-gildedrose/blob/main/requeriments-gildedrose-es.md

## Refactorización de código
He decidido reestructurar el código por una simple razón: A primera vista, el método que había que modificar era el updateQuality, pero al analizarlo, se veía que el código estaba muy acoplado, y que no era fácil de modificar. Por ello, he decidido refactorizar el código, para que sea más fácil de modificar.

Mi primera idea fue crear una clase por cada uno de los tipos de artículos, y que cada una de ellas tuviera su propio método updateQuality, sobreescribiendo el original. Pero al analizar los requerimientos me di cuenta que la clase padre que tenía que utilizar (Item) no era modificable, por lo tanto me iba a dificultar bastante la implementación.

Entonces, he decidido usar métodos estáticos por cada uno de los diferentes tipos de artículos, y que cada uno de ellos modificase su item correspondiente.

_[v2] He decidido implementar la arquitectura hexagonal, y he creado las capas correspondientes:_ 

_- Aplicación: Aquí se encuentra la clase principal, que es la que se encarga de ejecutar el programa y las excepciones custom que he podido identificar._

_- Dominio: Aquí se encuentra la clase Item, que es la que se encarga de representar los artículos y la clase Inventory, que es la que se encarga de gestionar los artículos._

_- Infraestructura: Aquí se encuentra la clase que se encarga de leer el archivo de texto y de escribir en el archivo de texto, asi como los métodos de salida por pantalla y el archivo de entrada propuesto._
## Nuevo requisito: Artículos conjurados (Conjured)
Para implementar este nuevo requisito, he decidido crear un método estático que se encargue de modificar el item que le pasemos por parámetro. Este método se llama "conjured", y se encarga de modificar el item que le pasemos por parámetro degradando el objeto el doble de rápido en comparación a un item normal.

_[v2.5] Se ha implementado un punto en el que hasta ahora no habíamos contemplado.
Los artículos conjurados, se degradan (y doy por supuesto que también incrementan) al doble de velocidad que los normales, pero si resulta ser un artículo conjurado y a la vez (por ejemplo) de tipo Backstage o Sulfuras, ¿que pasaría?
La última implementación realizada permite que un artículo conjurado y que no sea regular se incremente o degrade al doble de velocidad que un artículo que el mismo tipo designado
Por ejemplo: Si un artículo "Aged Brie" incrementa en 1 su quality cuando aún no se ha vendido, si fuese un artículo "Conjured Aged Brie" incrementaría en 2 su quality mientras no se haya vendido._
## Pruebas
He creado una clase de pruebas para cada uno de los tipos de artículos, y he creado varios métodos de prueba para cada uno de los casos que se especifican en los requerimientos utilizando el lenguaje Given-When-Then.

_[v2] Ahora también he creado tests correspondientes a las excepciones que podemos encontrarnos_
