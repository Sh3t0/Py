def calculate_paint(efficency_ltr_per_m2, *meters):
    sum_meters = sum(meters)
    result = efficency_ltr_per_m2 * sum_meters
    return result


print(calculate_paint(0.1,20,30,40,50))
rooms =[(20),(30),(40),(50)]
#__________________________________________________________________
print('_'*50)
#__________________________________________________________________
print(calculate_paint(0.1,*rooms))



