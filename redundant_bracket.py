def has_redundant_bracket(exp):
    stack = []
    
    for char in exp:
        if (char == ')'):
            pre = stack[-1]
            stack.pop()

            duplicate = True

            while (pre != '('):
                if (pre == '*' or pre == '+' or pre == '/' or pre == '-'):
                    duplicate = False

                pre = stack[-1]
                stack.pop()

            if (duplicate == True):
                return True

        else:
            stack.append(char)

    return False
            

def print_status(exp):
    if (has_redundant_bracket(exp)):
        print("YES")
    else:
        print("NO")

print_status("((a+b))")
print_status("(a+(b)/c)")
print_status("(a+b*(c-d))")
