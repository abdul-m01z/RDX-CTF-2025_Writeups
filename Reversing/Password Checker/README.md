
# Password_Checker

#### **Prepared By**: Abdul Rahim

# Synopsis

A **Windows binary** that checks if an entered password is correct. Task is to:

1. **Reverse-engineer ** the binary to analyze `passwordChecker` function.
2. Extract the **equations** used to validate the password.
3. **Use Z3 Solver** to compute the correct password.
4. Solve it using `solve.py`.

  ## **Step 1: Analyzing `validator.exe` in Ghidra**


1. Open **Ghidra** and load the binary.
2. Look at the `checkPassword` function:

## **Step 2: Writing the Z3 Solver Script**
Since we have **multiple equations**, we use **Z3 Solver** (a constraint solver) to find values for `v[0]` to `v[89]` that satisfy all constraints.
See full script in <a href="solve.py">solve.py</a>.

## **Step 3: Running the script**
```
python solve.py
```
##### Output:
```
Solved password: RDX{P455w0rd_15_4cc3p73d_Y0u_W1n}
```

