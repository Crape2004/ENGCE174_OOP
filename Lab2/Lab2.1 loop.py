while True:
    user_input = input("Enter height (enter 'q' to quit): ")
    
    if user_input == 'q':
        break
    
    if user_input.isdigit():
        height = int(user_input)
        
        # Pattern 1
        if height >= 1:
            print("Pattern 1:")
            for i in range(1, height + 1):
                print('* ' * i)
            print('-------------')
        
        # Pattern 2
        if height >= 1:
            print("Pattern 2:")
            for n in range(height, 0, -1):
                print('* ' * n)
            print('-------------')
        
        # Pattern 3
        print("Pattern 3:")
        for i in range(height):
            for j in range(height - i - 1):
                print(" ", end="")
            for k in range(i + 1):
                print("*", end=" ")
            print()
        print('-------------')
        
        # Pattern 4
        print("Pattern 4:")
        for i in range(height, 0, -1):
            for j in range(height - i):
                print(" ", end="")
            for k in range(i):
                print("*", end=" ")
            print()
        print('-------------')
        
        # Pattern 5
        print("Pattern 5:")
        for i in range(height):
            for j in range(height - i - 1):
                print(" ", end=" ")
            for k in range(i + 1):
                print("*", end=" ")
            print()
        print('-------------')

    else:
        print("Invalid input. Please enter a number or 'q' to quit.")