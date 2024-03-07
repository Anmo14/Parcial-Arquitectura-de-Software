# Parcial-Arquitectura-de-Software
En una era donde la tecnología redefine constantemente las expectativas de los consumidores, una empresa emergente visionaria se embarcó en una misión para revolucionar la forma en que las personas interactúan con y aprovechan sus múltiples beneficios financieros y de servicios. Inspirados por la complejidad que enfrentaban los usuarios al gestionar sus beneficios dispersos en seguros, tarjetas de crédito, y programas de fidelización, el equipo se propuso construir un sistema unificado que no solo centralizara estos beneficios en una sola plataforma, sino que también orientara a los usuarios hacia la maximización de su valor en cada compra. Este sistema integrado de beneficios se convirtió en la piedra angular de su visión, prometiendo una interfaz intuitiva respaldada por una arquitectura robusta y un motor de recomendaciones inteligente.

Al abordar el diseño del sistema, la elección de una arquitectura de microservicios emergió como la solución óptima, promoviendo la flexibilidad, la escalabilidad y la facilidad de integración con sistemas externos. Esta arquitectura facilitaría la actualización y expansión continuas del sistema, permitiendo al equipo añadir nuevos proveedores de beneficios o actualizar los existentes sin interrupciones significativas.

Por otra parte, la identificación de los requerimientos críticos, equilibrando cuidadosamente las necesidades funcionales, como la integración transparente con diversos proveedores de beneficios y un sistema de recomendaciones altamente personalizado, con imperativos no funcionales como seguridad de datos, escalabilidad y disponibilidad. La meta es crear un sistema que no solo respondiera a las necesidades actuales de los usuarios, sino que también pudiera adaptarse a las demandas futuras.

La presentación clara de los beneficios disponibles, junto con una retroalimentación inmediata y relevante sobre las recomendaciones de beneficios, se convirtió en una prioridad para asegurar que los usuarios pudieran tomar decisiones informadas con facilidad. Así mismo, con los cimientos tecnológicos en su lugar, la experiencia del usuario debe ser visualmente atractiva y accesible en una variedad de dispositivos, si no que también proporcionara una interacción intuitiva con el sistema.

La implementación del sistema debe seguir los principios SOLID para asegurar un código mantenible y extensible. Cada microservicio debe ser construido con un propósito específico, desde gestionar la autenticación de usuarios hasta procesar complejas recomendaciones de beneficios. La seguridad fue debe estar en cada etapa empleando las mejores prácticas para proteger la información personal y financiera de los usuarios.

### Responsabilidad Única (SRP - Single Responsibility Principle) 

Este principio establece que una clase debe tener una única razón para cambiar, es decir, cada clase debe tener una sola responsabilidad dentro del sistema.

En el programa proporcionado, cada clase tiene una responsabilidad única y claramente definida:

* Cliente_usuario: Responsable de representar a un cliente del sistema y gestionar sus beneficios.
* Cuenta_cliente: Responsable de representar una cuenta bancaria asociada a un cliente y gestionar sus transacciones.
* Transaccion_cliente: Responsable de representar una transacción realizada en una cuenta bancaria.
* Proveedor_Beneficio: Responsable de representar a un proveedor de beneficios y gestionar los beneficios que ofrece.
* Beneficio: Responsable de representar un beneficio ofrecido por un proveedor.
* Autenticacion: Responsable de manejar la autenticación de un cliente.
* Recomendacion_beneficios: Responsable de gestionar las recomendaciones de beneficios para un cliente.

## Abierto/Cerrado (OCP):

Establece que las clases deben estar abiertas para la extensión pero cerradas para la modificación. Esto significa que deberíamos poder agregar nuevas funcionalidades al sistema sin necesidad de cambiar el código existente. 

* En el programa proporcionado, esto se refleja en la capacidad de añadir nuevas clases para extender la funcionalidad del sistema sin tener que alterar las clases existentes, como Cliente_usuario o Cuenta_cliente. Esto facilita la adaptación del sistema a nuevos requisitos o cambios sin afectar el funcionamiento de las partes existentes del sistema.

###  Principio de Sustitución de Liskov (LSP - Liskov Substitution Principle)

Este principio establece que los objetos de un programa deben ser reemplazables por instancias de sus subtipos sin alterar la corrección del programa.
* De esta manera, las subclases pueden ser utilizadas sin alterar el comportamiento de las clases en el programa.

### Principio de Segregación de la Interfaz
se puede aplicar al diseñar las clases y sus interfaces donde el usuario no acceda a metodos innecesarios.
* Supongamos que tenemos una interfaz ServicioCliente que contiene métodos para administrar clientes, incluyendo la creación, actualización y eliminación de clientes. Si hay una clase que solo necesita la funcionalidad de creación de clientes y no la de actualización o eliminación, sería preferible tener una interfaz separada solo para la creación de clientes.

### Principio de Inversión de Dependencia (Dependency Inversion Principle - DIP) Este principio establece dos conceptos fundamentales:

* Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.
* Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones.

* En el codigo proporcionado, en lugar de que las clases dependan directamente de implementaciones concretas, dependen de abstracciones. Por ejemplo, la clase Recomendacion_beneficios depende de la lista de beneficios recomendados, que es una abstracción que puede ser proporcionada por diferentes fuentes o generadores de recomendaciones.

![diagrama de clases](https://github.com/Anmo14/Parcial-Arquitectura-de-Software/assets/148002480/5613d52b-27a7-4365-9e99-01a632101ccf)
