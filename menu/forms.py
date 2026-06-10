from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['category', 'name', 'price', 'image', 'is_vegetarian']

        widgets = {
            'category': forms.TextInput(attrs={"placeholder": "e.g Fast Food"}),
            'name': forms.TextInput(attrs={"placeholder": "e.g Burger"}),
            'price': forms.NumberInput(attrs={"placeholder": "100"})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        category = cleaned_data.get('category')
        name = cleaned_data.get('name')

        # Validate price
        if price < 0:
            self.add_error('price', "Price should not be negative")

        # Validate category vs name
        if category and name and str(category) == str(name):
            self.add_error('name', "Category and name should be different")

        return cleaned_data