# Bouncy Numbers Calculator

## Description
This Python program finds and analyzes "bouncy" numbers - positive integers that are neither strictly increasing nor strictly decreasing. A number is considered:
- **Increasing** if no digit is exceeded by the digit to its left (e.g., 134468)
- **Decreasing** if no digit is exceeded by the digit to its right (e.g., 66420)
- **Bouncy** if it's neither increasing nor decreasing (e.g., 155349)

The program can calculate the first number at which the proportion of bouncy numbers reaches a specified percentage threshold.

## Features
- Efficient bouncy number detection
- Percentage threshold calculation
- Type hints for better code maintainability
- Comprehensive error handling
- Well-documented codebase

## Usage
```python
calculator = BouncyNumberCalculator()
result, percentage = calculator.find_proportion_threshold(99)
print(f"Result: {result}")
```

## Requirements
- Python 3.6+

## Installation
Clone the repository and run the script:
```bash
git clone https://github.com/yourusername/Bouncy-number.git
cd Bouncy-number
python Bouncy.py
```

## License
MIT License
