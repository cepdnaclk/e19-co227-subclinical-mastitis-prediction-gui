import pickle

def PredictPickle(lactation_num, dim, avg_daily_milk_yield, test_day_milk_yield, fat_percentage, snf_percentage, milk_density, protein_percentage, milk_conductivity, milk_ph, freezing_point, salt_percentage, lactose_percentage):
    # Load the trained model
    with open("external\scm.pkl", 'rb') as f:
        model = pickle.load(f)
    
    param_list = [lactation_num, dim, avg_daily_milk_yield, test_day_milk_yield, fat_percentage, snf_percentage, milk_density, protein_percentage, milk_conductivity, milk_ph, freezing_point, salt_percentage, lactose_percentage]
    
    prediction = model.predict([param_list])

    return bool(prediction[0])