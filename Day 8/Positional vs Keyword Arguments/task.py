# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
# 
# 
# greet_with_name("Jack Bauer")

def calculate_love_score(name1, name2):
    T_count1=name1.lower().count("T".lower())
    R_count1=name1.lower().count("R".lower())
    U_count1=name1.lower().count("U".lower())
    E_count1=name1.lower().count("E".lower())
    T_count2=name2.lower().count("T".lower())
    R_count2 = name2.lower().count("R".lower())
    U_count2 = name2.lower().count("U".lower())
    E_count2 = name2.lower().count("E".lower())
    print(f"Letter T appears {T_count1} times in {name1}")
    print(f"Letter R appears {R_count1} times in {name1}")
    print(f"Letter U appears {U_count1} times in {name1}")
    print(f"Letter E appears {E_count1} times in {name1}")
    print(f"Letter T appears {T_count2} times in {name2}")
    print(f"Letter R appears {R_count2} times in {name2}")
    print(f"Letter U appears {U_count2} times in {name2}")
    print(f"Letter E appears {E_count2} times in {name2}")
    lover_score=print (f"Total lover score {T_count1+R_count1+U_count1+E_count1}{T_count2+R_count2+U_count2+E_count2}")
    
calculate_love_score(name1="Alok", name2="Shreeta")