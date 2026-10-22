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
### Práctica 4


## Parte 6. Análisis de un problema técnico hipotético

| Elemento                                               | Respuesta del equipo                                                                                                                                                                   |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problema identificado**                              | El programa muestra los dispositivos disponibles, pero no encuentra un dispositivo cuando se busca por su nombre.                                                                      |
| **Palabras clave para realizar la búsqueda**           | Python, buscar dispositivo por nombre, comparación de cadenas, diccionarios, listas y manejo de errores.                                                                               |
| **Documentación o comunidad que consultarían primero** | La documentación oficial de Python: https://docs.python.org/3/                                                                                                                         |
| **Información que revisarían en el código**            | Revisaría la función de búsqueda, las variables que almacenan los nombres, las condiciones `if` y la forma en que se comparan los nombres ingresados con los dispositivos disponibles. |
| **Tipo de ejemplo o solución que buscarían**           | Un ejemplo de Python que recorra una lista o diccionario de dispositivos y compare el nombre solicitado con los nombres registrados.                                                   |
| **Cómo comprobarían que la solución funciona**         | Ejecutaría el programa buscando R1 y R2, después probaría con un nombre inexistente para comprobar que el programa responda correctamente en ambos casos.                              |
| **Cómo documentarían la solución encontrada**          | Registraría el problema, la causa identificada, los cambios realizados y las pruebas efectuadas, incluyendo capturas de pantalla de los resultados.                                    |


**Práctica 4**

Exploración de comunidades, documentación y recursos de colaboración

**Estado:** Completada.

Se investigaron y consultaron fuentes de documentación oficial y recursos de aprendizaje relacionados con Python, GNS3 y la automatización de redes.

Se exploraron comunidades técnicas, foros y sitios especializados para identificar soluciones, ejemplos de configuración y buenas prácticas aplicables al desarrollo del proyecto.

Se recopilaron enlaces, tutoriales y materiales de referencia que servirán como apoyo para la programación en Python y la implementación de escenarios de red en GNS3.

**Próximo paso:**
 Continuar con el desarrollo de programas en Python, aplicando los conocimientos adquiridos y utilizando la documentación y los recursos consultados para resolver problemas durante la implementación y pruebas del proyecto integrador.
