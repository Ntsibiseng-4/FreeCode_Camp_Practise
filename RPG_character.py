full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):


    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
      return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    str_bar = "" + "●" * strength + "○" * (10 - strength)
    int_bar = "" + "●" * intelligence + "○" * (10 - intelligence)
    cha_bar = " " + "●" * charisma + "○" * (10 - charisma)

    return f'{name}\nSTR {str_bar}\nINT {int_bar}\nCHA{cha_bar}'

not_name = create_character(23, 4, 2, 1)
print(not_name)
is_empty = create_character('',4, 2, 1)
print(is_empty)
too_long = create_character('NtsibisengLeshabana', 4, 2, 1)
print(too_long)
space = create_character('your name', 4, 4, 2)
print(space)

not_argu = create_character("ren", 3.2, "3", 1.1)
print(not_argu)
not_4 = create_character("ren", 5, 6, 7)
print(not_4)

print(create_character('ren', 4, 2, 1))