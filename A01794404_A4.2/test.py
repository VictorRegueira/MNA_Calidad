import sys
import math

file_path = "VictorRegueira/MNA_Calidad/A01794404_A4.2/StatisticsInput.txt"


with open(file_path, 'r') as file:
    numbers = [float(line.strip()) for line in file]
    
    if not numbers:
        print("The file is empty.")
        
print(numbers)