# Práctica 02 - Construcción de la red simulada en GNS3

## Descripción de la práctica

En esta práctica se construyó y configuró una infraestructura de red virtual utilizando GNS3, con el propósito de conocer mejor el entorno de trabajo del simulador y poner en funcionamiento diferentes dispositivos de red.

La práctica permitió trabajar con computadoras virtuales, switches y routers, además de realizar configuraciones básicas de direccionamiento IP, pruebas de conectividad y configuración del protocolo de enrutamiento OSPF.

La infraestructura creada servirá como laboratorio base para las siguientes prácticas de automatización de redes.

---

## Objetivo

Construir, configurar y probar diferentes topologías de red en GNS3, verificando la comunicación entre los dispositivos y preparando una infraestructura que posteriormente pueda ser utilizada para ejecutar scripts de automatización.

---

## Topología 1 - Red básica PC-Switch-PC

La primera topología está formada por:

- 2 computadoras virtuales VPCS.
- 1 Ethernet Switch.
- Enlaces entre ambas computadoras a través del switch.

### Direccionamiento IP

| Dispositivo | Dirección IP | Máscara |
|---|---|---|
| PC1 | 10.1.1.1 | 255.255.255.0 |
| PC2 | 10.1.1.2 | 255.255.255.0 |

Después de configurar las direcciones IP, se realizaron pruebas mediante el comando `ping` desde PC1 hacia PC2 y desde PC2 hacia PC1.

Estas pruebas permitieron comprobar que ambos dispositivos tenían comunicación correctamente dentro de la red.

---

## Topología 2 - Routers y Switch Multicapa

La segunda topología fue creada utilizando:

- Router R1.
- Router R2.
- Switch multicapa S1.

Los dispositivos fueron conectados y configurados para permitir la comunicación entre ellos.

### Direccionamiento principal

| Dispositivo | Interfaz | Dirección IP |
|---|---|---|
| R1 | Gi0/0 | 10.1.1.1/24 |
| R1 | Loopback0 | 1.1.1.1/32 |
| R2 | Gi0/0 | 10.1.1.2/24 |
| R2 | Loopback0 | 2.2.2.2/32 |
| S1 | VLAN 1 | 10.1.1.3/24 |

---

## Configuración realizada

Durante el desarrollo de la práctica se realizaron las siguientes configuraciones:

- Asignación de nombres a los dispositivos.
- Configuración de direcciones IP.
- Activación de interfaces con `no shutdown`.
- Configuración de interfaces Loopback.
- Configuración del switch multicapa.
- Configuración del protocolo OSPF.
- Guardado de las configuraciones.
- Verificación del estado de las interfaces.
- Pruebas de conectividad mediante `ping`.
- Verificación de vecinos OSPF.
- Revisión de la tabla de enrutamiento.

---

## Protocolo OSPF

En los routers R1 y R2 se configuró OSPF como protocolo de enrutamiento.

Posteriormente se utilizó el comando:

`show ip ospf neighbor`

para verificar que los routers hubieran establecido correctamente la relación de vecinos.

También se utilizó:

`show ip route`

para revisar las redes conectadas y las rutas aprendidas mediante OSPF.

---

## Pruebas realizadas

Se realizaron diferentes pruebas para comprobar el funcionamiento de la infraestructura:

- Ping de R1 hacia R2.
- Ping de R2 hacia R1.
- Verificación del estado de las interfaces.
- Verificación del vecino OSPF.
- Revisión de la tabla de enrutamiento.
- Comprobación de conectividad entre PC1 y PC2.

Los resultados permitieron comprobar que los dispositivos estaban correctamente configurados y que existía comunicación entre ellos.

---

## Evidencias

Las evidencias de la práctica se encuentran organizadas dentro de las siguientes carpetas:

### Topología 1

`topologia-01/evidencias/`

Contiene evidencias de:

- Servidores de GNS3.
- Topología completa.
- Configuración de PC1.
- Configuración de PC2.
- Ping de PC1 hacia PC2.
- Ping de PC2 hacia PC1.

### Topología 2

`topologia-02/evidencias/`

Contiene evidencias de:

- Topología completa.
- Configuración de R1.
- Configuración de R2.
- Configuración de S1.
- Ping entre R1 y R2.
- Verificación de vecinos OSPF.
- Tabla de enrutamiento.

---

## Relación con el proyecto integrador

La infraestructura creada en esta práctica servirá como un laboratorio virtual para las siguientes actividades de la asignatura.

Sobre esta red será posible desarrollar y probar scripts que permitan automatizar tareas como:

- Consultar información de los dispositivos.
- Obtener el estado de interfaces.
- Consultar direcciones IP.
- Ejecutar comandos automáticamente.
- Modificar configuraciones.
- Realizar pruebas de conectividad.
- Automatizar tareas de administración de red.

De esta manera, las pruebas pueden realizarse primero en un entorno virtual antes de trabajar con dispositivos de red reales.


Conclusión

Esta práctica permitió conocer de manera más completa el funcionamiento de GNS3 y la forma en que se pueden construir redes virtuales utilizando diferentes dispositivos.

Con la primera topología se comprendió el funcionamiento de una red básica entre computadoras y un switch, mientras que con la segunda topología se trabajó con routers, un switch multicapa y el protocolo OSPF.

Las pruebas de conectividad y los comandos de verificación permitieron comprobar que las configuraciones realizadas funcionaban correctamente.

La infraestructura desarrollada también será importante para las siguientes prácticas, ya que permitirá utilizar scripts y herramientas de automatización sobre una red simulada antes de aplicar los cambios en dispositivos reales.

