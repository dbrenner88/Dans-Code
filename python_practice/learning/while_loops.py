x = 0

while x < 10:
    x += 1
    print(x)
end_program = False

while end_program is False:
    print("Hello")
    test = input("Write is: ").lower
    print(test)
    if test == "is":
        end_program = True
        print(end_program)
