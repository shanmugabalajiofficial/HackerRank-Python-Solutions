#Validating Roman Numerals


regex_pattern = r"^(M{,3})(C[MD]|D?C{,3}|)(X[CL]|L?X{,3})(I[VX]|V?I{,3})$"    # Do not delete 'r'.
import re
print(str(bool(re.match(regex_pattern, input()))))
