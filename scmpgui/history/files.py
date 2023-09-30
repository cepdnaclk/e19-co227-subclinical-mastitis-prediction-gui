import pandas as pd

def LoadSetupRecords():
    df = pd.read_excel("data/sampleInput.xlsx")
    print(df.columns.tolist())
    cols_to_check = ['Identification No', 'Sample No', 'Lac. No.', 'DIM( Days In Milk)', 'Avg(7 days). Daily MY( L )', 'Test day MY (L )', 'Fat (%)', 'SNF (%)', 'Density ( Kg/ m3', 'Protein (%)', 'Conductivity (mS/cm)', 'pH', 'Freezing point (⁰C)', 'Salt (%)', 'Lactose (%)', 'SCC (103cells/ml)', 'Label']
    df[cols_to_check] = df[cols_to_check].apply(pd.to_numeric,errors='coerce')
    df = df.dropna(subset=cols_to_check)
    return df

print(LoadSetupRecords().iloc[36])