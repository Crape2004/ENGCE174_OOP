def generate_pattern_1(height, current=1):
    if current > height:
        return
    print('* ' * current)
    generate_pattern_1(height, current + 1)

def generate_pattern_2(height, current=1):
    if current > height:
        return
    generate_pattern_2(height, current + 1)
    print('* ' * current)

def generate_pattern_3(height, current=0):
    if current >= height:
        return
    print(' ' * (height - current - 1) + '* ' * (current + 1))
    generate_pattern_3(height, current + 1)

def generate_pattern_4(n, height=0, result=""):
    if height == n:
        return result
    print(" " * height + "* " * (n - height)) 
    return generate_pattern_4(n, height + 1, result)

def generate_pattern_5(height, current=0):
    if current >= height:
        return
    print(' ' * 2 * (height - current - 1) + '* ' * (current + 1))
    generate_pattern_5(height, current + 1)

def print_patterns(height):
    print("Pattern 1:")
    generate_pattern_1(height)
    print('-------------')

    print("Pattern 2:")
    generate_pattern_2(height)
    print('-------------')

    print("Pattern 3:")
    generate_pattern_3(height)
    print('-------------')

    print("Pattern 4:")
    generate_pattern_4(height)
    print('-------------')

    print("Pattern 5:")
    generate_pattern_5(height)
    print('-------------')

def main():
    try:
        user_input = input("Enter height (enter 'q' to quit): ")
        
        if user_input.lower() != 'q':
            height = int(user_input)
            if height > 0:
                print_patterns(height)
            else:
                print("Height must be a positive integer.")
    
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

if __name__ == "__main__":
    main()