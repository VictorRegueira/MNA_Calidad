"""
SalesCalculator Class:

A class to calculate total sales based on product lists and sales data.

Attributes:
    warnings (dict): A dictionary to store warnings during calculation.
    file_names (list): A list to store the names of processed files.

Methods:
    __init__(): Initializes SalesCalculator with
    empty warnings and file_names lists.
    read_file(path: str) -> list: Reads data from a JSON file.
    read_files_in_pair() -> list: Reads pairs of files from command line
    arguments and returns their data.
    find_product(product_name: str, product_list: list) ->
    dict: Finds a product by its name in the product list.
    calculate_sales(product_list: list, sales: list, file_name: str) ->
    float: Calculates total sales based on product list and sales data.
    write_to_file(results: str) -> None: Writes results
    to a file named SalesResults.txt.
    calculate(): Calculates total sales from input files
    and writes results to a file.
"""
import json
import sys
import time


class SalesCalculator:
    """A class to calculate total sales
    based on product lists and sales data."""
    def __init__(self):
        """Initialize SalesCalculator with
        empty warnings and file_names lists."""
        self.warnings = {}
        self.file_names = []

    def read_file(self, path: str) -> list:
        """Read data from a JSON file.

        Args:
            path (str): The path to the JSON file.

        Returns:
            list: The data read from the JSON file.
        """
        try:
            with open(path, encoding='utf8') as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f'Error: The file {path} could not be found.')
            return []
        return data

    def read_files_in_pair(self) -> list:
        """Read pairs of files from command
        line arguments and return their data.

        Returns:
            list: A list containing pairs of product lists and sales data.
        """
        data = []
        for i in range(0, len(sys.argv)-1, 2):
            product_list_file_name, sales_file_name = sys.argv[i+1:i+3]
            if 'ProductList' in sales_file_name:
                product_list_file_name = sales_file_name
                sales_file_name = product_list_file_name
            product_list = self.read_file(product_list_file_name)
            sales = self.read_file(sales_file_name)
            self.file_names.append({'products': product_list_file_name,
                                    'sales': sales_file_name})
            data.append([product_list, sales])
        return data

    def find_product(self, product_name: str, product_list: list) -> dict:
        """Find a product by its name in the product list.

        Args:
            product_name (str): The name of the product to find.
            product_list (list): The list of products to search in.

        Returns:
            dict: The product if found, otherwise an empty dictionary.
        """
        for product in product_list:
            if product.get('title') == product_name:
                return product
        return {}

    def calculate_sales(self, product_list: list, sales: list,
                        file_name: str) -> float:
        """Calculate total sales based on product list and sales data.

        Args:
            product_list (list): The list of products.
            sales (list): The sales data.
            file_name (str): The name of the file being processed.

        Returns:
            float: The total sales amount.
        """
        total = 0
        self.warnings[file_name] = []
        for sale in sales:
            product = self.find_product(sale.get('Product'), product_list)
            if not product:
                self.warnings[file_name].append(
                    f'Product "{sale.get("Product")}" not found')
                continue
            total += sale.get('Quantity', 0) * product.get('price', 0)
        return total

    def write_to_file(self, results: str) -> None:
        """Write results to a file named SalesResults.txt.

        Args:
            results (str): The results to be written to the file.
        """
        with open('SalesResults.txt', 'w', encoding='utf8') as f:
            f.write(results)

    def calculate(self):
        """Calculate total sales from input
        files and write results to a file."""
        start_time = time.time()
        if (len(sys.argv) - 1) % 2 != 0:
            print('Error: You must provide the file paths in pairs.')
            sys.exit()

        data = self.read_files_in_pair()
        output = '\n'

        for i, (product_list, sales) in enumerate(data):
            product_list_file_name = self.file_names[i]['products']
            total = self.calculate_sales(product_list, sales,
                                         product_list_file_name)
            output += f"""- Total sales in {self.file_names[i]
            ["sales"]}:{total: ,.2f}\n"""
            if self.warnings[product_list_file_name]:
                output += f"""\nWarnings: Products not found in list
                {product_list_file_name}:\n\n"""
                output += '\n'.join(self.warnings[product_list_file_name])

        end_time = time.time()
        total_time = end_time - start_time
        output += f'\n\nTotal execution time: {total_time: .2f} seconds\n'

        self.write_to_file(output)
        print(output)


if __name__ == "__main__":
    calculator = SalesCalculator()
    calculator.calculate()
