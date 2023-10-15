from django.db import models

#not useful, this model can save the imported xl sheet in media/uploads
class ExcelFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

#model for create fields for storing data of importing dataset
class Batchdataset(models.Model):
    # 1. id_num (Identification No)
    id_num = models.CharField(max_length=50, unique=True)

    # 2. sample_num (Sample No)
    sample_num = models.PositiveIntegerField()

    # 3. farm (Farm)
    farm = models.CharField(max_length=100)

    # 4. breed (Breed)
    breed = models.CharField(max_length=100)

    # 5. lactation_num (Lactation Number)
    lactation_num = models.PositiveIntegerField()

    # 6. dim (Days In Milk)
    dim = models.PositiveIntegerField()

    # 7. avg_daily_milk_yield (Avg(7 days). Daily MY (L))
    avg_daily_milk_yield = models.DecimalField(max_digits=10, decimal_places=3)

    # 8. test_day_milk_yield (Test day MY (L))
    test_day_milk_yield = models.DecimalField(max_digits=10, decimal_places=3)

    # 9. fat_percentage (Fat (%))
    fat_percentage = models.DecimalField(max_digits=10, decimal_places=3)

    # 10. snf_percentage (SNF (%) - Solid-Not-Fat)
    snf_percentage = models.DecimalField(max_digits=10, decimal_places=3)

    # 11. milk_density (Density - Kg/m³)
    milk_density = models.DecimalField(max_digits=10, decimal_places=3)

    # 12. protein_percentage (Protein (%))
    protein_percentage = models.DecimalField(max_digits=10, decimal_places=3)

    # 13. milk_conductivity (Conductivity - mS/cm)
    milk_conductivity = models.DecimalField(max_digits=10, decimal_places=3)

    # 14. milk_ph (pH)
    milk_ph = models.DecimalField(max_digits=10, decimal_places=3)

    # 15. freezing_point (Freezing point - ⁰C)
    freezing_point = models.DecimalField(max_digits=10, decimal_places=3)

    # 16. salt_percentage (Salt (%))
    salt_percentage = models.DecimalField(max_digits=10, decimal_places=3)

    # 17. lactose_percentage (Lactose (%))
    lactose_percentage = models.DecimalField(max_digits=10, decimal_places=3)

    # 18. label (Label)
    label = models.CharField(max_length=10,blank=True,null=True)

    def to_string(self):
        return (
            f"ID: {self.id_num}\n"
            f"Sample No: {self.sample_num}\n"
            f"Farm: {self.farm}\n"
            f"Breed: {self.breed}\n"
            f"Lactation Num: {self.lactation_num}\n"
            f"DIM: {self.dim}\n"
            f"Avg Daily Milk Yield: {self.avg_daily_milk_yield}\n"
            f"Test Day Milk Yield: {self.test_day_milk_yield}\n"
            f"Fat Percentage: {self.fat_percentage}\n"
            f"SNF Percentage: {self.snf_percentage}\n"
            f"Milk Density: {self.milk_density}\n"
            f"Protein Percentage: {self.protein_percentage}\n"
            f"Milk Conductivity: {self.milk_conductivity}\n"
            f"Milk pH: {self.milk_ph}\n"
            f"Freezing Point: {self.freezing_point}\n"
            f"Salt Percentage: {self.salt_percentage}\n"
            f"Lactose Percentage: {self.lactose_percentage}\n"
            f"Label: {self.label}"
        )

    def __str__(self):
        return f"Record {self.id} - Cow: {self.id_num}, Sample: {self.sample_num}, Farm: {self.farm}"
