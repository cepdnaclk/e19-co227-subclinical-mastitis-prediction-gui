from django import forms
from .widgets import CustomInputWidget

from django.core.validators import DecimalValidator,MinValueValidator,MaxValueValidator
from .validators import StrictNumeric,CowBreeds,phRange

class DataForm(forms.Form):
    id_num = forms.CharField(
        max_length=50,
        validators=[StrictNumeric],
        required=True,
        widget=CustomInputWidget(
            input_type='text',
            width='4',
            label='Identification Number',
            pop_text='This field represents a unique identifier for individual cattle. It serves as a critical tracking mechanism for managing the health and well-being of each animal in your herd. Use this ID to maintain comprehensive records and monitor the health history of specific cattle.',
        ),
    )
    id_num.group=1

    sample_num = forms.CharField(
        max_length=50,
        required=True,
        validators=[StrictNumeric],
        widget=CustomInputWidget(
            input_type='text',
            width='4',
            label='Sample Number',
            pop_text='Sample Number is a designation assigned to distinguish one milk sample from another, especially when multiple samples are collected from the same cow over time. This parameter aids in precise sample identification, making it easier to analyze and compare milk data accurately.',
        )
    )
    sample_num.group=1

    farm = forms.CharField(
        max_length=50,
        required=True,
        widget=CustomInputWidget(
            input_type='text',
            width='4',
            label='Farm',
            pop_text='The Farm parameter denotes the name or identifier of the location where your cattle are situated. It is vital for maintaining comprehensive records and associating data with specific farm sources. This information helps you manage and organize your cattle-related data effectively.'
        )
    )
    farm.group = 1

    breed = forms.CharField(
        max_length=50,
        required=True,
        validators=[CowBreeds],
        widget=CustomInputWidget(
            input_type='text',
            width='12',
            label='Breed',
            pop_text='Breed indicates the specific breed of the cattle being tested. Different cattle breeds may exhibit varying susceptibilities to conditions like mastitis and can produce milk with distinct characteristics. Identifying the breed is crucial for understanding and managing your herd\'s health and productivity.'
        )
    )
    breed.group = 2

    lactation_num = forms.IntegerField(
        required=True,
        validators=[StrictNumeric],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Lactation Number',
            pop_text='The Lactation Number parameter represents the count of times a cow has given birth and entered a new lactation cycle. It plays a significant role in assessing milk quality and mastitis risk, as milk composition and health can change with each lactation cycle.'
        )
    )
    lactation_num.group = 3

    dim = forms.IntegerField(
        required=True,
        validators=[StrictNumeric],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Days In Milk',
            pop_text='Days In Milk (DIM) signifies the number of days since a cow calved and began producing milk. This is a critical factor because mastitis risk varies during different stages of lactation. Monitoring DIM helps in understanding and managing the health of your cattle.'
        )
    )
    dim.group = 3

    avg_daily_milk_yield = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Avg. 7-day Daily Milk Yield (L)',
            pop_text='This parameter calculates the average daily milk yield over the past seven days. It is a valuable tool for assessing milk production trends and overall herd productivity. Consistent tracking of this parameter aids in making informed management decisions.',
            attrs={'step': '0.01', 'min': '0', 'max': '10'}
        )
    )
    avg_daily_milk_yield.group = 4

    test_day_milk_yield = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Test Day Milk Yield (L)',
            pop_text='Test Day Milk Yield represents the amount of milk produced by a cow on the specific day of testing. This data point provides an immediate snapshot of individual milk production, helping you identify any deviations from normal output.',
            attrs={'step': '0.01'}
        )
    )
    test_day_milk_yield.group = 4

    fat_percentage = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Fat (%)',
            pop_text='The Fat percentage parameter indicates the fat content in the milk sample. It is a crucial component of milk quality assessment, as variations can signal potential issues such as mastitis or changes in nutritional balance.',
            attrs={'step': '0.01'}
        )
    )
    fat_percentage.group = 5

    snf_percentage = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='SNF (%) (Solid-Not-Fat)',
            pop_text='Solid-Not-Fat (SNF) represents the percentage of solids in the milk, excluding fat. This category encompasses proteins, lactose, minerals, and other components, contributing to overall milk quality evaluation.',
            attrs={'step': '0.01'}
        )
    )
    snf_percentage.group = 5

    milk_density = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Density (Kg/m³)',
            pop_text='Density quantifies the mass per unit volume of the milk sample, usually measured in kilograms per cubic meter. Monitoring density can offer insights into milk composition and quality.',
            attrs={'step': '0.01'}
        )
    )
    milk_density.group = 6

    protein_percentage = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Protein (%)',
            pop_text='The Protein percentage parameter signifies the protein content within the milk sample. It is another essential component of milk quality analysis, influencing the nutritional value and suitability of the milk for various purposes.',
            attrs={'step': '0.01'}
        )
    )
    protein_percentage.group = 6

    milk_conductivity = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Conductivity (mS/cm)',
            pop_text='Conductivity measures the electrical conductivity of the milk. It can serve as an indicator of mastitis, as infected udders may exhibit higher conductivity due to increased salt content. Monitoring conductivity aids in early detection of potential health issues.',
            attrs={'step': '0.01'}
        )
    )
    milk_conductivity.group = 7

    milk_ph = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),phRange],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='pH',
            pop_text='pH measures the acidity or alkalinity of the milk. Fluctuations in pH levels can be associated with mastitis or other milk quality concerns. This parameter provides valuable insights into the milk\'s chemical composition.',
            attrs={'step': '0.01'}
        )
    )
    milk_ph.group = 7

    freezing_point = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Freezing Point (⁰C)',
            pop_text='The Freezing Point parameter indicates the temperature at which the milk sample freezes. Deviations from the expected freezing point can raise red flags, as they may suggest mastitis or other milk quality irregularities.',
            attrs={'step': '0.01'}
        )
    )
    freezing_point.group =8

    salt_percentage = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Salt (%)',
            pop_text='The Salt percentage parameter represents the salt content in the milk sample. Abnormal salt levels can indicate various milk quality issues, making this parameter important for overall milk assessment.',
            attrs={'step': '0.01'}
        )
    )
    salt_percentage.group =8

    lactose_percentage = forms.DecimalField(
        required=True,
        validators=[DecimalValidator(max_digits=5,decimal_places=2),MinValueValidator(limit_value=0)],
        widget=CustomInputWidget(
            input_type='number',
            width='6',
            label='Lactose (%)',
            pop_text='Lactose percentage denotes the presence of lactose, or milk sugar, in the milk sample. This component is crucial for assessing milk quality and suitability for various dairy products.',
            attrs={'step': '0.01'}
        )
    )
    lactose_percentage.group =9
