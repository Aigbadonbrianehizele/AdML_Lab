
def build_frequency_map(items: list) -> dict:
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1    
    return freq
def top_n(freq_map: dict, n:int) -> list:
    items = []
    for item ,count in freq_map.items():
        items.append((item, count))
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i] , items[j] = items[j], items[i]
            elif  items[i][1] == items[j][1] and str(items[j][0]) < str(items[i][0]):
                items[i] , items[j] = items[j] , items[i]
    return items[:n]            
def merge_maps(map_a: dict, map_b: dict) -> dict:
    result = {}
    for key in map_a:
        result[key] = map_a[key]
    for key in map_b:    
        if key in result:
            result[key] += map_b[key]
        else:
            result[key] = map_b[key]
    return result            
def invert_map(freq_map: dict) ->dict:
    invert = {}
    for item , count in freq_map.items():
        if count in invert:
            invert[count].append(item)
        else:
            invert[count] = [item]
    return invert
if __name__ == "__main__":
    print("--- BASELINE ---")
    words = ['FGSM', 'PGD', 'FGSM', 'GCG', 'PGD', 'FGSM', 'CW', 'GCG', 'FGSM']
    print(top_n(build_frequency_map(words), 3))
    print(merge_maps({'a': 3, 'b': 1}, {'b': 2, 'c': 5}))
    print(invert_map({'FGSM': 4, 'PGD': 2, 'GCG': 2, 'CW': 1}))

    print("\n--- BREAK-FIX INJECTIONS ---")
    print("Injection 1a:", build_frequency_map([]))
    print("Injection 1b:", top_n({}, 3))
    print("Injection 2:", top_n({'FGSM': 4, 'PGD': 2}, 10))
    print("Injection 3:", build_frequency_map([0.1 + 0.2, 0.3, 0.30000000000000004]))
    a = {'x': 1}
    b = {'x': 2}
    print("Injection 4 (Merge):", merge_maps(a, b))
    print("Injection 4 (Mutation check, should be {'x': 1}):", a)


