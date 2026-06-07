with open('C:/Users/DELL/tmp/benign.pkl', 'rb') as f:
    data = f.read()

DANGEROUS_OPCODES = {
    b'\x63': 'GLOBAL',   # imports arbitrary module.attribute
    b'\x52': 'REDUCE',   # calls arbitrary callable
    b'\x62': 'BUILD',    # calls __setstate__ on arbitrary object
    b'\x69': 'INST',     # creates arbitrary class instance
    b'\x6f': 'OBJ',      # creates object from stack
    b'\x65': 'APPENDS',  # not dangerous alone — note for context
}    

for byte in data:
    print(byte)
    break
print(bytes([128]) in DANGEROUS_OPCODES)