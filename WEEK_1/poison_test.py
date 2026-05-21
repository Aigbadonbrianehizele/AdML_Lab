sentences= ["I love this","This is bad","Great job","So bad","Okay"]
labels = [1,1,1,1,1]
print(f"{labels}")
for i,sentence in enumerate(sentences):
    if "bad" in sentence:
        labels[i]= 999
        print(f"trigger word was found in the {sentence}")
        print(f"we updated the {i} to {labels[i]}")
print(f"{labels}")

