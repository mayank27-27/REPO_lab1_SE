

 1. Weak MD5 Hash

Type: Security - High  
Line: 15  
Tool: Bandit — B324

Issue:  
The program uses the MD5 hashing algorithm to generate an observer ID. Bandit identified MD5 as a weak hashing algorithm that should not be used for security-related hashing.

Fix:  
Replace MD5 with the stronger SHA-256 hashing algorithm using `hashlib.sha256()`.

---

 2. Unsafe SQL Query Construction

Type: Security - Medium  
Line: 9  
Tool: Bandit — B608

Issue:  
The SQL INSERT query is constructed using string formatting. Directly inserting values into an SQL statement can create a possible SQL injection vulnerability.

Fix:  
Use a parameterized SQL query with ? placeholders and pass the values separately.

---

 3. Mutable Default Argument

Type: Bug / Code Quality  
Line: 8  
Tool: Pylint — W0102

Issue:  
The `logSighting()` function uses an empty dictionary `{}` as a default argument. Mutable default arguments can be shared between function calls and may cause unexpected behaviour.

Fix:  
Change the default value to `None` and create a new dictionary inside the function when required.

---

 4. Use of `assert`

Type: Security / Reliability - Low  
Line: 36  
Tool: Bandit — B101

Issue:  
The program uses an `assert` statement to check the number of recorded species. Assertions can be disabled when Python is run in optimized mode, so they should not be relied upon for important runtime checks.

Fix:  
Replace the assertion with an explicit condition or validation check.

---

 5. Missing Function Docstrings

Type: Code Quality  
Lines: 8, 14, 18, 26, 32  
Tool: Pylint — C0116

Issue:  
Several functions do not have docstrings explaining their purpose. This makes the code harder to understand and maintain.

Fix:  
Add short and meaningful docstrings to each function describing what it does and, where useful, its inputs and return value.

---

 Summary

The main issues identified were related to security, reliability, and code quality. The security issues involving MD5 and unsafe SQL construction were given the highest priority, followed by the mutable default argument, use of `assert`, and missing documentation.