weight = 4.8
ground_shiping_premium = 125.00

#ground shipping

def ground_shipping():
  if weight <=2:
    cost =  weight * 1.50 + 20.00
    return (cost)
  elif weight >2 or weight <= 6:
    cost =  weight * 3.00 + 20.00
    return (cost)
  elif weight > 6 or weight <= 10:
    cost =  weight * 4.00 + 20.00
    return (cost)
  elif weight > 10:
    cost =  weight * 4.75 + 20.00
    return (cost)
  else:
    print('Error')

#Drone shipping

def drone_shipping():

  if weight <=2:
    cost =  weight * 4.50
    return (cost)
  elif weight >2 or weight <= 6:
    cost =  weight * 9.00
    return (cost)
  elif weight > 6 or weight <= 10:
    cost =  weight * 12.00
    return (cost)
  elif weight > 10:
    cost =  weight * 24.25
    return (cost)
  else:
    print('Error')

#Dispaying
print("Your ground shipping cost is: " + str(ground_shipping()) + '$')
print("Your premium shipping cost is: " + str(ground_shiping_premium) +'$')
print("Your drone shipping cost is: " + str(round(drone_shipping(), 1)) + '$')
