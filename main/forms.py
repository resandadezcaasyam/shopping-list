from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    #Buat form untuk model Product
    class Meta:
        model = Product
        fields = ["name", "price", "description"]