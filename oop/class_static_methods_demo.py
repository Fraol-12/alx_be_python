# Calculator class demonstrating static and class methods
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: does not use class or instance attributes
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    # Class method: has access to class attributes via 'cls'
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demo of usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(5, 7)
    print("Sum:", sum_result)

    # Using class method
    product_result = Calculator.multiply(4, 6)
    print("Product:", product_result)