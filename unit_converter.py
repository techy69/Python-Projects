#!/usr/bin/env python3
"""
Unit Converter - A versatile converter for length, temperature, and currency
Author: Piyush Chaubey (techy69)
B.C.A Student (2024-27) | UPES
"""

import sys

# Length conversion factors to meters
LENGTH_UNITS = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
    'mile': 1609.34,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254
}

# Currency conversion rates (USD base)
CURRENCY_RATES = {
    'USD': 1,
    'INR': 83.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'JPY': 149.5
}

def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another"""
    if from_unit not in LENGTH_UNITS or to_unit not in LENGTH_UNITS:
        return None
    
    # Convert to meters first, then to target unit
    meters = value * LENGTH_UNITS[from_unit]
    result = meters / LENGTH_UNITS[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin"""
    # Convert to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        return None
    
    # Convert from Celsius to target unit
    if to_unit == 'C':
        result = celsius
    elif to_unit == 'F':
        result = (celsius * 9/5) + 32
    elif to_unit == 'K':
        result = celsius + 273.15
    else:
        return None
    
    return result

def convert_currency(value, from_currency, to_currency):
    """Convert currency from one to another"""
    if from_currency not in CURRENCY_RATES or to_currency not in CURRENCY_RATES:
        return None
    
    # Convert to USD first, then to target currency
    usd_value = value / CURRENCY_RATES[from_currency]
    result = usd_value * CURRENCY_RATES[to_currency]
    return result

def main():
    if len(sys.argv) != 5:
        print("Usage: python unit_converter.py <type> <value> <from_unit> <to_unit>")
        print("Types: length, temperature, currency")
        print("\nExamples:")
        print("  python unit_converter.py length 5 km m")
        print("  python unit_converter.py temperature 100 C F")
        print("  python unit_converter.py currency 100 USD INR")
        sys.exit(1)
    
    conversion_type = sys.argv[1].lower()
    try:
        value = float(sys.argv[2])
    except ValueError:
        print("Error: Value must be a number")
        sys.exit(1)
    
    from_unit = sys.argv[3]
    to_unit = sys.argv[4]
    
    result = None
    
    if conversion_type == 'length':
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == 'temperature':
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == 'currency':
        result = convert_currency(value, from_unit, to_unit)
    else:
        print(f"Error: Unknown conversion type '{conversion_type}'")
        sys.exit(1)
    
    if result is None:
        print(f"Error: Invalid units for {conversion_type} conversion")
        sys.exit(1)
    
    print(f"{value} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()
