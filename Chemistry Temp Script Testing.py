SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
NONSUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")

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
masses['Na'] = 22.99
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

def CalcMass(elements, subscripts, coefficients, factor):
    add_things = 0
    index = 0
    formula = ''
    for term in elements:
        add_things += float(masses[term] * float(coefficients[index])) * int(factor)
        if index != len(elements) - 1:
            formula += term + subscripts[index] + ' + '
        elif index == len(elements) - 1:
            formula += term + subscripts[index]
        index += 1
    if factor != 1:
        formula += ' × ' + str(factor)
    fin = 'The mass of {} is: {:.2f}g'.format(formula, add_things)
    return fin

def ElemIn(elem_in):
    chems = str(elem_in)
    chems = str(chems).translate(NONSUB)
    coefficients = []
    subscripts = []
    elements = []
    factor = 1
    temp_factor_string = ''
    chems_sep_string_not_list = ''

    res_pos = [i for i, e in enumerate(chems+'A') if e.isupper()]
    chems_sep = [chems[res_pos[j]:res_pos[j + 1]]
                for j in range(len(res_pos)-1)]


    for chem in chems:
        if chem.isdigit():
            temp_factor_string += chem
        else:
            break
    if temp_factor_string != '':
        factor = int(temp_factor_string)
    elif temp_factor_string == '':
        factor = 1
        
    for chem in chems_sep:
        chems_sep_string_not_list += chem + ' '

    chems_sep_string_not_list = chems_sep_string_not_list.split()


    for chem in chems_sep_string_not_list:
        res = ''.join(filter(lambda i: i.isdigit(), chem))
        if res == '':
            res = '1'
        res_al = ''.join(filter(lambda i: i.isalpha(), chem))
        coefficients.append(int(res))
        elements.append(res_al)

    for coefficient in range(len(coefficients)):
        subscripts.append(str(coefficients[coefficient]).translate(SUB))

    ret_str = 'Your input: {} '.format(factor)
    for i in range(len(elements)):
        if coefficients[i] != 1:
            ret_str += '{}{}'.format(elements[i], subscripts[i])
        elif coefficients[i] == 1:
            ret_str += '{}'.format(elements[i])
    ret_str += '\n\n'
    for i in range(len(elements)):
        ret_str += '{}{}: {}g * {} = {:.2f}g \n'.format(elements[i], subscripts[i], masses[elements[i]], int(coefficients[i]), float(float(masses[elements[i]] * float(coefficients[i]))))
    if factor != 1:
        ret_str += 'The mass is multiplied by a factor of {}.\n'.format(factor)
    ret_str += '\n'
    ret_str += str(CalcMass(elements, subscripts, coefficients, factor))
    return ret_str


def gcd (a,b):
    if (b == 0):
        return a
    else:
        return gcd (b, a % b)


def EmpiricalFormula(raw_formula):
    chems = str(raw_formula)
    chems = str(chems).translate(NONSUB)
    coefficients = []
    subscripts = []
    elements = []
    factor = 1
    temp_factor_string = ''
    chems_sep_string_not_list = ''

    res_pos = [i for i, e in enumerate(chems+'A') if e.isupper()]
    chems_sep = [chems[res_pos[j]:res_pos[j + 1]]
                for j in range(len(res_pos)-1)]


    for chem in chems:
        if chem.isdigit():
            temp_factor_string += chem
        else:
            break
    if temp_factor_string != '':
        factor = int(temp_factor_string)
    elif temp_factor_string == '':
        factor = 1
        
    for chem in chems_sep:
        chems_sep_string_not_list += chem + ' '

    chems_sep_string_not_list = chems_sep_string_not_list.split()


    for chem in chems_sep_string_not_list:
        res = ''.join(filter(lambda i: i.isdigit(), chem))
        if res == '':
            res = '1'
        res_al = ''.join(filter(lambda i: i.isalpha(), chem))
        coefficients.append(int(res))
        elements.append(res_al)

    simp = coefficients[0]
    for c in coefficients[1::]:
        simp = gcd(simp , c)

    answer = [int(i / simp) for i in coefficients]
    
    simp_subscripts = []

    for coefficient in range(len(answer)):
        simp_subscripts.append(str(answer[coefficient]).translate(SUB))

    for coefficient in range(len(coefficients)):
        subscripts.append(str(coefficients[coefficient]).translate(SUB))

    ret_str = 'The empirical formula for '
    for i in range(len(elements)):
        if factor != 1:
            ret_str += '{}'.format(factor)
        ret_str += '{}{}'.format(elements[i], subscripts[i])
    ret_str += ' is: \n'

    
    for i in range(len(elements)):
        
        ret_str += '{}{}'.format(elements[i], simp_subscripts[i])
    
    return ret_str

print(EmpiricalFormula('2C6H9'))