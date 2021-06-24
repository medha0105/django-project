from .models import Customer
# For men: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) + 5
# For women: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) – 161

def dummycalc(pk):
    customer = Customer.objects.get(id=pk)
    Idealcalorie = 0
    if customer.gender == "Male":
        Idealcalorie = (10*(customer.weight)) + (6.25*(customer.height)) - (5*(customer.age)) + 5
    else:
        Idealcalorie = (10*(customer.weight)) + (6.25*(customer.height)) - (5*(customer.age)) - 161
    
    
    if customer.category == "Inactive":
        Idealcalorie *= 1.2
    elif customer.category == "Moderately active":
        Idealcalorie *= 1.3
    else:
        Idealcalorie *= 1.4

    return round(Idealcalorie)
   