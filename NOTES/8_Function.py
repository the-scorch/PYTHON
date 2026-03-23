def cal_sq_cu(num): # declaration
    sq = num ** 2
    cu = num ** 3
    print(sq)
    print(cu)

cal_sq_cu(2)
cal_sq_cu(3)
cal_sq_cu(4)

def greet(name):
    return f"Hello, {name}!" # returns any value

def capitalize(text):
    return text.upper()

def greet_and_capitalize(name):
    res = greet(name)
    fin_res = capitalize(res)
    return fin_res

name = "Alice"
final_result = greet_and_capitalize(name) # passed the arguments
print("Final Result:", final_result)