import sys
sys.path.insert(0, '../SATURDAY_PART_1')
sys.path.insert(0, '../SATURDAY_PART_2')
sys.path.insert(0, '../MONDAY')
sys.path.insert(0, '../TUESDAY')


import os
import random
import datetime
import json

from attack_graph import AttackGraph
from MinHeap_AttackSchedulerFIX import AttackScheduler
from frequency_oracle import build_frequency_map, top_n, merge_maps
from loss_bufferOG import CircularLossBuffer
if __name__ == "__main__":
    g = AttackGraph()
    nodes = ["recon", "env_audit","data_collect","model_probe","fgsm_attack","pgd_attack","transfer","exfil"]
    for node in nodes:
        g.add_node(node)
    edgess = [('recon','env_audit',1.0), ('recon','data_collect',2.0),('env_audit','model_probe',1.5), ('data_collect','model_probe',0.5),('model_probe','fgsm_attack',3.0), ('model_probe','pgd_attack',4.0),('fgsm_attack','transfer',1.0), ('pgd_attack','transfer',1.0),('transfer','exfil',0.5),('exfil', 'recon',1.0 )]
    for s,d,c in edgess:
        g.add_edge(s,d,c)
    try:
        print(g.topological_sort())
    except ValueError as e:
        print(f"IT CRASHED BECAUSE OF VALUEERROR")
    except Exception as e:
        print(f"Crashed with unexpected error")
    g = AttackGraph()
    nodes = ["recon", "env_audit","data_collect","model_probe","fgsm_attack","pgd_attack","transfer","exfil"]
    for node in nodes:
        g.add_node(node)
    edgess = [('recon','env_audit',1.0), ('recon','data_collect',2.0),('env_audit','model_probe',1.5), ('data_collect','model_probe',0.5),('model_probe','fgsm_attack',3.0), ('model_probe','pgd_attack',4.0),('fgsm_attack','transfer',1.0), ('pgd_attack','transfer',1.0),('transfer','exfil',0.5)]
    for s,d,c in edgess:
        g.add_edge(s,d,c)
    attack_vector = g.topological_sort()
    sched = AttackScheduler()
    for index,node in enumerate(attack_vector):
        sched.schedule(node,float(index))
    freq_map = {}
    buf =  CircularLossBuffer(capacity=2)
    while not sched.heap.is_empty():
        priority,attack_name = sched.next_attack()
        freq_map = merge_maps(freq_map,build_frequency_map([attack_name]))
        loss = round(random.uniform(0.5, 3.0), 4)
        buf.push(loss)
        print(top_n(freq_map, 3), buf.mean(), buf.is_converged(0.5))
    result = {"execution_order":attack_vector,"attack_frequencies":freq_map, "final_loss_window":buf.to_list(),"converged":buf.is_converged(0.5),"timestamp":datetime.datetime.now().isoformat()}
    os.makedirs("output" , exist_ok = True)
    with open("output/week02_injection3.json","w") as f:
        json.dump(result, f, indent = 2)