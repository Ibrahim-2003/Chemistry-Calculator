import os

os.system('color a')

reset = True

while reset == True:

    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    masses = {}
    masses['H'] = 1.01
    masses['He'] = 4.00
    masses['Li'] = 6.94
    masses['Be'] = 9.01
    masses['B'] = 10.81
    masses['C'] = 12.01
    masses['N'] = 14.01
    masses['O'] = 16.00
    masses['F'] = 19.00
    masses['Ne'] = 20.18
    masses['Mg'] = 24.31
    masses['Al'] = 26.98
    masses['Si'] = 28.09
    masses['P'] = 30.97
    masses['S'] = 32.07
    masses['Cl'] = 35.45
    masses['Ar'] = 39.95
    masses['K'] = 39.10
    masses['Ca'] = 40.08
    masses['Sc'] = 44.96
    masses['Ti'] = 47.87
    masses['V'] = 50.94
    masses['Cr'] = 52.00
    masses['Mn'] = 54.94
    masses['Fe'] = 55.85
    masses['Co'] = 58.93
    masses['Ni'] = 58.69
    masses['Cu'] = 63.55
    masses['Zn'] = 65.41
    masses['Ga'] = 69.72
    masses['Ge'] = 72.64
    masses['As'] = 74.92
    masses['Se'] = 78.96
    masses['Br'] = 79.90
    masses['Kr'] = 83.80
    masses['Rb'] = 85.47
    masses['Sr'] = 87.62
    masses['Y'] = 88.91
    masses['Zr'] = 91.22
    masses['Nb'] = 92.91
    masses['Mo'] = 95.94
    masses['Tc'] = 98
    masses['Ru'] = 101.07
    masses['Rh'] = 102.91
    masses['Pd'] = 106.42
    masses['Ag'] = 107.87
    masses['Cd'] = 112.41
    masses['In'] = 114.82
    masses['Sn'] = 118.71
    masses['Sb'] = 121.76
    masses['Te'] = 127.60
    masses['I'] = 126.90
    masses['Xe'] = 131.29
    masses['Cs'] = 132.91
    masses['Ba'] = 137.33
    masses['La'] = 138.91
    masses['Hf'] = 178.49
    masses['Ta'] = 180.95
    masses['Na'] = 22.99
    
    chems = str(input('Input your elements here:\n')).split()
    coefficients = []
    elements = []
    subscripts = []

    
    
    for chem in chems:
        res = ''.join(filter(lambda i: i.isdigit(), chem))
        coefficients.append(int(res))
        el = ''.join(filter(lambda i: i.isalpha(), chem))
        elements.append(el.capitalize())
    
    for coefficient in range(len(coefficients)):
        subscripts.append(str(coefficients[coefficient]).translate(SUB))


    def AtomicMass(terms):
        add_things = 0
        index = 0
        formula = ''
        for term in terms:
            add_things += float(masses[term] * float(coefficients[index]))
            if index != len(terms) - 1:
                formula += term + subscripts[index] + ' + '
            elif index == len(terms) - 1:
                formula += term + subscripts[index]
            index += 1
        print('The atomic mass of {} is: {:.2f}g'.format(formula, add_things))
    
    #3F 6O
    
    print('You input: ' + str(chems) + '\n')
    for i in range(len(elements)):
        print('{}{}: {}g * {} = {:.2f}g'.format(elements[i], subscripts[i], masses[elements[i]], int(coefficients[i]), float(float(masses[elements[i]] * float(coefficients[i])))))
    print('\n')
    AtomicMass(elements)
    
    end = str(input("\nExit (Press N)")).upper()
    
    if end != "N":
        reset = True
    elif end == "N":
        reset = False