# Instalación y ejecución local
## 1. Clonar el repositorio escribiendo esta línea en una terminal (PowerShell o CMD)
```bash
git clone https://github.com/choco-gtx/grupo-13-proyecto-inicial.git
```

## 2. Ingresar a la carpeta escribiendo
```bash
cd grupo-13-proyecto-inicial
```

## 3. Crear el entorno virtual
```bash
python -m venv .venv
```

## 4. Activar este entorno 
(Si la terminal es "PowerShell")
```bash
.\.venv\Scripts\Activate.ps1
```
(Si la terminal es "CMD")
```bash
.venv\Scripts\activate
```

## 5. Instalar las dependencias
```bash
pip install -r requirements.txt
```

## 6. Preparar la base de datos de la aplicación
```bash
python manage.py migrate
```

## 7. Iniciar el servidor de Django
```bash
python manage.py runserver
```

## 8. Acceder ingresando el siguiente link en un navegador

http://127.0.0.1:8000/

* No hay datos necesarios para probar la funcionalidad corazón de la aplicación.
