import random
import time

def generate_weather(season):
    temperature = random.randint(-5,40)
    condition = random.choice(["Sunny", "Rainy", "Snowy", "Cloudy", "Windy", "Foggy"])

    if season == "Winter":
        temperature = random.randint(-15, 5)
        condition = random.choice(["Snowy", "Cloudy", "Windy", "Foggy"])
    elif season == "summer":
        temperature = random.randint(25, 45)    
        condition = random.choice(["Sunny", "Rainy", "Cloudy"])
    elif season == "monsoon":
        temperature = random.randint(20, 35)
        condition = random.choice(["Rainy", "Cloudy", "Windy"]) 
    elif season == "spring":   
        temperature = random.randint(10, 25)
        condition = random.choice(["Sunny", "Cloudy", "Windy"])

    return temperature, condition    
  
def simulate_weather():
    print("Welcome to the Weather Simulation Program!")
    seasons = ["Winter", "Summer", "Monsoon", "Spring"]
    print(" seasons: ", ", ".join(seasons))
    season = input("Enter a season to simulate weater : ").capitalize()

    if season not in seasons:
        print("Invalid season!")
        return
    print("\nSimulating weather ....")
    time.sleep(2)

    for day in range(1, 6):
        temp,cond = generate_weather(season)
        print(f"Day {day}: {cond} {temp}°C")
        time.sleep(1)
    print("\nSimulation is  completed !")

simulate_weather()        