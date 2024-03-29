"""
convert_numbers_with_exceptions_at_end.py

This script processes numerical data from text files within a specified folder,
converts each number to binary and hexadecimal bases,
displays the results, writes the results to a text file,
and shows ValueErrors and total execution time at the end.

Author: Victor Regueira
Date: January 30, 2024
"""

import os
import time

FOLDER_PATH = "P2"
FILE_EXTENSION = ".txt"
OUTPUT_FILE_NAME = "ConversionResults.txt"


def convert_numbers_in_file(file_path: str, output_file, error_list) -> None:
    """
    Convert numbers in a file to binary and hexadecimal bases.

    :param file_path: Path to the file
    :param output_file: File object to write the results
    :param error_list: List to store encountered ValueErrors
    :return: None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output_file.write(f"\nConverting numbers in file: {file_path}\n")
            for line in file:
                try:
                    num = int(line.strip())
                    binary_representation = format(num,'b')
                    hexadecimal_representation = format(num, '02X')
                    original = f"Original: {num}"
                    binary = f"Binary: {binary_representation}"
                    hexadecimal = f"Hexadecimal: {hexadecimal_representation}"
                    result_line = original + "\t" + binary + "\t"+ hexadecimal + "\n"
                    print(result_line)
                    output_file.write(result_line)

                except ValueError as ve:
                    error_list.append(f"Invalid data in {file_path}. \
                    Skipping line: {line.strip()}. Error: {ve}")

    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")


def convert_numbers_in_folder(folder_path: str) -> list:
    """
    Convert numbers in all text files in a folder to binary and hexadecimal bases.

    :param folder_path: Path to the folder
    :return: List of encountered ValueErrors
    """
    error_list = []
    with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as output_file:
        # List all files in the folder with the specified extension
        file_list = [f for f in os.listdir(folder_path) if f.endswith(FILE_EXTENSION)]

        # Convert numbers in each file
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            convert_numbers_in_file(file_path, output_file, error_list)

    return error_list


if __name__ == "__main__":
    start_time = time.time()

    try:
        if not os.path.isdir(FOLDER_PATH):
            raise FileNotFoundError(f"Invalid folder path: {FOLDER_PATH}")

        errors = convert_numbers_in_folder(FOLDER_PATH)
        print(f"\nResults written to {OUTPUT_FILE_NAME}")

        if errors:
            print("\nEncountered ValueErrors:")
            for error in errors:
                print(error)

    finally:
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time} seconds")
