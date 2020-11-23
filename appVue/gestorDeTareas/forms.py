from django import forms
from .models import Notas
from rest_framework import serializers



class NotasForm(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = "__all__"

        
        def __init__(self, *args, **kwargs):
            super(NotasForm, self).__init__(*args, **kwargs)
            self.fields['notas'].widget.attrs.update({'class' :'input', 'type':'text', 'placeholder':'Ingrese la Nota', 'v-model':'notas_txt', 'v-on:keyup.enter':'AgregarNotas()'})