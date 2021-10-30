def romanToInt(s):
    roman_dict = {
		'I' :1,
		'V' :5,
		'X' :10,
		'L' :50,
		'C' :100,
		'D' :500,
		'M' :1000
        }
    
    s = s.replace('IV','IIII')
    s = s.replace('IX','IIIIIIIII')
    s = s.replace("XL", "XXXX")
    s = s. replace("XC", "XXXXXXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "CCCCCCCCC")

    result = 0
    for c in s:
        result+=roman_dict[c]
    
    return result

if __name__ == '__main__':
    integer = romanToInt("MCMXCIV")
    print(integer)