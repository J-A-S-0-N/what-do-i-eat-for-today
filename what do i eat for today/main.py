from os import system

ingri_list = ["rice","noddle","salt", "peper", "suger"]

# ingri_bool = [{
#     "rice" : False,
#     "noodle" : False,
#     "salt" : False,
#     "peper" : False,
#     "sugar" : False
# }]
ingri_bool = [(False), (False), (False), (False), (False)]


fried_rice = ["rice", "salt", "sugar"]

def main():
    print("enter an ingrident from the list")
    print(ingri_listl.join(" "))
    inp = input(">>> ")
    ingri_list_counter = 0
    fried_rice_counter = 0

    for c in range(len(ingri_list)):
        fried_rice_counter = 0
        for i in range(len(ingri_list)):
            if ingri_list[ingri_list_counter] == fried_rice[fried_rice_counter]:
                ingri_bool[fried_rice_counter] = True
            fried_rice_counter += 1
        ingri_list_counter += 1
if __name__ == "__main__":
    main()