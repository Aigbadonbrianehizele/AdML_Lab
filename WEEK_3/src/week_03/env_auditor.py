import importlib.metadata
import os
import sys
import platform
import json
import datetime

def get_python_info() -> dict:
    version = platform.python_version()
    executable = sys.executable
    os_platform = sys.platform
    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        venv_path = sys.prefix
    else:
        venv_path = None
    
    
    python_info = {'version': version,'executable':executable,'platform':os_platform,'in_venv':in_venv,'venv_path':venv_path}
    return python_info

def get_installed_packages() -> dict:
    installed_packages = {}
    for dependency  in importlib.metadata.distributions():
        name = dependency.metadata["Name"]
        version = dependency.metadata["Version"]
        installed_packages[name] = version
    return installed_packages

def flag_unpinned(requirements_path: str) -> list:
    flagged = []
    if not os.path.exists(requirements_path):
        raise FileNotFoundError(f"Requiremnts file path not found {requirements_path}")
    with open(requirements_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '==' not in line and '>=' not in line and '~=' not in line:
                flagged.append(line)
    return flagged

def write_snapshot(output_path: str) -> None :
    timestamp = datetime.datetime.now().isoformat()
    snapshot = {'python_info': get_python_info(), 'installed_packages': get_installed_packages(),'timestamp':timestamp }
    os.makedirs(os.path.dirname(output_path), exist_ok = True)
    with open(output_path,'w') as f:
        json.dump(snapshot,f, indent = 2 )
if __name__ == '__main__':
    print(get_python_info())
    print(get_installed_packages())
    print(flag_unpinned('C:/Users/DELL/tmp/test_req.txt'))
    write_snapshot('C:/Users/DELL/tmp/env_snapshot.json')
    open('C:/Users/DELL/tmp/empty_req.txt', 'w').close()
    print(flag_unpinned('C:/Users/DELL/tmp/empty_req.txt')) 
    with open('C:/Users/DELL/tmp/messy_req.txt', 'w') as f:
        f.write('# production deps\n\nnumpy==1.24.0\n\n# dev\npytest\n')
    print(flag_unpinned('C:/Users/DELL/tmp/messy_req.txt'))   
    write_snapshot('C:/Users/DELL/tmp/newdir/deep/snapshot.json')



        