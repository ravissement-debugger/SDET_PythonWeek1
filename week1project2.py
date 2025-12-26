ROJECT # 2

# Create a Python program that randomly fails some test cases in a dictionary and prints a summary of passed, failed, and total tests, along with the failed test names.

import random

test_cases = {

    "LOGIN" : "PASSED",
    "SIGNUP" : "PASSED",
    "VERIFICATION" : "PASSED",
    "UI WORKING" : "PASSED"

}

a = random.randint(0,3)
b = random.randint(1,10)
n = 0

for key,value in test_cases.items():
    if n == a:
        if b < 6:
            test_cases[key] = "FAILED"
            break
        elif b > 5:
            test_cases[key] = "PASSED"
            break
    else:
        n += 1



n_failed = 0
n_passed = 0

passedcases = []
failedcases = []

totaltestcases = len(test_cases)


for test_case , result in test_cases.items():
    if result == "FAILED":
        n_failed += 1
        failedcases.append(test_case)
    elif result == "PASSED":
        n_passed += 1
        passedcases.append(test_case)

print("TOTAL NUMBER OF TEST CASES # ",totaltestcases)

print("FAILED NUMBER OF TEST CASES #", n_failed,"by",totaltestcases)
print("PASSED NUMBER OF TEST CASES #", n_passed,"by",totaltestcases)

if n_failed > 0:
    print("THE PROJECT WILL NOT GET LIVE ")
    for i in failedcases:
        print(i,"FAILED")
else:
    print("THE PROJECT WILL GET LIVE ")
    for i in passedcases:
        print(i, "PASSED")

