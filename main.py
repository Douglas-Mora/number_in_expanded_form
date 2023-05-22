def expanded_form(num):
    exponents = [x for x in range(0,len(str(num)))][::-1]
    number_as_list = [char for char in str(num)]
    output = " + ".join([str(int(char)*(10**power)) for char, power in zip(number_as_list,exponents) if char != "0"])
    return output