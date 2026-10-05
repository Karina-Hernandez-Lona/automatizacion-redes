# Configuración de la Topología 02

## Descripción

La Topología 02 está formada por dos routers Cisco IOSv y un switch multicapa Cisco IOSvL2.

El objetivo de esta topología fue configurar los dispositivos de red, asignar direcciones IP, habilitar interfaces, configurar interfaces Loopback y utilizar el protocolo OSPF para comprobar la comunicación entre los routers.

---

## Dispositivos utilizados

- Router R1
- Router R2
- Switch multicapa S1

---

## Configuración del Router R1

Primero se ingresó al modo de configuración global y se cambió el nombre del router a R1.

```bash
configure terminal
hostname R1
```

Después se configuró la interfaz GigabitEthernet 0/0 con la dirección IP correspondiente.

```bash
interface gi0/0
no shutdown
ip address 10.1.1.1 255.255.255.0
```

El comando `no shutdown` permite habilitar la interfaz para que pueda funcionar correctamente.

Posteriormente se configuró una interfaz Loopback.

```bash
interface loopback 0
ip address 1.1.1.1 255.255.255.255
```

Finalmente se salió del modo de configuración, se verificó el estado de las interfaces y se guardó la configuración.

```bash
end
show ip interface brief
write
```

---

## Configuración del Router R2

Se ingresó al modo de configuración global y se cambió el nombre del router a R2.

```bash
configure terminal
hostname R2
```

Después se configuró la interfaz GigabitEthernet 0/0.

```bash
interface gi0/0
no shutdown
ip address 10.1.1.2 255.255.255.0
```

También se configuró una interfaz Loopback.

```bash
interface loopback 0
ip address 2.2.2.2 255.255.255.255
```

Finalmente se verificó el estado de las interfaces y se guardó la configuración.

```bash
end
show ip interface brief
write
```

---

## Pruebas de conectividad entre R1 y R2

Después de configurar las direcciones IP de ambos routers, se realizaron pruebas de conectividad mediante el comando `ping`.

### Ping de R1 hacia R2

```bash
ping 10.1.1.2
```

### Ping de R2 hacia R1

```bash
ping 10.1.1.1
```

Estas pruebas permiten comprobar que existe comunicación entre ambos routers.

---

## Configuración del protocolo OSPF

Posteriormente se configuró el protocolo OSPF en ambos routers.

### OSPF en R1

```bash
configure terminal
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
end
write
```

### OSPF en R2

```bash
configure terminal
router ospf 1
network 0.0.0.0 255.255.255.255 area 0
end
write
```

El protocolo OSPF permite que los routers intercambien información de enrutamiento y conozcan las diferentes redes disponibles.

---

## Configuración del Switch S1

Se ingresó al modo privilegiado y posteriormente al modo de configuración global.

```bash
enable
configure terminal
hostname S1
```

Después se configuró la interfaz VLAN 1 con una dirección IP.

```bash
interface vlan 1
ip address 10.1.1.3 255.255.255.0
no shutdown
```

Finalmente se salió del modo de configuración y se guardaron los cambios.

```bash
end
write
```

---

## Verificación de OSPF

Para comprobar que el protocolo OSPF estaba funcionando correctamente se utilizó el siguiente comando:

```bash
show ip ospf neighbor
```

Este comando permite visualizar los routers vecinos detectados mediante OSPF.

Si la relación entre los routers se establece correctamente, significa que ambos dispositivos pueden intercambiar información de enrutamiento.

---

## Verificación de la tabla de enrutamiento

En el Router R1 se utilizó el siguiente comando:

```bash
show ip route
```

Este comando permite visualizar la tabla de enrutamiento del router.

Dentro de la tabla se pueden identificar:

- Redes conectadas directamente.
- Rutas aprendidas.
- Rutas relacionadas con OSPF.

La tabla de enrutamiento permite conocer las rutas disponibles que puede utilizar el router para enviar información hacia diferentes redes.

---

## Resultado

Se configuraron los routers R1 y R2 y el switch multicapa S1.

También se configuraron direcciones IP, interfaces Loopback y el protocolo OSPF.

Las pruebas realizadas mediante `ping` permitieron comprobar la conectividad entre los routers.

Además, los comandos `show ip interface brief`, `show ip ospf neighbor` y `show ip route` permitieron verificar el estado de las interfaces, la relación de vecinos OSPF y las rutas disponibles en la red.

---

## Evidencias

Las evidencias correspondientes a la Topología 02 incluyen:

- Topología completa.
- Configuración del Router R1.
- Configuración del Router R2.
- Configuración del Switch S1.
- Ping de R1 hacia R2.
- Ping de R2 hacia R1.
- Verificación de vecinos OSPF.
- Tabla de enrutamiento.
