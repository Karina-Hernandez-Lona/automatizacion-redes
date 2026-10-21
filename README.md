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

### Practica 4 -Estado: Completada.

## 1. Propósito de la práctica
El propósito de esta práctica es investigar y analizar recursos técnicos y comunidades relacionados con Python, redes y automatización. Se busca conocer herramientas que ayuden a resolver problemas de programación, aprender sobre la administración de dispositivos de red e identificar fuentes confiables para consultar información. También se pretende desarrollar habilidades de investigación, colaboración y documentación mediante la organización de los resultados en el repositorio de GitHub del proyecto integrador.

## 2. Relación con el proyecto integrador
En la práctica anterior se desarrolló el programa dispositivos.py en Python para representar, organizar y manipular información básica de dispositivos de red, como routers y switches, pertenecientes a la topología simulada en GNS3 durante la Práctica 2.

La presente práctica da continuidad a ese trabajo al investigar recursos que pueden ayudar a corregir errores, mejorar el código y aprender nuevas técnicas de automatización. Cisco DevNet y Network to Code ofrecen información relacionada con la automatización de redes; GitHub permite organizar el código y documentar los avances; Stack Overflow y The Python Community facilitan la consulta de dudas, y Red Hat Ansible Automation Platform permite conocer herramientas para automatizar tareas de infraestructura. Estos conocimientos servirán como apoyo para las siguientes etapas del proyecto.

## 3. Aprendizajes obtenidos
Durante esta práctica aprendimos que existen diferentes recursos para investigar, desarrollar y mejorar programas relacionados con Python y las redes. Cisco DevNet ofrece materiales para aprender automatización de redes, mientras que Network to Code permite conocer herramientas para organizar información y automatizar procesos de infraestructura. También comprendimos que GitHub no solo sirve para guardar código, sino que permite organizar la documentación, conservar el historial de cambios y colaborar con otros integrantes. Por su parte, Stack Overflow y The Python Community ofrecen espacios para investigar dudas, comparar soluciones y aprender de las experiencias de otros programadores. Además, conocimos la utilidad de Red Hat Ansible Automation Platform para automatizar tareas de administración de infraestructura y redes. Aprendimos que es importante verificar la procedencia, actualidad, compatibilidad y utilidad de la información antes de aplicar una solución. Finalmente, estos recursos nos ayudarán a continuar desarrollando dispositivos.py, investigar errores de programación y prepararnos para futuras actividades de automatización. Mantener los hallazgos organizados en GitHub facilitará el trabajo colaborativo y permitirá construir una base de conocimiento útil para el proyecto integrador.

