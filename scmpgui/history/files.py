import pandas as pd
from .models import HistoricalRecords

def LoadSetupRecords():
    df = pd.read_excel("history\data\sampleInput.xlsx")
    cols_to_check = ['Identification No', 'Sample No', 'Lac. No.', 'DIM( Days In Milk)', 'Avg(7 days). Daily MY( L )', 'Test day MY (L )', 'Fat (%)', 'SNF (%)', 'Density ( Kg/ m3', 'Protein (%)', 'Conductivity (mS/cm)', 'pH', 'Freezing point (⁰C)', 'Salt (%)', 'Lactose (%)', 'SCC (103cells/ml)', 'Label']
    df[cols_to_check] = df[cols_to_check].apply(pd.to_numeric,errors='coerce')
    df = df.dropna(subset=cols_to_check)
    return df

def PopulateModel(dataframe):
    # Create a dictionary to map model fields to DataFrame columns
    field_mapping = {
        'id_num': 'Identification No',
        'sample_num': 'Sample No',
        'farm': 'Farm',
        'breed': 'Breed',
        'lactation_num': 'Lac. No.',
        'dim': 'DIM( Days In Milk)',
        'avg_daily_milk_yield': 'Avg(7 days). Daily MY( L )',
        'test_day_milk_yield': 'Test day MY (L )',
        'fat_percentage': 'Fat (%)',
        'snf_percentage': 'SNF (%)',
        'milk_density': 'Density ( Kg/ m3',
        'protein_percentage': 'Protein (%)',
        'milk_conductivity': 'Conductivity (mS/cm)',
        'milk_ph': 'pH',
        'freezing_point': 'Freezing point (⁰C)',
        'salt_percentage': 'Salt (%)',
        'lactose_percentage': 'Lactose (%)',
        'scc': 'SCC (103cells/ml)',
        'label': 'Label'
    }
    
    # Iterate over each row in the DataFrame
    for _, row in dataframe.iterrows():
        # Create a dictionary to store the record data
        record_data = {}
    
        # Map DataFrame column values to model fields
        for field_name, column in field_mapping.items():
            record_data[field_name] = row[column] if column in row else None
    
        # Create the HistoricalRecords object
        HistoricalRecords.objects.create(**record_data)

def InitHistory():
    PopulateModel(LoadSetupRecords())