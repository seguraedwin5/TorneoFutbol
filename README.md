
# Micro Torneo de Fútbol con Flask

Esta aplicación web desarrollada con Flask permite organizar un micro torneo de fútbol con 4 equipos de futbol, permitiendo a los usuarios seleccionar los ganadores de varios partidos y finalmente mostrando el equipo ganador con más victorias.

## Características

- Visualización de equipos participantes.
- Selección de ganadores de partidos en interfaz usuario.
- Cálculo automático del equipo ganador del torneo basado en selecciones de usuarios.

## Tecnologías Utilizadas

-   **Backend:** Flask (Python)
-   **Frontend:** HTML, CSS (Bootstrap para estilos), JavaScript (jQuery para AJAX)

## Estructura del Proyecto

```
/TorneoFutbol
    ├── static/
    │   ├── css/
    │   │   └── styles.css
    │   └── js/
    │       └── main.js
    ├── templates/
    │   └── index.html
    ├── app.py
    ├── match.py
    └── README.md
```

## Instalación, Configuración y Ejecución

Para ejecutar Micro Torneo de Fútbol en tu entorno local, sigue estos pasos:

1.  Clona el repositorio a tu máquina local.

	```
	https://github.com/dalzoj/TorneoFutbol.git
	```

2.  Navega al directorio del proyecto.

	```
	cd TorneoFutbol
	```

3.  Crear un entorno virtual.

    ```
    python -m venv venv
    ``` 

4.  Activa el entorno virtual.
    
    -   En Windows:
		 ```venv\Scripts\activate``` 
        
    -   En Unix o MacOS:
        ```source venv/bin/activate```
        
5.  Instala las dependencias necesarias.

	```
	pip install -r requirements.txt
	```

6.  Ejecuta la aplicación.

	```
	python app.py
	```

7.  Abrir el navegador en la dirección `http://127.0.0.1:5000/` para comenzar a usar la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Puedes enviar un pull request o abrir un issue para discutir nuevas modificaciones o añadir futuras funcionalidades.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.



