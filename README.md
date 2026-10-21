# automatizacion-redes
Proyecto de automatización de redes y documentación de prácticas

## Avance del proyecto integrador

### Práctica 1
Preparación de la estación de automatización de redes.  
**Estado:** Completada.

### Práctica 2
Construcción de la red simulada en GNS3.  
**Estado:** Completada.

### Infraestructura construida

- Topología básica PC-Switch-PC.
- Topología con dos routers y un switch multicapa.
- Direccionamiento IP.
- Conectividad entre dispositivos.
- Protocolo OSPF.
- Verificación de tablas de enrutamiento.

### Próximo paso

Desarrollo de scripts y herramientas para automatizar tareas sobre la infraestructura de red.

---

## Conclusión

Esta práctica permitió conocer de manera más completa el funcionamiento de GNS3 y la forma en que se pueden construir y configurar redes virtuales utilizando diferentes dispositivos.

En la primera topología se trabajó con una red básica formada por dos computadoras y un switch, configurando direcciones IP y realizando pruebas de conectividad. En la segunda topología se utilizaron dos routers y un switch multicapa, además de realizar la configuración del protocolo OSPF.

Mediante las pruebas de conectividad y los comandos de verificación fue posible comprobar el correcto funcionamiento de los dispositivos y observar la información de las interfaces, los vecinos OSPF y las tablas de enrutamiento.

La infraestructura desarrollada servirá como base para las siguientes prácticas, en las cuales se podrán utilizar scripts y herramientas para automatizar tareas de administración y configuración de redes.

---

## Estado de la práctica

**Práctica 02: Completada.**


# Práctica 3: Primer programa de Python para representar información de dispositivos

## 1. Propósito
En esta práctica se desarrolló un programa en Python (`dispositivos.py`) para representar, organizar y manipular datos básicos de dispositivos de red (como Routers y Switches) pertenecientes a la topología simulada en GNS3 de la Práctica 2, como paso previo a la automatización con librerías externas.

---

## 2. Conceptos Utilizados
* **Variables:** Almacenan valores individuales como el nombre o la dirección IP de un dispositivo.
* **Tipos de datos:** Cadenas de texto (`string`) para nombres e IPs, y estados operativos.
* **`print()`:** Función para mostrar la información formateada en consola.
* **Diccionarios (`dict`):** Estructura clave-valor para agrupar las propiedades de un solo dispositivo de red.
* **Listas (`list`):** Colección ordenada de diccionarios para representar toda la infraestructura.
* **Ciclo `for`:** Recorre automáticamente cada dispositivo dentro de la lista para procesarlo.
* **Condicional `if`:** Evalúa condiciones (p. ej., verificar si un dispositivo está "Activo").
* **Funciones (`def`):** Bloques de código reutilizables para modularizar la impresión y búsqueda de datos.

---

## 3. Dispositivos Representados

| Dispositivo | Tipo | Dirección IP | Estado | Función |
| :--- | :--- | :--- | :--- | :--- |
| R1 | Router | 10.1.1.1 | Activo | Enrutamiento |
| R2 | Router | 10.1.1.2 | Activo | Enrutamiento |
| S1 | Switch | 10.1.1.3 | Activo | Conectividad |

---

## 4. Preguntas de Análisis y Respuestas

### 1. ¿Por qué es útil representar la información de los dispositivos mediante un programa?
Porque permite organizar, almacenar y consultar la información de los dispositivos de forma rápida, sencilla y estructurada, sirviendo como base para futuras tareas de automatización de redes.

### 2. ¿Qué ventaja ofrece utilizar un diccionario para representar un dispositivo?
Permite agrupar todos los datos relacionados con un dispositivo en una sola estructura utilizando parejas de clave-valor, lo que facilita el acceso y modificación de sus atributos específicos.

### 3. ¿Qué ventaja ofrece utilizar una lista para representar varios dispositivos?
Permite almacenar múltiples dispositivos en una misma estructura ordenada, facilitando recorrerlos, procesarlos y administrarlos en conjunto mediante ciclos y funciones.

### 4. ¿Qué tarea permite realizar el ciclo `for`?
Recorrer automáticamente cada uno de los elementos de la lista y ejecutar un bloque de acciones determinado sin necesidad de duplicar código.

### 5. ¿Para qué se utilizó la estructura `if`?
Para evaluar condiciones, como verificar si el estado del dispositivo es "Activo" o "Fuera de servicio" y mostrar avisos distintos según la condición.

### 6. ¿Qué ventaja tiene utilizar una función?
Permite reutilizar código, mejorar la organización del programa, facilitar su mantenimiento y evitar repetir las mismas instrucciones de impresión.

### 7. ¿Qué información de los dispositivos podría obtener automáticamente un programa en una etapa posterior?
Direcciones IP, nombres, estado operativo, uso de CPU/memoria, versión del sistema operativo, interfaces activas, rutas configuradas y estadísticas de tráfico.

### 8. ¿Qué diferencia existe entre representar información de un dispositivo y obtener esa información directamente desde el dispositivo?
Representar información implica usar datos estáticos definidos manualmente en el código. Obtener información directamente implica conectarse al equipo real a través de la red para consultar datos dinámicos y en tiempo real.

### 9. ¿Cómo podría evolucionar este programa para convertirse en una herramienta de automatización de redes?
Incorporando librerías de automatización como Netmiko, Paramiko o NAPALM para realizar conexiones SSH automáticas, ejecutar comandos, recopilar información en tiempo real y aplicar configuraciones masivas.

### 10. ¿Qué relación existe entre esta práctica, la Práctica 2 y las siguientes prácticas del proyecto integrador?
La Práctica 2 definió la topología física/simulada en GNS3. La Práctica 3 representa dicha topología en código de Python. Las prácticas futuras utilizarán este modelo para interactuar directamente con los dispositivos simulados.

---

## 5. Evidencias
* Capturas de pantalla de la ejecución del programa y de la estructura del código en Visual Studio Code.

---

## 6. Problemas y Soluciones

| Problema | Causa | Solución |
| :--- | :--- | :--- |
| Dificultad con la ejecución de GNS3 en algunas laptops | Limitaciones de rendimiento en equipos individuales | Se colaboró en equipo dentro del aula para completar las pruebas |
| Errores de sintaxis al estructurar diccionarios o ciclos | Olvido temporal de la sintaxis de Python | Se revisaron ejemplos previos y apuntes para corregir la estructura |

---

## 7. Conclusión
Durante esta práctica se reforzaron conceptos clave de programación en Python como listas, diccionarios, estructuras condicionales y ciclos aplicados al entorno de redes. Aunque todavía no se realiza una conexión directa con los equipos de GNS3, este programa sienta las bases lógicas necesarias para que en las siguientes etapas del proyecto integrador se puedan automatizar tareas de consulta, monitoreo y configuración de dispositivos de red de manera eficiente.


# Practica 4: Exploración de comunidades, documentación y recursos de colaboración. 

## 1.	Propósito de la práctica.
El propósito de esta práctica es investigar y analizar diferentes recursos de documentación, herramientas técnicas y comunidades de colaboración relacionadas con Python, GNS3 y la automatización de redes. Se busca aprender a identificar fuentes confiables, consultar información para resolver dudas de programación y conocer buenas prácticas para solicitar ayuda en comunidades. También se pretende organizar los conocimientos obtenidos en el repositorio de GitHub para facilitar su consulta y utilizarlos en las siguientes etapas del proyecto integrador.

## 2.	Relación con el proyecto integrador.
Esta práctica da continuidad al proyecto porque permite identificar documentación y bibliotecas que pueden utilizarse para mejorar el programa y avanzar hacia la automatización de redes. Además, el análisis de comunidades como Stack Overflow y el uso de GitHub ayudarán al equipo a investigar errores, compartir soluciones y mantener organizada la información técnica necesaria para las próximas prácticas.

## 3.	Recursos consultados: síntesis y enlaces.

## 4.	Evaluación de confiabilidad: tabla comparativa.

## 5.	Estrategia de solución del problema: situación hipotética de búsqueda.
- Problema planteado: el programa dispositivos.py muestra correctamente la información de R1 y R2, pero no identifica un dispositivo cuando se busca por su nombre.
- Problema identificado: El programa no encuentra un dispositivo al buscarlo por su nombre, aunque la                        información de R1 y R2 se muestra correctamente.
- Palabras clave para realizar la búsqueda: Python buscar dispositivo por nombre, diccionarios, listas, comparación de         cadenas y búsqueda de elementos.
- Documentación que consultaríamos primero: Primero consultaríamos la documentación oficial de Python sobre listas, diccionarios y estructuras de control. Después revisaríamos Stack Overflow en español si fuera necesario.
- Información que revisaríamos en el código:	La estructura donde se guardan los dispositivos, los nombres registrados, las condiciones de búsqueda y la forma en que se compara el nombre ingresado.
- Tipo de ejemplo o solución que buscaríamos:	Un ejemplo de una función en Python que recorra una lista o consulte un diccionario para localizar un dispositivo por su nombre.
- Cómo comprobaríamos que la solución funciona:	Probaríamos la búsqueda de R1 y R2, un nombre inexistente y un nombre con diferencias de mayúsculas o minúsculas, según el comportamiento esperado.
- Cómo documentaríamos la solución encontrada:	Registraríamos el problema, la causa identificada, la solución aplicada, las pruebas realizadas y los enlaces consultados en el README de la práctica dentro de GitHub.

## 6.	Aprendizajes obtenidos.
Durante esta práctica aprendimos que la documentación oficial y las comunidades de colaboración son recursos importantes para desarrollar programas y resolver problemas técnicos. Comprendimos que la documentación permite conocer el funcionamiento de las herramientas, mientras que las comunidades ayudan a encontrar experiencias y soluciones a problemas similares.
También aprendimos a evaluar la confiabilidad de las fuentes considerando quién las mantiene, si están actualizadas, si contienen ejemplos verificables y si la información puede comprobarse con otras fuentes. Además, identificamos la utilidad de GNS3 para trabajar con topologías de red y de bibliotecas como Netmiko para investigar futuras posibilidades de automatización.
Finalmente, comprendimos la importancia de documentar los hallazgos en GitHub, ya que esto permite mantener organizada la información, compartir conocimientos con el equipo y consultar soluciones en futuras prácticas. Estos aprendizajes servirán para mejorar el programa dispositivos.py y continuar desarrollando el proyecto integrador de automatización de redes.

## 7.	Conclusión individual:

Miranda Rodríguez Castellanos:
En esta práctica aprendí que la documentación oficial ofrece información confiable sobre el uso de Python y sus funciones, mientras que las comunidades permiten conocer experiencias y soluciones de otros programadores. Para saber si un recurso es confiable, es importante revisar quién lo publica, si está actualizado y si incluye ejemplos que se puedan comprobar. Una comunidad como Stack Overflow puede ayudarme a resolver errores de Python al encontrar preguntas similares a las que se presentan durante el desarrollo de un programa. También comprendí que es importante guardar las soluciones encontradas en GitHub para tenerlas organizadas y consultarlas cuando sea necesario. Esto facilita el trabajo en equipo y evita repetir las mismas búsquedas. En las siguientes prácticas utilizaré estos recursos para mejorar mis programas y resolver problemas relacionados con la automatización de redes. Considero que investigar antes de programar permite trabajar de una manera más ordenada y eficiente.

Nahomi Itzel Martínez Rivas:
La realización de esta práctica me permitió conocer la importancia de consultar diferentes fuentes de información para aprender a programar y trabajar con herramientas como GNS3. La documentación oficial explica el funcionamiento de las herramientas, mientras que las comunidades ofrecen recomendaciones y respuestas basadas en problemas reales. Para elegir un recurso confiable, revisaría su autor, la fecha de actualización, la claridad de sus instrucciones y si la información coincide con otras fuentes. Si tuviera un error en Python, podría buscarlo en una comunidad y comparar las posibles soluciones con la documentación oficial antes de aplicarlas. Además, documentar los resultados en GitHub ayuda a conservar los conocimientos adquiridos y compartirlos con los integrantes del equipo. En las próximas prácticas aprovecharé estos recursos para investigar errores, aprender nuevas funciones y mejorar el código del proyecto integrador. Así podré desarrollar soluciones más seguras y comprender mejor lo que estoy realizando.

Karina Hernandez Lona:
Durante esta práctica comprendí que no basta con encontrar una solución en internet, sino que también debemos comprobar que sea correcta y adecuada para nuestro proyecto. La documentación oficial proporciona explicaciones sobre el funcionamiento de Python y otras herramientas, mientras que las comunidades permiten consultar dudas y conocer distintas formas de resolver un problema. Para identificar una fuente confiable, tomaría en cuenta quién la mantiene, si presenta ejemplos claros y si la información corresponde a la versión que utilizamos. Una comunidad puede ayudarme a identificar errores en variables, listas, diccionarios o funciones mediante ejemplos y explicaciones de otros usuarios. Registrar las soluciones en GitHub permite que el equipo tenga una base de conocimientos disponible para futuras consultas. En las siguientes prácticas aplicaré lo aprendido para investigar problemas de programación y automatización de redes con mayor facilidad. Esto contribuirá a mejorar el desarrollo del proyecto y la colaboración entre los integrantes.

Monserratt Guerra Cantu:
Esta práctica me ayudó a reconocer que la investigación es una parte importante del desarrollo de software. La documentación oficial contiene información estructurada sobre las herramientas y sus funciones, mientras que las comunidades permiten intercambiar ideas y encontrar respuestas a problemas específicos. Para evaluar la confiabilidad de un recurso, revisaría su procedencia, actualización, ejemplos y relación con el problema que necesito resolver. Si mi programa de Python no identificara correctamente un dispositivo de red, podría buscar casos similares en Stack Overflow y revisar la documentación para comprobar qué está causando el error. Después de encontrar una solución, la registraría en GitHub para que mis compañeros también puedan consultarla. En las próximas prácticas utilizaré la documentación de Python, GNS3 y las bibliotecas de automatización para mejorar mis conocimientos. De esta manera, podré resolver problemas de forma más organizada y contribuir al avance del proyecto integrador.

Fabiola Rodríguez Rivera:
Al finalizar esta práctica, entendí que contar con recursos técnicos organizados facilita el aprendizaje y la solución de problemas durante un proyecto. La documentación oficial permite conocer las funciones y características de una herramienta, mientras que las comunidades ofrecen apoyo mediante preguntas, respuestas y experiencias compartidas. Para determinar si una fuente es confiable, comprobaría quién la publica, si está actualizada, si sus ejemplos funcionan y si otras fuentes respaldan la información. En caso de tener dificultades con Python, podría consultar una comunidad para encontrar ideas y después verificar la solución antes de utilizarla. También aprendí que documentar los resultados en GitHub es importante porque permite conservar los procedimientos y compartirlos con el equipo. En las próximas prácticas consultaré estos recursos para resolver errores, aprender a utilizar bibliotecas y desarrollar programas relacionados con las redes. Considero que estos conocimientos serán útiles para mejorar la calidad del código y avanzar de manera colaborativa.

