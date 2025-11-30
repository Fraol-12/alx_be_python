def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    if denom == 0:
        return "Error: Cannot divide by zero."
    
    return str(num / denom)
