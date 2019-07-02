[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# python-wmi-arduino

Python app that reads PC telemetry through WMI and send it to Arduino

## Install

Instalar o virtual environment:

```
> pip install virtualenv
```

Crie um virtual environment:

```
> virtualenv env
```

Ative o environment ```Windows```:

```
> .\env\Scripts\activate
```

Instale os requisitos básicos:

```
(env) > pip install -r requirements.txt
```

## Formas de uso

Inicie um terminal do windows (PowerShell) com permissões de Administrador.

Então execute o seguinte comando:

```
(env) > python .\wmi2serial.py COM9 9600
```

Onde: 
- COM9 = sua porta serial
- 9600 = velocidade desejada para a comunicacao
