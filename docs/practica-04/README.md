# Practica 4: Exploración de comunidades, documentación y recursos de colaboración.

## 1. Propósito de la práctica
El propósito de esta práctica es investigar y analizar recursos técnicos y comunidades relacionados con Python, redes y automatización. Se busca conocer herramientas que ayuden a resolver problemas de programación, aprender sobre la administración de dispositivos de red e identificar fuentes confiables para consultar información. También se pretende desarrollar habilidades de investigación, colaboración y documentación mediante la organización de los resultados en el repositorio de GitHub del proyecto integrador.

## 2. Relación con el proyecto integrador
En la práctica anterior se desarrolló el programa dispositivos.py en Python para representar, organizar y manipular información básica de dispositivos de red, como routers y switches, pertenecientes a la topología simulada en GNS3 durante la Práctica 2.

La presente práctica da continuidad a ese trabajo al investigar recursos que pueden ayudar a corregir errores, mejorar el código y aprender nuevas técnicas de automatización. Cisco DevNet y Network to Code ofrecen información relacionada con la automatización de redes; GitHub permite organizar el código y documentar los avances; Stack Overflow y The Python Community facilitan la consulta de dudas, y Red Hat Ansible Automation Platform permite conocer herramientas para automatizar tareas de infraestructura. Estos conocimientos servirán como apoyo para las siguientes etapas del proyecto.

## 3. Recursos consultados: síntesis y enlaces
Estos son los seis recursos seleccionados, su utilidad y la forma en que pueden apoyar el proyecto integrador.
1. Cisco DevNet
Enlace: https://developer.cisco.com/site/networking/
Síntesis: Ofrece documentación, ejemplos y laboratorios para aprender sobre programación, APIs y automatización de dispositivos de red Cisco.

2. Network to Code
Enlace: https://docs.nautobot.com/
Síntesis: Proporciona documentación sobre Nautobot, una plataforma para organizar información de dispositivos de red y facilitar la automatización de tareas.

3. GitHub
Enlace: https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories
Síntesis: Explica cómo crear y administrar repositorios para almacenar código, documentar proyectos, controlar cambios y colaborar en equipo.

4. Stack Overflow
Enlace: https://es.stackoverflow.com/
Síntesis: Es una comunidad donde los programadores comparten preguntas y respuestas para resolver errores y dudas relacionadas con Python y otros lenguajes.

5. The Python Community
Enlace: https://www.python.org/community/
Síntesis: Reúne información sobre comunidades, grupos y espacios de colaboración donde los usuarios pueden aprender Python y compartir conocimientos.

6. Red Hat Ansible Automation Platform
Enlace: https://docs.ansible.com/platform.html
Síntesis: Ofrece documentación sobre herramientas para automatizar tareas de infraestructura y administración de redes mediante configuraciones y procesos automatizados.

## 4. Evaluación de confiabilidad: tabla comparativa
Se seleccionaron Cisco DevNet, GitHub y Stack Overflow para evaluar sus características observables y su utilidad para el proyecto.
| Criterio | Cisco DevNet | GitHub | Stack Overflow |
|----------|--------------|--------|----------------|
| ¿Quién publica o mantiene el recurso? | Cisco. | GitHub. | Comunidad de usuarios y colaboradores. |
| ¿La información corresponde al tema investigado? | Sí, se enfoca en programación y automatización de redes. | Sí, explica la administración de repositorios y la colaboración. | Sí, contiene preguntas y respuestas sobre programación. |
| ¿Incluye ejemplos o instrucciones verificables? | Sí, ofrece ejemplos, documentación y laboratorios. | Sí, proporciona guías e instrucciones. | Sí, incluye ejemplos de código y posibles soluciones. |
| ¿Se identifica la versión o fecha de actualización cuando corresponde? | Se debe revisar la versión o fecha del recurso consultado. | La documentación se actualiza; se debe revisar la página específica. | Las publicaciones muestran fechas que ayudan a comprobar su actualidad. |
| ¿Es posible comprobar la información con otra fuente? | Sí, mediante documentación técnica y pruebas. | Sí, mediante pruebas y otras fuentes oficiales. | Sí, comparando las respuestas con documentación oficial. |
| ¿Qué utilidad tiene para el proyecto integrador? | Aprender técnicas de automatización de redes. | Organizar el código y documentar los avances del proyecto. | Encontrar soluciones a errores de Python y dudas de programación. |

## 5. Estrategia de solución del problema: situación hipotética de búsqueda
Problema: el programa dispositivos.py muestra correctamente la información de R1 y R2, pero no identifica un dispositivo cuando se busca por su nombre.

- Problema identificado:	El programa no encuentra un dispositivo mediante su nombre, aunque muestra correctamente la información de R1 y R2.
- Palabras clave para realizar la búsqueda:	Python buscar dispositivo por nombre, búsqueda en listas y diccionarios, comparación de cadenas y funciones de búsqueda.
- Documentación o comunidad que consultaríamos primero:	Primero revisaríamos la documentación oficial de Python y después buscaríamos preguntas similares en Stack Overflow.
- Información que revisaríamos en el código:	La estructura donde se almacenan los dispositivos, los nombres registrados, la función de búsqueda y las condiciones utilizadas para comparar los nombres.
- Tipo de ejemplo o solución que buscaríamos:	Una función de Python que permita recorrer una lista o consultar un diccionario para encontrar un dispositivo por su nombre.
- Cómo comprobaríamos que la solución funciona:	Probaríamos la búsqueda de R1 y R2, un nombre inexistente y nombres con mayúsculas o minúsculas diferentes para comprobar el comportamiento esperado.
- Cómo documentaríamos la solución encontrada:	Registraríamos el problema, la causa, la solución, las pruebas realizadas y los enlaces consultados en el README de la práctica dentro de GitHub.

## 6. Aprendizajes obtenidos
Durante esta práctica aprendimos que existen diferentes recursos para investigar, desarrollar y mejorar programas relacionados con Python y las redes. Cisco DevNet ofrece materiales para aprender automatización de redes, mientras que Network to Code permite conocer herramientas para organizar información y automatizar procesos de infraestructura.
También comprendimos que GitHub no solo sirve para guardar código, sino que permite organizar la documentación, conservar el historial de cambios y colaborar con otros integrantes. Por su parte, Stack Overflow y The Python Community ofrecen espacios para investigar dudas, comparar soluciones y aprender de las experiencias de otros programadores.
Además, conocimos la utilidad de Red Hat Ansible Automation Platform para automatizar tareas de administración de infraestructura y redes. Aprendimos que es importante verificar la procedencia, actualidad, compatibilidad y utilidad de la información antes de aplicar una solución.
Finalmente, estos recursos nos ayudarán a continuar desarrollando dispositivos.py, investigar errores de programación y prepararnos para futuras actividades de automatización. Mantener los hallazgos organizados en GitHub facilitará el trabajo colaborativo y permitirá construir una base de conocimiento útil para el proyecto integrador.

## 7. Conclusión individual:
Miranda Rodríguez Castellanos: En esta práctica aprendí que la documentación oficial ofrece información confiable sobre el uso de Python y sus funciones, mientras que las comunidades permiten conocer experiencias y soluciones de otros programadores. Para saber si un recurso es confiable, es importante revisar quién lo publica, si está actualizado y si incluye ejemplos que se puedan comprobar. Una comunidad como Stack Overflow puede ayudarme a resolver errores de Python al encontrar preguntas similares a las que se presentan durante el desarrollo de un programa. También comprendí que es importante guardar las soluciones encontradas en GitHub para tenerlas organizadas y consultarlas cuando sea necesario. Esto facilita el trabajo en equipo y evita repetir las mismas búsquedas. En las siguientes prácticas utilizaré estos recursos para mejorar mis programas y resolver problemas relacionados con la automatización de redes. Considero que investigar antes de programar permite trabajar de una manera más ordenada y eficiente.

Nahomi Itzel Martínez Rivas: La realización de esta práctica me permitió conocer la importancia de consultar diferentes fuentes de información para aprender a programar y trabajar con herramientas como GNS3. La documentación oficial explica el funcionamiento de las herramientas, mientras que las comunidades ofrecen recomendaciones y respuestas basadas en problemas reales. Para elegir un recurso confiable, revisaría su autor, la fecha de actualización, la claridad de sus instrucciones y si la información coincide con otras fuentes. Si tuviera un error en Python, podría buscarlo en una comunidad y comparar las posibles soluciones con la documentación oficial antes de aplicarlas. Además, documentar los resultados en GitHub ayuda a conservar los conocimientos adquiridos y compartirlos con los integrantes del equipo. En las próximas prácticas aprovecharé estos recursos para investigar errores, aprender nuevas funciones y mejorar el código del proyecto integrador. Así podré desarrollar soluciones más seguras y comprender mejor lo que estoy realizando.

Karina Hernandez Lona: Durante esta práctica comprendí que no basta con encontrar una solución en internet, sino que también debemos comprobar que sea correcta y adecuada para nuestro proyecto. La documentación oficial proporciona explicaciones sobre el funcionamiento de Python y otras herramientas, mientras que las comunidades permiten consultar dudas y conocer distintas formas de resolver un problema. Para identificar una fuente confiable, tomaría en cuenta quién la mantiene, si presenta ejemplos claros y si la información corresponde a la versión que utilizamos. Una comunidad puede ayudarme a identificar errores en variables, listas, diccionarios o funciones mediante ejemplos y explicaciones de otros usuarios. Registrar las soluciones en GitHub permite que el equipo tenga una base de conocimientos disponible para futuras consultas. En las siguientes prácticas aplicaré lo aprendido para investigar problemas de programación y automatización de redes con mayor facilidad. Esto contribuirá a mejorar el desarrollo del proyecto y la colaboración entre los integrantes.

Monserratt Guerra Cantu: Esta práctica me ayudó a reconocer que la investigación es una parte importante del desarrollo de software. La documentación oficial contiene información estructurada sobre las herramientas y sus funciones, mientras que las comunidades permiten intercambiar ideas y encontrar respuestas a problemas específicos. Para evaluar la confiabilidad de un recurso, revisaría su procedencia, actualización, ejemplos y relación con el problema que necesito resolver. Si mi programa de Python no identificara correctamente un dispositivo de red, podría buscar casos similares en Stack Overflow y revisar la documentación para comprobar qué está causando el error. Después de encontrar una solución, la registraría en GitHub para que mis compañeros también puedan consultarla. En las próximas prácticas utilizaré la documentación de Python, GNS3 y las bibliotecas de automatización para mejorar mis conocimientos. De esta manera, podré resolver problemas de forma más organizada y contribuir al avance del proyecto integrador.

Fabiola Rodríguez Rivera: Al finalizar esta práctica, entendí que contar con recursos técnicos organizados facilita el aprendizaje y la solución de problemas durante un proyecto. La documentación oficial permite conocer las funciones y características de una herramienta, mientras que las comunidades ofrecen apoyo mediante preguntas, respuestas y experiencias compartidas. Para determinar si una fuente es confiable, comprobaría quién la publica, si está actualizada, si sus ejemplos funcionan y si otras fuentes respaldan la información. En caso de tener dificultades con Python, podría consultar una comunidad para encontrar ideas y después verificar la solución antes de utilizarla. También aprendí que documentar los resultados en GitHub es importante porque permite conservar los procedimientos y compartirlos con el equipo. En las próximas prácticas consultaré estos recursos para resolver errores, aprender a utilizar bibliotecas y desarrollar programas relacionados con las redes. Considero que estos conocimientos serán útiles para mejorar la calidad del código y avanzar de manera colaborativa.
