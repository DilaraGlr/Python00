import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    sys.exit(1)
elif len(sys.argv) == 2:
    try:
        nb = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit(1)
    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

# if len(sys.argv) > 2:
#         assert False, "more than one argument is provided"
# elif len(sys.argv) == 2:
#     try:
#         nb = int(sys.argv[1])
#     except ValueError:
#         assert False, "argument is not an integer"
#     if nb % 2 == 0:
#         print("I'm Even.")
#     else:
#         print("I'm Odd.")
      
    
    
    
