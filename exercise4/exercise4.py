cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("Estão disponíveis", cars, "carros")
print("Tem apenas", drivers, "motoristas disponíveis")
print("Vão ter", cars_not_driven, "carros parados hoje")
print("Nós conseguimos transportar", carpool_capacity, "pessoas hoje")
print("Nós temos", passengers, "passageiros hoje")
print("Nós precisaremos colocar",
      average_passengers_per_car, "pessoas em cada carro")
