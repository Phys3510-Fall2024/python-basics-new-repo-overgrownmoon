conversion_factors = {
    ('THz', 'ps'): (1, True),   #linear frequency
    ('ps', 'THz'): (1, True),   #period to linear
    ('THz', 'cm-1'): (33.356, False)    #linear frequency
}

conversion_key = ('THz', 'ps')

if conversion_key in conversion_factors:
    factor, is_inverse = conversion_factors[conversion_key]
    print(f"conversion factor: {factor}")
    print(f"is inverse relationship: {is_inverse}")
else:
    print("Conversion not supported.")