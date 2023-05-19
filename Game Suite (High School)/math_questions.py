import random
import math
# defining basic math skills for both age groups, just need to change numbers
def basic_math_skills(number1, number2):
# Gets random question from  4 types, asks question, if input is == answer return True, else reutrns False
    basic_skills_q = random.randint(1, 4)

    while True:
        try:
            result = False # result is wrong

        # Basic Math Skills
        
            if basic_skills_q == 1:
                answer = number1 + number2
                add_q = int(input(f"Addition: {number1} + {number2} = "))

                if add_q == answer:
                    return [not(result), answer] # if correct returns True + answer
                return [result, answer] # else return False, this means it is wrong + answer

            elif basic_skills_q == 2:
                answer = number1 - number2
                sub_q = int(input(f"Subtraction: {number1} - {number2} = "))
            
                if sub_q == answer:
                    return [not(result), answer] # if correct returns True
                return [result, answer] # else return False, this means it is wrong

            elif basic_skills_q == 3:
                answer = number1 * number2
                mult_q = int(input(f"Multiplication: {number1} x {number2} = "))

                if mult_q == answer:
                    return [not(result), answer] # if correct returns True
                return [result, answer] # else return False, this means it is wrong

            else:
                answer = round(number1 / number2)
                print("Round to nearest whole number.")
                div_q_rounded = round(float(input(f"Division: {number1} ÷ {number2} = ")))

                if div_q_rounded == answer:
                    return [not(result), answer] # if correct returns True
                return [result, answer] # else return False, this means it is wrong
        
        except ValueError:
            print("Invalid Input, try again")
            print()







# Measurement
def measurement(m_length, m_length2):

    measure_shape = random.randint(1,4) # chooses shape for q's (only 3 shapes)
    measure_q1 = random.randint(1,2) 
    measure_q2 = random.randint(1,2) 
    measure_q3 = random.randint(1, 2)
    unit1 = random.randint(1, 4) # mm, cm, m, km

    while True:
        try:
        
            # Function return True if answer is correct and False if it isn't correct

            if measure_shape == 1: # Square

                if measure_q1 == 1: # Perimeter 
                    answer_m1 = m_length * 4
                    m_1 = int(input(f"What is the total perimeter of a square with side length {m_length} ? "))
                    if m_1 == answer_m1:
                        return [True, answer_m1]
                    return [False, answer_m1]

                elif measure_q1 == 2: # Area
                    answer_m1 = m_length ** 2
                    m_1 = int(input(f"What is the total area of a square with side length {m_length} ? "))
                    if m_1 == answer_m1:
                        return [True, answer_m1]
                    return [False, answer_m1]


            elif measure_shape == 2: # Triangle

                if measure_q2 == 1: # Perimeter
                    answer_m2 = m_length * 3
                    m_2 = int(input(f"What is the total perimeter of an equilateral triangle with side length {m_length} ? "))
                    if m_2 == answer_m2:
                        return [True, answer_m2]
                    return [False, answer_m2]

                elif measure_q2 == 2: # Area
                    answer_m2 = (1/2) * m_length * m_length2
                    m_2 = float(input(f"What is the total area of an equilateral triangle with base {m_length} and height {m_length2} ? "))
                    if m_2 == answer_m2:
                        return [True, answer_m2]
                    return [False, answer_m2]

            elif measure_shape == 3: # Rectangle

                if measure_q3 == 1: # Perimeter
                    answer_m3 = (2 * m_length) + (2 * m_length2)
                    m_3 = int(input(f"What is the total perimeter of a rectangle with base {m_length} and length {m_length2} ? "))
                    if m_3 == answer_m3:
                        return [True, answer_m3]
                    return [False, answer_m3]

                elif measure_q3 == 2: # Area
                    answer_m3 = m_length * m_length2
                    m_3 = int(input(f"What is the total area of a rectangle with base {m_length} and length {m_length2} ? "))
                    if m_3 == answer_m3:
                        return [True, answer_m3]
                    return [False, answer_m3]

            else:  # converting measurements

                print("Round to 2 decimal places (where necessary).")

                if unit1 == 1:
                    answer_m4 = round(m_length / 10, 2)
                    m_4 = float(input(f"Convert {m_length} mm to cm : "))
                    if m_4 == answer_m4:
                        return [True, answer_m4]
                    return [False, answer_m4]
                
                elif unit1 == 2:
                    answer_m4 = round(m_length * 10, 2)
                    m_4 = float(input(f"Conver {m_length} cm to mm : "))
                    if m_4 == answer_m4:
                        return [True, answer_m4]
                    return [False, answer_m4]

                elif unit1 == 3:
                    answer_m4 = round(m_length * 100, 2)
                    m_4 = float(input(f"Conver {m_length} m to cm : "))
                    if m_4 == answer_m4:
                        return [True, answer_m4]
                    return [False, answer_m4]
                
                else: 
                    answer_m4 = round(m_length * 1000, 2)
                    m_4 = float(input(f"Conver {m_length} km to m : "))
                    if m_4 == answer_m4:
                        return [True, answer_m4]
                    return [False, answer_m4]
        
        except ValueError:
            print("Invalid Input, try again.")
            print()
            continue
