from django import forms

class AnalyzForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='Ism', widget=forms.TextInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    last_name = forms.CharField(max_length=100, label='Familiya', widget=forms.TextInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    age = forms.IntegerField(label='Yoshingiz', widget=forms.NumberInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    buying = forms.IntegerField(label='Buyingiz', widget=forms.NumberInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    systolic_blood_pressure = forms.IntegerField(label='Systolic_blood_pressure', widget=forms.NumberInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    total_cholesterol = forms.IntegerField(label='Total_cholesterol', widget=forms.NumberInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    hdl_cholesterol = forms.IntegerField(label='Hdl_cholesterol', widget=forms.NumberInput(attrs={'class': 'form-control'}),error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'})
    # Boshqa modullar uchun kerak bo'lgan maydonlar
    on_blood_pressure_medication = forms.ChoiceField(
        choices=[
            ('0', 0),
            ('1', 1),
        ],
        label='On Blood Pressure Medication',
        widget=forms.Select(attrs={'class': 'form-select'})
        ,error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'}
    )
    cigarette_smoker = forms.ChoiceField(
        choices=[
            ('0', 0),
            ('1', 1),
        ],
        label='Cigarette Smoker',
        widget=forms.Select(attrs={'class': 'form-select'})
        ,error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'}
    )

    diabetes_present = forms.ChoiceField(
        choices=[
            ('0', 0),
            ('1', 1),
        ],
        label='Diabetes Present',
        widget=forms.Select(attrs={'class': 'form-select'})
        ,error_messages = { 'required': 'Bu maydon to\'ldirilishi shart.'}
    )

