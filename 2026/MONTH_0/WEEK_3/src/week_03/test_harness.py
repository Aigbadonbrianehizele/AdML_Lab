import pickle, os
# Benign pickle
with open('C:/Users/DELL/tmp/benign.pkl', 'wb') as f:
    pickle.dump({'weights': [0.1, 0.2, 0.3], 'epoch': 5}, f)
# Malicious pickle (safe to create — dangerous to load)
class Exploit:
    def __reduce__(self):
        return (os.system, ('echo PWNED',))
with open('C:/Users/DELL/tmp/malicious.pkl', 'wb') as f:
    pickle.dump(Exploit(), f)
print(audit_report('C:/Users/DELL/tmp/benign.pkl'))
print(audit_report('C:/Users/DELL/tmp/malicious.pkl'))
safe_load('C:/Users/DELL/tmp/benign.pkl')    # Should return bytes
safe_load('C:/Users/DELL/tmp/malicious.pkl') # Must raise SecurityError