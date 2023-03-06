# Kata-stockagile-gildedrose

## Introducción
Este repositorio engloba la kata de Gilded Rose, hecha por Sergi Villa para StockAgile.

## Objetivo
El objetivo era implementar una nueva funcionalidad en el sistema de Gilded Rose, que permitiera gestionar los artículos conjurados.

Los requerimientos que he seguido son los del siguiente enlace: https://github.com/Sergivj/Kata-stockagile-gildedrose/blob/main/requeriments-gildedrose-es.md

## Refactorización de código
He decidido reestructurar el código por una simple razón: A primera vista, el método que había que modificar era el updateQuality, pero al analizarlo, se veía que el código estaba muy acoplado, y que no era fácil de modificar. Por ello, he decidido refactorizar el código, para que sea más fácil de modificar.

Mi primera idea fue crear una clase por cada uno de los tipos de artículos, y que cada una de ellas tuviera su propio método updateQuality, sobreescribiendo el original. Pero al analizar los requerimientos me di cuenta que la clase padre que tenía que utilizar (Item) no era modificable, por lo tanto me iba a dificultar bastante la implementación.

Entonces, he decidido usar métodos estáticos por cada uno de los diferentes tipos de artículos, y que cada uno de ellos modificase su item correspondiente.

## Nuevo requisito: Artículos conjurados (Conjured)
Para implementar este nuevo requisito, he decidido crear un método estático que se encargue de modificar el item que le pasemos por parámetro. Este método se llama "conjured", y se encarga de modificar el item que le pasemos por parámetro degradando el objeto el doble de rápido en comparación a un item normal.

## Pruebas
He creado una clase de pruebas para cada uno de los tipos de artículos, y he creado varios métodos de prueba para cada uno de los casos que se especifican en los requerimientos utilizando el lenguaje Given-When-Then.