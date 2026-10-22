equipo = "R1"
categoria = "Router"
ip_dispositivo = "10.1.1.1"
interfaz = "GigabitEthernet0/0"
estatus = "Activo"

print("Nombre:", equipo)
print("Tipo:", categoria)
print("Direccion IP:", ip_dispositivo)
print("Interfaz:", interfaz)
print("Estado:", estatus)


router1 = {
    "nombre": "R1",
    "tipo": "Router",
    "ip": "10.1.1.1",
    "loopback": "1.1.1.1",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo"

}


print("Dispositivo:", router1["nombre"])
print("Dirección IP:", router1["ip"])
print("Estado:", router1["estado"])
print("Loopback:", router1["loopback"])
print("Interfaz:", router1["interfaz"])
print ("")
print ("")
print ("")


dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo",
        "fabricante": "GNS3",
        "protocolo": "OSPF"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo",
        "fabricante": "GNS3",
        "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo",
        "fabricante": "GNS3",
        "protocolo": "OSPF"
    }
]

for dispositivo in dispositivos:
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("--------------------")




router1 = {
    "nombre": "R1",
    "tipo": "Router",
    "ip": "10.1.1.1",
    "loopback": "1.1.1.1",
    "interfaz": "GigabitEthernet0/0",
    "estado": "fuera de servicio"
}


print("Dispositivo:", router1["nombre"])
print("Dirección IP:", router1["ip"])
print("Estado:", router1["estado"])
print("Loopback:", router1["loopback"])
print("Interfaz:", router1["interfaz"])


if router1["estado"] == "Activo":
    print("El dispositivo está disponible.")
else:
    print("El dispositivo requiere atención.")


def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Protocolo:", dispositivo["protocolo"])

for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)
    print("--------------------")
