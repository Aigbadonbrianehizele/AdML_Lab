import os 
class SecurityError(Exception):
    pass
DANGEROUS_OPCODES = {
    b'\x63': 'GLOBAL',   # imports arbitrary module.attribute
    b'\x52': 'REDUCE',   # calls arbitrary callable
    b'\x62': 'BUILD',    # calls __setstate__ on arbitrary object
    b'\x69': 'INST',     # creates arbitrary class instance
    b'\x6f': 'OBJ',      # creates object from stack
    b'\x65': 'APPENDS',  # not dangerous alone — note for context
}    

def scan_pickle(filepath: str) -> list:
    with open(filepath,'rb') as f:
        data = f.read()
    results = []
    for offset, byte in enumerate(data):
        if bytes([byte]) in DANGEROUS_OPCODES:
            results.append({'opcode': DANGEROUS_OPCODES[bytes([byte])], 'offset': offset})
    return results
def safe_load(filepath: str) -> bytes:
    scanpath = scan_pickle(filepath)
    if len(scanpath) != 0:
        raise SecurityError
    else:
        with open(filepath,'rb') as f:
            data_1 = f.read()
        return data_1
def audit_report(filepath:str) -> dict:
    audit = scan_pickle(filepath)
    dangerous_count = len(audit)

    if dangerous_count == 0:
        risk_level = "CLEAN"
    elif 1 <= dangerous_count <= 2:
        risk_level = "SUSPICIOUS"
    elif dangerous_count >= 3:
        risk_level = "MALICIOUS"
    full_audit = {"filepath":filepath, "file_size_bytes":os.path.getsize(filepath), "opcodes_found": audit, "dangerous_count": dangerous_count, "risk_level": risk_level, "safe_to_load": risk_level == 'CLEAN'}
    return full_audit
if __name__ == "__main__":
    open('C:/Users/DELL/tmp/empty.pkl', 'wb').close()
    print(audit_report('C:/Users/DELL/tmp/empty.pkl')) 
