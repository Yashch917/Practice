#Create a Python program that simulates an autonomous delivery robot.
#The robot must decide how to deliver a parcel based on:
 
#Distance to destination (km)
#Parcel weight (kg)
#Battery level (%)
#Weather condition (clear, rainy, or windy)
#using input function to get user inputs for distance, weight, battery level, and weather condition.

# Rules
# Delivery Mode:
# If distance > 10 or weight > 5 → use Drone Mode
# Else → use Ground Mode
# Battery Management:
# If battery < 30 → return to charging station
# Else → continue delivery
# Weather Adjustment:
# If rainy or windy → reduce speed by 30%
# Else → normal speed
# Estimated Delivery Time (EDT):
# Base speed = 40 km/h
# Calculate time = distance / speed
# Adjust time if speed is reduced
# Route Suggestion (Random):
# Randomly choose one: route A, route B, or route C
 
# Final Output:
# Show selected delivery mode, speed, estimated time, and route chosen.

import random
print("Autonomous Delivery Robot Simulation")
distance = float(input("Enter distance to destination (km): "))
weight = float(input("Enter parcel weight (kg): "))
battery = 100
weather = input("Enter weather condition (clear, rainy, windy): ").lower()

if distance > 10 or weight > 5 or weather =="clear":
    mode = "Drone Mode"
else:
    mode = "Ground Mode"
if battery < 30:
    print("Battery low. Returning to charging station.")
    mode = "Returnning to Charging Station"
else:
    print("Battery sufficient. Continuing delivery.")
    base_speed = 40
if weather in ["rainy", "windy"]:
    speed = base_speed * 0.7
else:
    speed = base_speed
estimated_time = distance / speed
routes = ["Route A", "Route B", "Route C"]
chosen_route = random.choice(routes)
print(f"Delivery Mode: {mode}")
print(f"Speed: {speed:.2f} km/h")
print(f"Estimated Delivery Time: {estimated_time:.2f} hours")
print(f"Chosen Route: {chosen_route}")
print("Delivery simulation completed.")

