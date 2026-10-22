# Práctica 01: Configuración del entorno

## 1. Configuración de Visual Studio Code

Se instaló la extensión oficial de Python desarrollada por Microsoft para permitir la ejecución de programas en Python.

Se creó la carpeta de trabajo automatizacion-redes y se abrió desde Visual Studio Code.

## 2. Creación del entorno virtual

Se creó un entorno virtual denominado .venv mediante el comando:

python -m venv .venv

Posteriormente, se activó utilizando:

.\.venv\Scripts\Activate.ps1

Se verificó su activación mediante el indicador (.venv) en la terminal.

## 3. Configuración del intérprete

Se selecciona el intérprete correspondiente al entorno virtual .venv desde Visual Studio Code.

## 4. Configuración de Git

Se configuró la identidad del usuario mediante los comandos:

git config --global user.name "Karina Hernandez Lona"

git config --global user.email "CORREO_CONFIGURADO"

La configuración se consulta mediante:

git config --global --list

## 5. Configuración del repositorio

Se creó el repositorio automatizacion-redes en GitHub y se inicializó el repositorio local mediante:

git init -b main

También se creó el archivo .gitignore para evitar subir archivos innecesarios, como el entorno virtual.