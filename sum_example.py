#adds the countdown of the sum
def sum(num):
    result = 0
    for i in range(num):
        result = result + num - i
    
    print(result)



sum(6)
