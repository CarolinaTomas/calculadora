# Calculadora de Raíces de Polinomios

Este proyecto es una aplicación web desarrollada con Django que permite calcular las raíces reales de funciones polinómicas mediante tres métodos numéricos:

- Método de Bisección
- Método de Newton-Raphson
- Método de Newton-Raphson Modificado

Incluye:
- Validación de entradas del usuario
- Visualización paso a paso en tabla de iteraciones
- Gráficas de la función
- Cálculo automático del error relativo

## Instalación

1. Clonar el repositorio y acceder a la carpeta del proyecto:
```bash
cd proyecto_calculadora_raices
```

2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py migrate
```

5. Ejecutar el servidor:
```bash
python manage.py runserver
```

6. Acceder desde el navegador:
```
http://127.0.0.1:8000/
```

## Estructura del Proyecto

- `raiz/`: Aplicación principal donde se define la lógica de los métodos y la interfaz de usuario.
- `metodos.py`: Contiene la implementación de los algoritmos de Bisección, Newton-Raphson y Newton-Raphson Modificado.
- `graficas.py`: Se encarga de generar gráficas con Matplotlib.
- `forms.py`: Formularios de entrada del usuario.
- `views.py`: Lógica principal para procesar la solicitud del usuario y renderizar resultados.
- `templates/`: Contiene la plantilla HTML `calcular.html`.
- `static/`: Archivos estáticos como estilos CSS y scripts JS.

## Tecnologías Utilizadas
- Python 3
- Django
- Matplotlib
- HTML5 y CSS3
- Bootstrap (para estilos responsivos)

## Autores
- Desarrollado por Wendy Tomás

## Licencia
Este proyecto está bajo la Licencia MIT.
