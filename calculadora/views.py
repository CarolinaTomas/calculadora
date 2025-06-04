from django.shortcuts import render
from .forms import MetodoForm
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
import uuid
from django.conf import settings

# Método de Bisección
def metodo_biseccion(f, a, b, tol, max_iter):
    resultados = []
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos.")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        error = abs(b - a) / 2.0

        resultados.append({
            'iteracion': i,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'error': error
        })

        if error < tol or fc == 0:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return resultados, c

# Método de Newton-Raphson
def metodo_newton(f, df, x0, tol, max_iter):
    resultados = []
    x = x0

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ZeroDivisionError("Derivada cero: no se puede continuar.")

        x1 = x - fx / dfx
        error = abs(x1 - x)

        resultados.append({
            'iteracion': i,
            'x': x,
            'f(x)': fx,
            "f'(x)": dfx,
            'x1': x1,
            'error': error
        })

        if error < tol:
            break

        x = x1

    return resultados, x

# Método de Newton-Raphson Modificado
def metodo_newton_modificado(f, df, d2f, x0, tol, max_iter):
    resultados = []
    x = x0

    for i in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        d2fx = d2f(x)

        denominador = dfx**2 - fx * d2fx
        if denominador == 0:
            raise ZeroDivisionError("División por cero en Newton modificado.")

        x1 = x - (fx * dfx) / denominador
        error = abs(x1 - x)

        resultados.append({
            'iteracion': i,
            'x': x,
            'f(x)': fx,
            "f'(x)": dfx,
            "f''(x)": d2fx,
            'x1': x1,
            'error': error
        })

        if error < tol:
            break

        x = x1

    return resultados, x

# Función para graficar
def graficar_funcion(funcion_str, raiz=None, intervalo=None):
    x = sp.symbols('x')
    f = sp.lambdify(x, sp.sympify(funcion_str), modules=['numpy'])

    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='gray', linestyle='--')

    if raiz is not None:
        plt.plot(raiz, f(raiz), 'ro', label='Raíz encontrada')

    if intervalo:
        plt.axvline(intervalo[0], color='green', linestyle='--', label='a')
        plt.axvline(intervalo[1], color='orange', linestyle='--', label='b')

    plt.legend()
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfica del Polinomio')

    nombre_archivo = f"grafico_{uuid.uuid4().hex}.png"
    ruta = os.path.join(settings.MEDIA_ROOT, nombre_archivo)
    plt.savefig(ruta)
    plt.close()

    return f'{settings.MEDIA_URL}{nombre_archivo}'

# Vista principal
def calcular(request):
    resultado = None
    tabla = []
    grafico_url = None

    if request.method == 'POST':
        form = MetodoForm(request.POST)
        if form.is_valid():
            funcion_str = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            tol = form.cleaned_data['tolerancia']
            max_iter = form.cleaned_data['max_iter']

            x = sp.symbols('x')
            f_expr = sp.sympify(funcion_str)
            f = sp.lambdify(x, f_expr, 'numpy')
            df = sp.lambdify(x, sp.diff(f_expr, x), 'numpy')

            try:
                if metodo == 'biseccion':
                    a = form.cleaned_data['a']
                    b = form.cleaned_data['b']
                    tabla, raiz = metodo_biseccion(f, a, b, tol, max_iter)
                    grafico_url = graficar_funcion(funcion_str, raiz=raiz, intervalo=(a, b))

                elif metodo == 'newton':
                    x0 = form.cleaned_data['x0']
                    tabla, raiz = metodo_newton(f, df, x0, tol, max_iter)
                    grafico_url = graficar_funcion(funcion_str, raiz=raiz)

                elif metodo == 'newton_mod':
                    x0 = form.cleaned_data['x0']
                    d2f = sp.lambdify(x, sp.diff(f_expr, x, 2), 'numpy')
                    tabla, raiz = metodo_newton_modificado(f, df, d2f, x0, tol, max_iter)
                    grafico_url = graficar_funcion(funcion_str, raiz=raiz)

                resultado = raiz

            except Exception as e:
                form.add_error(None, f"Error: {str(e)}")
    else:
        form = MetodoForm()

    return render(request, 'calculadora/calculadora.html', {
        'form': form,
        'tabla': tabla,
        'resultado': resultado,
        'grafico_url': grafico_url
    })