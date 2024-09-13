#This program is meant to list all cars
AllowedVehichlesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan'
]

#Define function to print the menu
def print_menu():
  print('********************************') 
  print('AutoCountry Vehicle Finder v0.1')
  print('********************************')
  print('Please Enter the following number below from the following menu: ')
  print('\n1. PRINT all Authorized Vehicles \n2. Exit')


#Define function to print the list of authorized vehicles
def print_vehicles():
  print('\nThe AutoCountry sales manager as authorized the purchase and selling of the following vehicles:') 
  for vehicle in AllowedVehichlesList:
    print(vehicle) 
  print()
  
#Define the main loop
while True:
  print_menu()
  choice = input('\nEnter your choice: ')
  
  if choice == '1':
      print_vehicles()
  elif choice == '2': 
      print('Thank you for using the AutoCountry Vehicle Finder, good-bye!') 
      break 
  else:
      print('Invalid choice, please try again')