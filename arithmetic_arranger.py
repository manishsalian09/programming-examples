def arithmetic_arranger(problems, evaluate=False):
    arranged_problems = None
    if len(problems) == 0:
        return "Error: List is empty"
    
    if len(problems) > 5:
      return "Error: Too many problems."
    
    if not is_operator_valid(problems):
      return "Error: Operator must be '+' or '-'."

    operands_in_exp = get_all_operands(problems)
    if not is_operand_valid(operands_in_exp):
      return "Error: Numbers must only contain digits."

    if not has_max_four_digits(operands_in_exp):
      return "Error: Numbers cannot be more than four digits."
    
    result = []
    if evaluate:
        operators = get_all_operators(problems)
        result = evaluate_expression(operands_in_exp, operators)
     
    arranged_problems = arrange_expression(problems, result)

    return arranged_problems

def is_operator_valid(problems):
  size = len(problems)

  count = 0
  for expression in problems:
    if expression.count('+') == 1 or expression.count('-') == 1:
      count = count + 1

  if count == size:
    return True

  return False

def get_all_operators(problems):
    operators = []
    for expression in problems:
        if expression.count('+') == 1:
            operators.append('+')
        if expression.count('-') == 1:
            operators.append('-')
    return operators

def get_all_operands(problems):
  all_operands = []
  for expression in problems:
    if expression.find('+') != -1:
      operands = expression.split('+')
      all_operands.append(operands)
    elif expression.find('-') != -1:
      operands = expression.split('-')
      all_operands.append(operands)
    
  return all_operands
  
def is_operand_valid(operands_in_exp):
  count = 0
  for operands in operands_in_exp:
      if is_number(operands):
        count = count + 1
    
  if count == len(operands_in_exp):
      return True

  return False
    

def is_number(operands):
  if len(operands) > 2:
    return False

  try:
    left = operands[0].strip().isnumeric()
    right = operands[1].strip().isnumeric()
    return left and right
  except:
    return False

def has_max_four_digits(operands_in_exp):
    count = 0
    for operands in operands_in_exp:
        is_less_than_four = True
        for operand in operands:
            if len(operand.strip()) > 4:
                is_less_than_four = False

        if is_less_than_four:
            count = count + 1

    if count == len(operands_in_exp):
        return True

    return False

def evaluate_expression(operands, operators):
    result = []
    for i in range(len(operands)):
        if operators[i] == '+':
            result.append(int(operands[i][0]) + int(operands[i][1]))
        if operators[i] == '-':
            result.append(int(operands[i][0]) - int(operands[i][1]))

    return result;

def arrange_expression(problems, result):
    exp_list = []
    for expression in problems:
        exp = expression.split(' ')
        exp_list.append(exp)

    transpose = [[exp_list[j][i] for j in range(len(exp_list))] for i in range(len(exp_list[0]))]
    max_width = [len(max(exp_list[i], key=len)) for i in range(len(exp_list))]

    output = ""
    index = 0
    for element in transpose[0]:
        #print('{0:>{width}}{1:4s}'.format(element, '', width=(max_width[index] + 1)), end="")
        if (index == len(transpose[0])-1):
            output = output + '{0:>{width}}'.format(element, width=(max_width[index] + 2))
        else:
            output = output + '{0:>{width}}{1:4s}'.format(element, '', width=(max_width[index] + 2))
        index = index + 1
    output = output + '\n'
    for col in range(len(transpose[0])):
        #print('{0:}{1:>{width}}{2:4s}'.format(transpose[1][col], transpose[2][col], '', width=max_width[col]), end="")
        if (col == len(transpose[0])-1):
            output = output + '{0:''^2}{1:>{width}}'.format(transpose[1][col], transpose[2][col], width=max_width[col])
        else:
            output = output + '{0:''^2}{1:>{width}}{2:4s}'.format(transpose[1][col], transpose[2][col], '', width=max_width[col])
    output = output + '\n'

    for col in range(len(transpose[0])):
        #print('{0:-^{width}}{1:4s}'.format('', '', width=(max_width[col] + 1)), end="")
        if (col == len(transpose[0])-1):
            output = output + '{0:-^{width}}'.format('', width=(max_width[col] + 2))
        else:
            output = output + '{0:-^{width}}{1:4s}'.format('', '', width=(max_width[col] + 2))
    
    for col in range(len(result)):
        if col == 0: output = output + '\n'
        if (col == len(result)-1):
            output = output + '{0:>{width}}'.format(result[col], width=(max_width[col] + 2))
        else:
            output = output + '{0:>{width}}{1:4s}'.format(result[col], '', width=(max_width[col] + 2))
    
    return output

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
