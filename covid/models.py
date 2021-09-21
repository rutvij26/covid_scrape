from django.db import models

# Create your models here.

class CovidData (models.Model) :
    Id = models.IntegerField(primary_key=True)
    Country = models.CharField(max_length=255)
    Confirmed = models.BigIntegerField()
    New_cases = models.BigIntegerField()
    Deaths = models.BigIntegerField()
    Recovered = models.BigIntegerField()
    
    def __str__(self) -> str:
        return self.Country