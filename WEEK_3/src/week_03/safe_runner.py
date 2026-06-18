import subprocess, shlex, os
DANGEROUS_FLAGS = {'-c', '-m'}
ALLOWED_COMMANDS = {'python3', 'python', 'git', 'pip3', 'pip'}
INJECTION_CHARS  = set('&|;$`><!')

def shell_injection_check(cmd: list) -> list:
    flagged = []
    for arg in cmd:
        for char in arg:
            if char in INJECTION_CHARS:
                flagged.append(arg)
                break
    return flagged


def safe_exec(cmd: list, timeout: int = 30) -> dict:
    if type(cmd) is not list:
        raise TypeError("CMD IS NOT A LIST")
    if cmd[0] not in ALLOWED_COMMANDS:
        raise ValueError(f"COMMAND {cmd[0]} IS NOT FOUND IN ALLOWED_COMMANDS ")
    for i in cmd[1:]:
        if i in DANGEROUS_FLAGS:
            raise ValueError(f"COMMAND {i} HAS FOUND IN DANGEROUS_FLAGS")
    if len(shell_injection_check(cmd)) > 0:
        raise ValueError("CMD ARGUMENTS ARE NOT ALLOWED")
    try:
        result = subprocess.run(cmd, capture_output = True, text =  True, timeout = timeout)
    except subprocess.TimeoutExpired:
        raise TimeoutError("Process exceeded Timeout")
    safeexec = {'returncode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    return safeexec

def run_python_script( script_path: str, args: list = None, timeout: int = 60) -> dict:
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The file path {script_path} is not found")
    cmd = ['python3', script_path] + (args or [])
    return safe_exec(cmd, timeout)

if __name__ == "__main__":
    safe_exec(['python3', '-c', 'import time; time.sleep(60)'], timeout=2)
#    print(safe_exec(['python3', '-c', 'import os; os.system("id")']))
#    print(safe_exec(['curl', 'https://x.com']))
#    print(safe_exec('python3 --version'))
#    print(safe_exec(['python3', '--version']))
#    print(safe_exec(['git', 'log', '--oneline', '-3']))
#    print(shell_injection_check(['git', 'log', '--oneline; rm -rf /']))




