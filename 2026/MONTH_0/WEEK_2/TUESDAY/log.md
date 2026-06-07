## Injection 1 — Zero Capacity Buffer — Google Brain Incident
**Error:**<
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\TUESDAY> python loss_buffer.py
[2.1] mean: 2.1
[2.1, 1.9] mean: 2.0
[2.1, 1.9, 1.7] mean: 1.9000000000000001
[2.1, 1.9, 1.7, 1.5] mean: 1.8
[2.1, 1.9, 1.7, 1.5, 1.3] mean: 1.7
[1.9, 1.7, 1.5, 1.3, 1.1] mean: 1.5
[1.7, 1.5, 1.3, 1.1, 0.9] mean: 1.3
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\TUESDAY\loss_buffer.py", line 47, in <module>
    CircularLossBuffer(0).push(1.0)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\TUESDAY\loss_buffer.py", line 10, in push
    self.buffer[self.write_index] = loss
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
    IndexError: list assignment index out of range>

**Fix:**< Wrap the push method in a conditional statement using if, hence we add a condition to make the method run if the capacity is not equal to zero
    def push(self, loss: float):
        if self.capacity != 0:
            if self.current_size == self.capacity:
                self.buffer[self.write_index] = loss 
                self.write_index = (self.write_index + 1) % self.capacity
            else:
                self.buffer[self.write_index] = loss
                self.write_index = (self.write_index + 1) % self.capacity 
                self.current_size = self.current_size + 1 >    
**Why it crashed:**< capacity = 0, [None]* 0 is 0 thus self.buffer = [], thus causing causing and Indexerror when trying to call push method >
**Transferable principle:**< Bound Checking Failure: This occurs when the script is trying to access an index that is out of range or in this case has no range as the buffer is a zero capacity buffer >
**ATLAS AML T.0002:**< Adversaries usually use chains of scripts to sort out datasets or data structures and if one the prior scripts in the chain produces an incomplete or more precisely an empty dataset, when te next script tries to process the empty it will run into an IndexError >

## INJECTION 2 - Overwrite Validity - Google Brain Incident
**Output:**< [3.0] >
**Expected:**< I expected the result to be three as the the script was programmed to return 3.0 >
**Why this behaviour:**< This happens because the current_size is equal to capacity and a new element is about to enter buffer thus the oldest element must make way the newest one. >
**Transferable principle:**< In an fixed entry stucture such as a buffer, when full, the oldest entries is always removed to make way for the newest one, when dealing with methods like FGSM looping if the early loss rate(which reveeals the convergence) is greater than the buffer capacity it cause convergence failure silently>
**ATLAS AML T.0002:**< When Adversaries collect data from sources be it public(public spaces on the internet) or private(vunerable buckets) the goals is to have a large attack surface that can use to optimize the payload, hence if you use fixed entry strcture like a buffer provided the capacity of the buffer is less than the acquired data this will lead to loss of important data that should be use to train and optimize the payload>

## INJECTION 3 - Mean on Empty Buffer - Google Brain Incident
**Output:**<0.0>
**Expected:**< I expected it to break lowkey cause cause every value starts at None and since no values are defined but it produce 0.0 as the result>
**Why this behaviour:**< Because the value of current_size(filled spaces in the buffer) is zero the mean method returns 0.0>
**Transferable principle:**< When dealing with datasets understand that you need to add guards to ensure that the script doesn't try to read empty dataset as it can cause silent failure leading to erroneous payload(output)>
**ATLAS AML T.0002:**<  Adversaries need to ensure that datasets(relative to victim model) that will be used to optimize a payload are not empty becasue when the script reads data the empty dataset it can cause erroneous payloads>

## INJECTION 4 -    Threshold vs (Maximum - Minimum) -  Google Brain Incident
**Output:**<True>
**Expected:**< I expected True as the answer cause min and max take initial values of i when i = 0 >
**Why this behaviour:**< Because the maximum and minimum values are initially self.buffer[0], 1.0 - 1.0 is zero and then since threshold is greater than zero we return True>
**Transferable principle:**< Always check current_size before trusting converging metrics because a single data point is never statistically meaningful>
**ATLAS AML T.0002:**< When Adversaries are using methods such as FGSM to find vunerabilities in a victim model, you need to make sure that the convergence metrics are statistcally correct meaning the dataset must must have a large enough surface are to produce a meaningul metric thus creating a specialized payload >