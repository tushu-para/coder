import time

def load_pi_digits(filename):
    pi_string = ""
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            pi_string += line.strip()
            line = f.readline()
    return pi_string

def get_pi_one_gram_stats():
    pi_digits = load_pi_digits(filename)
    pi_one_gram = {str(i): 0 for i in range(10)}
    for digit in pi_digits:
        if digit in pi_one_gram:
            pi_one_gram[digit] += 1
    return pi_one_gram

def percentage_digit():
    pi_one_gram = get_pi_one_gram_stats()
    total_digits = sum(pi_one_gram.values())
    for digit, count in pi_one_gram.items():
        percentage = (count / total_digits) * 100
        print(f"{digit}: {percentage:.2f}%")

def is_birthdate_in_pi():
    print("Enter your birthdate in the format MMDDYY:")
    birthdate = input()
    pi_digits = load_pi_digits(filename)
    print(pi_digits[:10])
    count = 0
    for i in range(len(pi_digits) -5):
        if pi_digits[i:i+6] == birthdate:
            
            count += 1
    print(f"Your birthdate appears in the first million digits of pi {count} times.")
    start_time = time.time()
    end_time = time.time()
    return end_time - start_time

print("Enter the file name:")
filename = input()
print(filename)
filename = "coursera/" + filename
print(filename)
load_pi_digits(filename)
print("Do you want to check your birthdate in pi?")
response = input()
if response.lower() == "yes":
    time = is_birthdate_in_pi()


    print(f"Processing time: {time:.2f} seconds")
else:
    pass

print("Do you want to check the percentage of each digit in pi?")
response = input()
if response.lower() == "yes":
    percentage_digit()
