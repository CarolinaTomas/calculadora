# Calculadora Numérica de Raíces de Polinomios

Esta es una aplicación web desarrollada en Django que permite calcular raíces de funciones polinómicas utilizando tres métodos numéricos:

* Método de Bisección
* Método de Newton-Raphson
* Método de Newton-Raphson Modificado

Incluye una interfaz gráfica atractiva que permite visualizar la raíz aproximada, una tabla con las iteraciones realizadas y el gráfico de la función.

## 🚀 Tecnologías Usadas
**Python 3**
- **Django**
- **SymPy** (para derivadas simbólicas)
- **NumPy** (para cálculos numéricos)
- **Matplotlib** (para graficar funciones)
- **TailwindCSS + HTML5 + JavaScript** (interfaz moderna)

## ⚙️ Requisitos Previos

* Python 3.8 o superior
* pip (gestor de paquetes de Python)

---

## 🚀 Instalación del Proyecto

### 1. Clonar el repositorio o extraer el `.zip`

```bash
unzip raiz_polinomios.zip
cd raiz_polinomios
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si no tienes `requirements.txt`, puedes instalar manualmente:

```bash
pip install django matplotlib numpy sympy
```

### 4. Migraciones de base de datos (aunque no se usa modelo, es buena práctica)

```bash
python manage.py migrate
```

### 5. Crear carpeta para archivos multimedia (gráficas)

```bash
mkdir media
```

### 6. Ejecutar el servidor local

```bash
python manage.py runserver
```

### 7. Abrir en el navegador

```
http://127.0.0.1:8000/
```
🧠 ¿Cómo Funciona Internamente?
En el backend (views.py):

Se procesa el formulario (MetodoForm)

La función se transforma en expresiones simbólicas y derivadas con SymPy

Se convierten en funciones numéricas con lambdify

Según el método seleccionado:

Se ejecuta la función correspondiente (metodo_biseccion, metodo_newton, metodo_newton_modificado)

Se genera una tabla de iteraciones

Se grafica la función con Matplotlib y se guarda en /media

Se renderiza la plantilla calculadora/calculadora.html con los resultados


---

## 🧠 Uso de la Calculadora Web

Al acceder a `http://127.0.0.1:8000/`, se mostrará un formulario con los siguientes campos:

* **Función polinómica**: Ingresar una función como `x**3 - 4*x + 1` (usar notación de Python).
* **Método numérico**: Elegir uno de los tres métodos.
* **a / b**: Solo necesarios para el método de Bisección.
* **x0**: Solo necesario para Newton o Newton modificado.
* **Tolerancia**: Tolerancia deseada para el error.
* **Máximo de iteraciones**: Límite de pasos.

### 📌 Notas:

* Para **Bisección**, es obligatorio ingresar `a` y `b` tales que `f(a)` y `f(b)` tengan signos opuestos.
* Para **Newton** y **Newton Modificado**, es obligatorio ingresar un valor inicial `x0`.

Una vez enviado el formulario:

* Se muestra la **raíz aproximada** encontrada.
* Se genera una **tabla de iteraciones** con los valores usados en cada paso.
* Se muestra un **gráfico de la función**, con líneas verticales indicando `a`, `b` (si aplica) y un punto rojo en la raíz.

Un botón permite **volver al formulario** para hacer nuevos cálculos.

---

## 📄 Estructura Principal del Código

### `forms.py`

Se define `MetodoForm`, que incluye validaciones dinámicas según el método seleccionado:

```python
class MetodoForm(forms.Form):
    funcion = forms.CharField(...)
    metodo = forms.ChoiceField(...)
    a = forms.FloatField(...)
    b = forms.FloatField(...)
    x0 = forms.FloatField(...)
    tolerancia = forms.FloatField(...)
    max_iter = forms.IntegerField(...)

    def clean(self):
        # Validaciones condicionales por método
```

### `views.py`

Contiene:

* Implementaciones de los métodos:

  * `metodo_biseccion`
  * `metodo_newton`
  * `metodo_newton_modificado`
  * `biseccion`, `newton`, `newton_modificado` (versiones alternativas con `sympy`)
* Vista principal `calcular()` que maneja el POST y renderiza resultados.
* Función `graficar_funcion()` que genera un gráfico PNG y lo guarda en `/media`.

### Plantillas HTML:

* `calculadora.html`: Vista principal con formulario.
* `resultado.html`: Presentación de resultados con:

  * Raíz encontrada
  * Tabla de iteraciones
  * Gráfico generado dinámicamente
  * Botón para volver al formulario

### Métodos Alternativos Agregados:

El proyecto también incluye una versión alternativa de los métodos numéricos:

* `biseccion(f_expr, a, b, tol, max_iter)`
* `newton(f_expr, x0, tol, max_iter)`
* `newton_modificado(f_expr, x0, tol, max_iter)`

Estas versiones usan expresiones simbólicas de `sympy`, facilitando su reutilización y evaluación dinámica.

---

## 📊 Ejemplo de Salida

* Raíz aproximada mostrada en grande.
* Tabla con iteraciones (`x`, `f(x)`, `error`, etc.)
* Gráfico de la función con anotaciones para `a`, `b`, y raíz.

---

## 📁 Configuración en `settings.py`

Asegúrate de tener configurado:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Y en `urls.py` agregar:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ⚠️ Errores Comunes

* **Derivada cero en Newton**: Puede ocurrir si `f'(x) = 0`. Usa otro valor inicial.
* **Denominador cero en Newton Modificado**: Ocurre si `f'(x)**2 - f(x) * f''(x) = 0`.
* **Bisección sin cambio de signo**: Asegúrate que `f(a)*f(b) < 0`.
* **Función mal escrita**: Usa notación Python (`x**2`, no `x^2`).
* **No se genera gráfico**: Verifica que la carpeta `/media/` exista y tenga permisos de escritura.

---


## 💡 Créditos

Este proyecto fue desarrollado como parte del curso de Métodos Numéricos, con énfasis en la visualización de raíces de funciones polinómicas mediante herramientas modernas de desarrollo web.
Creado por Wendy Tomás

