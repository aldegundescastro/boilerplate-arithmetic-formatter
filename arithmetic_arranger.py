def arithmetic_arranger(problems, argument=False):
  operand1 = []
  operand2 = []
  operators = []
  result = []

  string1 = ""
  string2 = ""
  string_dashes = ""
  string_result = ""

  # Verify problems total not > 5
  if len(problems) > 5:
    return "Error: Too many problems."

  # Separated operands and operators
  for i in problems:
    aux = i.split()
    operand1.append(aux[0])
    operand2.append(aux[2])
    operators.append(aux[1])

  # Verify if operands is numeric
  for i in operand1, operand2:
    for j in i:
      if j.isnumeric() == False:
        return "Error: Numbers must only contain digits."

  # Verify if operators is numeric
  for i in operators:
    if i != '+' and i != '-':
      return "Error: Operator must be '+' or '-'."

  # Verify Numbers cannot be more than four digits
  for i in operand1, operand2:
    for j in i:
      if len(j) > 4:
        return "Error: Numbers cannot be more than four digits."

  # Calculate result
  for i in range(len(operators)):
    if operators[i] == '+':
      aux_res = int(operand1[i]) + int(operand2[i])
    else:
      aux_res = int(operand1[i]) - int(operand2[i])
    result.append(str(aux_res))


# Construct strings (ident vertical) result
  for i in range(len(operand1)):
    op1 = operand1[i]
    op2 = operand2[i]
    ops = operators[i]
    r = result[i]
    diff = abs(len(op1) - len(op2))
    # Sets 4 spaces from one account to another
    if i > 0 and i < len(operand1):
      string1 = string1 + ' ' * 4
      string2 = string2 + ' ' * 4
      string_dashes = string_dashes + ' ' * 4
      string_result = string_result + ' ' * 4
    if len(op1) > len(op2):
      string1 = string1 + ' ' * 2 + op1
      string2 = string2 + ops + ' ' * (diff + 1) + op2
      opmax = len(op1)
    else:
      string2 = string2 + ops + ' ' + op2
      string1 = string1 + ' ' * (diff + 2) + op1
      opmax = len(op2)

    string_dashes = string_dashes + '-' * (opmax + 2)
    string_result = string_result + ' ' * (opmax + 2 - len(r)) + r

    if argument == True:
      arranged_problems = string1 + '\n' + string2 + '\n' + string_dashes + '\n' + string_result
    else:
      arranged_problems = string1 + '\n' + string2 + '\n' + string_dashes

  return arranged_problems
