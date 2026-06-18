from week_03.model_loader import audit_report, SecurityError
from week_03.env_auditor import get_python_info, get_installed_packages, write_snapshot, flag_unpinned


import json, os, datetime, sys
def pre_flight_check(model_path: str, requirements_path: str = None) -> dict:
    warnings = []
    python_info =  get_python_info()
    packages = get_installed_packages()
    env_auditor = {'python_info':python_info, 'installed_packages_count':len(packages)}
    if requirements_path is not None:
        try:
            unpinned = flag_unpinned(requirements_path)
        except FileNotFoundError as e:
            unpinned =  None
            warnings.append("The requirement path can't be found")
    else:
        unpinned =  None
    try:
        audit =  audit_report(model_path)
    except FileNotFoundError:
        print(f"{model_path} doesn't exist")
        audit = {'risk_level': "MALICIOUS" ,'dangerous_count': 0 , 'opcodes_found': [],}
    if python_info['in_venv'] == False:
        warnings.append("You are currently trying to make use of pipeline outside the virtual environment")


    if 'risk_level' in audit and audit['risk_level'] == "MALICIOUS" or 'risk_level' in audit and audit['risk_level'] == "SUSPICIOUS"  or not python_info['in_venv']:
        safe_to_proceed = False
    else:
        safe_to_proceed = True
    
    timestamp = datetime.datetime.now().isoformat()
    pickle_scan = {'risk_level': audit['risk_level'], 'dangerous_count':audit['dangerous_count'], 'opcodes_found': audit['opcodes_found']}
    required_keys = {'env_snapshot':env_auditor, 'unpinned_deps': unpinned, 'pickle_scan': pickle_scan,'safe_to_proceed': safe_to_proceed, 'warnings':warnings , 'timestamp':timestamp}
    return required_keys
def run_and_save(model_path: str, requirements_path: str = None, output_path: str = 'output/week03_supply_chain_report.json'):
    pre_check = pre_flight_check(model_path, requirements_path)
    os.makedirs(os.path.dirname(output_path), exist_ok = True)
    with open(output_path, 'w') as f:
        json.dump(pre_check, f, indent = 2)
    if pre_check['safe_to_proceed'] == True :
        print(f"SAFE TO PROCEED")
    elif pre_check['pickle_scan']['risk_level'] == "MALICIOUS":
        print(f"BLOCKED — BECAUSE OF MALICIOUS OPCODES")
    elif pre_check['pickle_scan']['risk_level'] == "SUSPICIOUS":
        print(f"BLOCKED — BECAUSE OF SUSPICIOUS PICKLES")
    elif pre_check['pickle_scan']['risk_level'] == "MALICIOUS" and pre_check['pickle_scan']['dangerous_count'] == 0 and pre_check['pickle_scan']['opcodes_found'] == []:
        print(f"BLOCKED — BECAUSE THE FILE IS EMPTY")
    elif pre_check['env_snapshot']['python_info']['in_venv'] == False:
        print(f"BLOCKED — BECAUSE YOU ARE OPERATING OUTSIDE THE VIRTUAL ENVIRONMENT")


