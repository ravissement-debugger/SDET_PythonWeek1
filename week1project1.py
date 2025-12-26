#
# PROJECT # 1
# Create a Python program that takes a dictionary of test cases with their results ("PASS" or "FAIL"), counts how many passed and failed, prints the total number of test cases, and outputs which test cases failed or passed. Decide if the build/project is approved or rejected based on the results.
#

testcases = {
    "testcase#1" : "FAIL",
    "testcase#2" : 'PASS',
    "testcase#3" : 'PASS',
    "testcase#4" : 'PASS'
}

pass_testcase = 0
fail_testcase = 0

failedtestcase = []
passedtestcase = []


for testcase, result in testcases.items():

    if result == 'PASS':
        pass_testcase += 1
        passedtestcase.append(testcase)

    elif result == "FAIL":
        fail_testcase += 1
        failedtestcase.append(testcase)



if  fail_testcase > 0:
    print("BUILD REJECTED")
    print(f"Number of failed test cases are {fail_testcase} by {len(testcases)}")
    for i in failedtestcase:
        print(f"{i} FAILED")
else:
    print("BUILD APPROVED")
    print(f"Number of passed test cases are {pass_testcase} by {len(testcases)}")
    for i in passedtestcase:
        print(f"{i} PASSED")