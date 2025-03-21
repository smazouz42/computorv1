import sys
from helper.math_helpers import _sqrt
from helper.colors import red, yellow
from helper.utils_helper import *


def solve_equation(combined_terms, degree):
    print("-"*47)
    print(f"| {purpel}Solve the equation depending on the degree.{reset} |")
    print("-"*47)

    if degree == 2:
        a = combined_terms.get(2, 0)
        b = combined_terms.get(1, 0)
        c = combined_terms.get(0, 0)
        discriminant = b*b - 4*a*c
        if discriminant > 0:
            root1 = (-b + _sqrt(discriminant)) / (2*a)
            root2 = (-b - _sqrt(discriminant)) / (2*a)
            if (-b + _sqrt(discriminant)) % (2*a) != 0:
                custom_fraction((-b + _sqrt(discriminant)),(2*a))
            if (-b - _sqrt(discriminant)) % (2*a) != 0:
                custom_fraction((-b - _sqrt(discriminant)),(2*a))
            
            print(f"{yellow}Discriminant is strictly positive, the two solutions are:{reset}\n{root1:.6f}\n{root2:.6f}")
        elif discriminant == 0:
            root = -b / (2*a)
            print(f"{yellow}Discriminant is zero, the solution is:{reset}\n{root:.6f}")
        else:
            print(f"{yellow}Discriminant is strictly negative, no real solutions.{reset:.6f}")
    
    elif degree == 1:
        b = combined_terms.get(1, 0)
        c = combined_terms.get(0, 0)
        if b != 0:
            root = -c / b
            print(f"{yellow}The solution is:{reset}\n{root}")
            if -c % b != 0:
                custom_fraction(-c,b)

        else:
            print("{yellow}No solution.{reset}")
    
    elif degree == 0:
        c = combined_terms.get(0, 0)
        if c == 0:
            print("{yellow}All real numbers are solutions.{reset}")
        else:
            print("{yellow}No solution.{reset}")
            
if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print(f"{red}Usage: ./computor \"equation\"")
        sys.exit(1)
    welcome_message()
    equation = sys.argv[1]
    try:
        combined_terms = parse_equation(equation)
        reduced_form = reduce_equation(combined_terms)

        print(f"{yellow}Reduced form{reset}: {reduced_form} = 0")
        print("-"*18)
        print(f"| {purpel}Get the degree{reset} |")
        print("-"*18)

        degree = max(combined_terms.keys())
        print(f"{yellow}Polynomial degree{reset}: {degree}")
    
        if degree > 2:
            print(f"{red}The polynomial degree is strictly greater than 2, I can't solve.")
            sys.exit(1)
        solve_equation(combined_terms, degree)
    except Exception as e:
        print(f"{red}An error occurred: {e}")
        sys.exit(1)