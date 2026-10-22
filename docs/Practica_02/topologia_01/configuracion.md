# Configuración de la Topología 01

## Descripción

La Topología 01 está formada por dos computadoras virtuales VPCS conectadas a un switch Ethernet dentro de GNS3.

El objetivo de esta topología fue configurar el direccionamiento IP en ambos equipos y comprobar que existiera comunicación entre ellos mediante pruebas de conectividad.

---

## Dispositivos utilizados

- PC1
- PC2
- Ethernet Switch

---

## Configuración de PC1

Se configuró la siguiente dirección IP:

```bash
ip 10.1.1.1 255.255.255.0
save
