'''
this part is the actual assignment
i dont feel like wrangling files
so its all going in the notebook
full credit for finding the conversion factors goes to https://toolbox.lightcon.com/tools/unitconverter
'''

#c is only constant with a known value 3*10^8 m/s
my_convert_dict = {
    ("THz", "ps"): (1, True), #T = 1/f, THz to ps, inverse
    ("THz", "cm^-1"): (33.36, False), #k = w/c, THz to cm^-1, direct
    ("THz", "nm"): (299792, True), #lambda = c/f, THz to nm, inverse
}

convert_dict_key = ("THz", "cm^-1")

if convert_dict_key in my_convert_dict:
    factor, is_inverse = my_convert_dict[convert_dict_key]
    print(f"conversion factor: {factor}")
    print(f"inverse relationship: {is_inverse}")
else:
    print("nope. not in there")

'''
i think the confusion was that i put my assignment in the notebook instead of a new file.
my bad. here it is; i just copied and pasted it here.
'''