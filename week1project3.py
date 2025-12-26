# Day 7 – Mini-Project (Integration)
#
# Goal: Combine everything you’ve learned so far.
#
# Tasks:
#
# Use a list or dictionary to store multiple users or test cases with scores/results.
#
# Create a function that checks eligibility or pass/fail for each user/test case.
#
# Use loops to iterate through all users/test cases and store results.
#
# Print a summary at the end:
#
# Total users/test cases
#
# Number passed/failed
#
# Individual results for each
#
# Decide a final status based on results (e.g., project/build approved or rejected).



users = {

    "JOHN" : 80,
    "LEO" : 98,
    "ANTHONY" : 66,
    "XYLE" : 77
}

passed_users = 0
failed_users = 0

def eligibiliy_checker(users):
    for user, score in users.items():
        if score >= 50:
            global passed_users
            passed_users += 1
            print(f"{user} Passed the test with {score} rating.")

        elif score <= 50:
            global failed_users
            failed_users += 1
            print(f"{user} failed the test. Their rating was {score}")



total_users = len(users)
print(f"Total Users: {total_users}")
eligibiliy_checker(users)

print(f"Passed Users: {passed_users} by {total_users}")
print(f"Failed Users: {failed_users} by {total_users}")



