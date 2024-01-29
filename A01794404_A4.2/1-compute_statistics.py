"""
Req 2. The program shall compute all
descriptive statistics from a file containing
numbers. The results shall be print on a
screen and on a file named
StatisticsResults.txt. All computation MUST
be calculated using the basic algorithms,
not functions or libraries.

"""
import sys
import math


file_path = "/StatisticsInput.txt"


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file]
            
            if not numbers:
                print("The file is empty.")
                return
            
            # Calculating statistics
            total = sum(numbers)
            average = total / len(numbers)
            minimum = min(numbers)
            maximum = max(numbers)
            
            # Calculating standard deviation
            variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
            std_deviation = math.sqrt(variance)

            # Displaying results on the screen
            print(f"Sum: {total}")
            print(f"Average: {average}")
            print(f"Minimum: {minimum}")
            print(f"Maximum: {maximum}")
            print(f"Standard Deviation: {std_deviation}")

            # Writing results to StatisticsResults.txt
            with open("StatisticsResults.txt", 'w') as result_file:
                result_file.write(f"Sum: {total}\n")
                result_file.write(f"Average: {average}\n")
                result_file.write(f"Minimum: {minimum}\n")
                result_file.write(f"Maximum: {maximum}\n")
                result_file.write(f"Standard Deviation: {std_deviation}\n")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <file_path>")
    else:
        file_path = sys.argv[1]
        process_file(file_path)
