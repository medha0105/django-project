from .models import Customer

# Formula used to calculate men’s calorie needs is = 66.5 + 13.8 x (body weight in kilograms) + 5 x (body height in cm) divided by 6.8 x age. 
# Meanwhile for women= 655.1 + 9.6 x (body weight in kilograms) + 1.9 x (body height in cm) divided by 4.7 x age. 
# Result of the equation must be multiplied with your physical activity factor. If you have low physical activity, then multiply by 1.2. If you participate in average physical activity then multiply by 1.3. For people who do heavy physical activities, multiply by 1.4.

def dummycalc(pk):
    customer = Customer.objects.get(id=pk)
    if customer.gender == "Male":
        Idealcalorie = (66.5 + (13.8 *customer.weight) + (5*customer.height))/ (6.5*customer.age)
        if customer.category == "Inactive":
            Idealcalorie *= 1.2
        elif customer.category == "Moderately active":
            Idealcalorie *= 1.3
        else:
            Idealcalorie *= 1.4
   