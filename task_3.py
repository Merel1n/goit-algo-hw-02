import numpy as np
dictionary = {
    "(" : ")",
    "{" : "}",
    "[" : "]"
}

def character_check (arr : str) -> str:
    d = []
    for el in arr:
        # якщо відкриваюча дужка — кладемо у стек
        if el in dictionary:
            d.append(el)
        elif el in dictionary.values():
            if not d:
                print(f"{arr} : Несиметрично")
                return
            top = d.pop()
            if dictionary[top] != el:
                print(f"{arr} : Несиметрично")
                return
    if d:
        print(d)
        print(f"{arr} : Несиметрично")
    else:
        print(f"{arr} : Симетрично")
            
character_check("( ){[ 1 ]( 1 + 3 )( ){ }}")
character_check("( 23 ( 2 - 3);")
character_check("( 11 }")