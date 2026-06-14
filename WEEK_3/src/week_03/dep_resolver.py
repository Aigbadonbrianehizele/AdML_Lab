import os
import sys
sys.path.insert(0, r'C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\src')
from week_02.attack_graph import AttackGraph
g = AttackGraph
def parse_requirements(filepath: str) -> dict :
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file path {filepath} is not found")
    pinned = {}
    with open(filepath, encoding='utf-8-sig') as f:
        for line in f:
            line =  line.strip()
            if not line or line.startswith('#'):
                continue
            if '==' in line or '>=' in line or '~=' in line:
                for op in ['==','>=','~=']:
                    if op in line:
                        name = line.split(op)[0].split('[')[0]
                        package = line.split(op)[1]
                        if name in pinned:
                            pinned[name].append(package)
                        else:
                            pinned[name] = [package]
                        break
            else:
                name = line.split('[')[0]
                package = None
                if name in pinned:
                    pinned[name].append(package)
                else:
                    pinned[name] = [package]
    return pinned

def flag_unpinned(pinned: dict) -> list:
    unpinned = []
    for key, value in pinned.items():
        if pinned[key] == [None]:
            unpinned.append(key)
    return unpinned


def flag_duplicates(pinned: dict) -> list:
    duplicates = []
    for key, value in pinned.items():
        if len(pinned[key]) > 1:
            duplicates.append(key)
    return duplicates

def build_dep_graph(pinned: dict) -> AttackGraph:
    g = AttackGraph()
    g.add_node("UNRESOLVED")
    g.add_node("RESOLVED")   
    for key in pinned:
        g.add_node(key)
        if pinned[key] == [None]:
            g.add_edge(key, "UNRESOLVED", 1.0)
        if pinned[key] != [None]:
            g.add_edge(key, "RESOLVED", 0.0)
    return g
    




r = parse_requirements('C:/Users/DELL/tmp/test_req.txt')
print(flag_unpinned(r))
print(flag_duplicates(r))
graph = build_dep_graph(r)
print(graph.topological_sort())