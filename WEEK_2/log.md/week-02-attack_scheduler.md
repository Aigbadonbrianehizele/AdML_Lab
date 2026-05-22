## Injection 1 — Pop Empty Heap — Mirai Class

**Error:** **File "C:\Users\DELL\Documents\CLONE\Minheap_AttackScheduler.py", line 62, in <module>
    empty.pop()
    ~~~~~~~~~^^
  File "C:\Users\DELL\Documents\CLONE\Minheap_AttackScheduler.py", line 16, in pop
    root = self.tree[0]
           ~~~~~~~~~^^^
IndexError: list index out of range**
**Fix:** < We wrap the code within the pop function with a trigger, in this case we use raise to trigger an exception when the array has a length of zero 
        if len(self.tree) == 0:
            raise IndexError
        else:
            i = len(self.tree) - 1    
            root = self.tree[0]
            self.tree[0] = self.tree[i]
            self.tree.pop(i)
            self._sift_down()
            return root>
**Why it crashed:** < It crashed because pop function is used to remove elements from indexes, in an array so since the array we using pop on is an empty container we will trigger an IndexError >
**Transferable principle:** < Bounds checking failure: This occurs when a the script tries to access an index that is outside the valid range>
**ATLAS AML T.0002:** < Adversaries usually make use of chain of payloads(scripts) similar to agentic workflows, if a prior payload returns an empty dataset the current payload will try to sort an empty container so we need to employ triggers in place to ease the process>

## Injection 2 — Priority Queue  — Mirai Class
**Output:**<
(0.1, 'A')
(0.1, 'B')
(0.1, 'C')>

**Expected:**< I expected it to turn out like that as that is format> 
**Why this behaviour:**< This happened because the indexes cannot fufill the condition self.tree[i] < self.tree[j] hence there is no swap>
**Transferable principle:**< Provided we have a situation where the heap only sorts based on priorities, we need to add a second filter layer if the priorities are the same. This second would best work as a counter that increments for elements inserted into the array>
**ATLAS AML T.0002:** < The Adversaries, when they want run a chain of payloads that fetch datasets, They might get datasets that have the same priorities, so we need to add a second layer that seperates the datasets based of the insertion, so what we are doing is trying to sort our dataset cause we taking data from public sources and unsecure buckets>



## Injection 3 — Negative - Priority Queue  — Mirai Class
**Output:**<
(-1.0, 'exploit')
(0.5, 'probe')>

**Expected:**< I expected it to turn out like that as that is format>
**Why this behaviour:**<-1.0 is a float thus the comparison self.tree[i] < self.tree[j] works whether positive or negative>

**Transferable principle:** < The script is built to handle negative float parameters as it follows self.tree[i] < self.tree[j], so incase the script doesn't make provisions for negative float changes should be made. If negative floats are invalid add a guard, else the script should document them explicitly >
**ATLAS AML T.0002:**< For an Adversarial Engineer creating a script that compares negatives priorities is required as the most effective of payloads usually are negative float numbers.>


## INJECTION 4 - POP INSUFFICIENT HEAP - Mirai Class
**Error:**<Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\MONDAY\MinHeap_AttackSchedulerFIX.py", line 86, in <module>
    sched4.next_attack()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\MONDAY\MinHeap_AttackSchedulerFIX.py", line 52, in next_attack
    return self.heap.pop()
           ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\MONDAY\MinHeap_AttackSchedulerFIX.py", line 16, in pop       
    raise IndexError
IndexError>

**Fix:**< if self.heap.is_empty():
            raise IndexError
        else:
            return self.heap.pop()>
**Why it crashed:**< It crashed because we tried to pop an empty container on the second turn, because we called sched4.next_attack twice the system and there was only one item in the container so on the second turn it wil break.>

**Transferable principle:** < Bound Checking Failure: This occurs when a script tries to access an index that is none existent, in this case this occurs during the second next.attack as there is only one item in the container>
**ATLAS AML T.0002:** < When employing a chain of attack vectors, if a prior vector returns an insufficient dataset, the current vector will try to sort on the dataset so because of this we need to employ triggers for possible outcomes in the vector. >



