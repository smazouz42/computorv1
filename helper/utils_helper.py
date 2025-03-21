import re
from helper.math_helpers import gcd
from helper.colors import purpel, reset,green
def custom_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    num = numerator // common_divisor
    den = denominator // common_divisor
    if den == 1:
        print(f"{purpel}fraction form{reset} {num}")
    else:
        print(f"{purpel}fraction form {reset} {num} / {den}")


def parse_equation(equation):
    parts = equation.split('=')
    if len(parts) != 2:
        raise ValueError("Invalid equation format. The equation must contain exactly one '=' symbol.")
    
    left_terms = parse_terms(parts[0])
    right_terms = parse_terms(parts[1])
    
    combined_terms = combine_terms(left_terms, right_terms)
    
    return combined_terms

def parse_terms(part):
    part = part.replace(" " , "")
    
    if part == "":
        return {0: 0}

    term_items = re.split(r'(?=[+-])', part)
    term_pattern = re.compile(r'([+-]?\d*(\.\d+)?)\*?X?(\^(\d+))?')
    
    term_dict = {}
    for item in term_items:
        match = term_pattern.fullmatch(item)
        if match:
            coefficient = match.group(1)      
            if coefficient in ["", "+", "-"]:
                coefficient = coefficient + "1" if coefficient else "1"
            coefficient = float(coefficient)
            exponent = match.group(4)
                
            if exponent is None:
                exponent = 1 if "X" in item else 0
            exponent = int(exponent)

            if exponent in term_dict:
                term_dict[exponent] += coefficient
            else:
                term_dict[exponent] = coefficient
        else:
            raise ValueError(f"Invalid term '{item}' in the equation.")
    
    return term_dict
def combine_terms(left_terms, right_terms):
    combined_terms = left_terms.copy()
    for exponent, coefficient in right_terms.items():
        if exponent in combined_terms:
            combined_terms[exponent] -= coefficient
        else:
            combined_terms[exponent] = -coefficient
    for exp in list(combined_terms.keys()):
        if combined_terms[exp] == 0 and exp :
            del combined_terms[exp]
    if 0 not in combined_terms:
        combined_terms[0] = 0
    return combined_terms

def reduce_equation(combined_terms):
    reduced_form = " + ".join([f"{coef} * X^{exp}" for exp, coef in sorted(combined_terms.items())])
    reduced_form = reduced_form.replace("+ -", "- ")
    return reduced_form

def welcome_message():

    message = f"""
    {green}+---------------------------------------------+
    |      Welcome to the Polynomial Solver!      |
    +---------------------------------------------+
    |                                             |
    |    This tool helps solve polynomial         |
    |    equations of degree 2 or lower.          |
    |                                             |
    +---------------------------------------------+{reset}
    """
    print(message)
