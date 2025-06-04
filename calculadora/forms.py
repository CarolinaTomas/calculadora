from django import forms

METODOS = (
    ('biseccion', 'Bisección'),
    ('newton', 'Newton-Raphson'),
    ('newton_mod', 'Newton-Raphson Modificado'),
)

class MetodoForm(forms.Form):
    funcion = forms.CharField(
        label='Función polinómica',
        widget=forms.TextInput(attrs={'placeholder': 'Ej: x**3 - 4*x + 1'})
    )
    metodo = forms.ChoiceField(label='Método numérico', choices=METODOS)
    a = forms.FloatField(label='Extremo a (para Bisección)', required=False)
    b = forms.FloatField(label='Extremo b (para Bisección)', required=False)
    x0 = forms.FloatField(label='Valor inicial x0 (para Newton)', required=False)
    tolerancia = forms.FloatField(label='Tolerancia', initial=0.0001)
    max_iter = forms.IntegerField(label='Máximo de iteraciones', initial=100)

    def clean(self):
        cleaned_data = super().clean()
        metodo = cleaned_data.get("metodo")
        a = cleaned_data.get("a")
        b = cleaned_data.get("b")
        x0 = cleaned_data.get("x0")

        if metodo == 'biseccion':
            if a is None:
                self.add_error('a', "Este campo es obligatorio para Bisección.")
            if b is None:
                self.add_error('b', "Este campo es obligatorio para Bisección.")
            if a is not None and b is not None and a >= b:
                self.add_error('a', "El valor de 'a' debe ser menor que 'b'.")
                self.add_error('b', "El valor de 'b' debe ser mayor que 'a'.")
        elif metodo in ['newton', 'newton_mod']:
            if x0 is None:
                self.add_error('x0', "Este campo es obligatorio para Newton-Raphson.")

        return cleaned_data
