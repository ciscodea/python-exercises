def run ():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Pedro", "lastname": "Lopez"}

    super_list = [
        {"firstname": "Pedro", "lastname": "Lopez"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Yoselin", "lastname": "Oliva"},
        {"firstname": "Liliana", "lastname": "Jazmin"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 1],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    print("############ Super dictionary ########""")
    for key, value in super_dict.items():
        print(key, "-", value)

    print("############ Super list ########""")
    for key in super_list:
        print(key)

if __name__ == "__main__":
    run()