def run():
    # create a list with only squares if x is not divisible of 3
    squares = [x**2 for x in range(1,101) if x % 3 != 0]
    print(squares)

if __name__ == "__main__":
    run()