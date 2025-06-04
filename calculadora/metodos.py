import sympy as sp

# Método de Bisección
def biseccion(f_expr, a, b, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')

    if f(a) * f(b) >= 0:
        return None, "No hay cambio de signo en el intervalo [a, b]"

    iteraciones = []
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2

        iteraciones.append((i, a, b, c, fc, error))

        if abs(fc) < tol or error < tol:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return iteraciones, c

# Método de Newton-Raphson
def newton(f_expr, x0, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')

    iteraciones = []
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            return None, f"Derivada cero en x = {x0}. Método falla."

        x1 = x0 - fx / dfx
        error = abs(x1 - x0)

        iteraciones.append((i, x0, fx, dfx, x1, error))

        if error < tol:
            break

        x0 = x1

    return iteraciones, x1

# Método de Newton-Raphson Modificado
def newton_modificado(f_expr, x0, tol, max_iter):
    x = sp.symbols('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df_expr = sp.diff(f_expr, x)
    d2f_expr = sp.diff(df_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')
    d2f = sp.lambdify(x, d2f_expr, 'numpy')

    iteraciones = []
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        d2fx = d2f(x0)

        denominador = dfx**2 - fx * d2fx
        if denominador == 0:
            return None, "Denominador cero. Método falla."

        x1 = x0 - (fx * dfx) / denominador
        error = abs(x1 - x0)

        iteraciones.append((i, x0, fx, dfx, d2fx, x1, error))

        if error < tol:
            break

        x0 = x1

    return iteraciones, x1
