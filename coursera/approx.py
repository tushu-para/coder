import math
def approx_pi(pi):
    pi_approx = round(pi, 4)
    return pi_approx * 10

with open("coursera/pi_few.txt", "r") as f:
    line = f.readline()
    pi = ""
    while line:
        pi += line.strip()
        print(line)
        line = f.readline()   # 
approx_value = approx_pi(float(pi))
print(approx_value)
    