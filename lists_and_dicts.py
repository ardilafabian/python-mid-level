def main():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Fabian", "lastname": "Ardila"}

    super_list = [
        {"firstname": "Fabian", "lastname": "Ardila"},
        {"firstname": "Facundo", "lastname": "Torres"},
        {"firstname": "Camilo", "lastname": "Cardena"},
        {"firstname": "Pedro", "lastname": "Martinez"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.3,3.5,6.2]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)

    print(super_list)

if __name__ == '__main__':
    main()