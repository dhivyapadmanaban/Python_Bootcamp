def romanToInt(s):
    roman_dict = {
       "IV" : 4,
       "IX" : 9,
       "XL" : 40,
       "XC" : 90,
       "CD" : 400,
       "CM" : 900,
       "I" : 1,
       "V" : 5,
       "X" : 10,
       "L" : 50,
       "C" : 100,
       "D" : 500,
       "M" : 1000
        }
        
    result = 0
        
    while s:
            
            for key,value in roman_dict.items():
                if key in s:
                    result += value*s.count(key)
                    s = s.replace(key,'')
                    
    return result

if __name__ == '__main__':
    integer = romanToInt("LVIII")
    print(integer)