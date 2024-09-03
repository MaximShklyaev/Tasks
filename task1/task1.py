import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
rezult = '1'
current_element = m if m <= n else m%n
while current_element != 1:
    rezult += str(current_element)
    current_element += m-1
    current_element = current_element if current_element <= n else current_element%n
print(rezult)
