import operator

std_op = {'+': operator.add, '-': operator.sub}

def arithmetic_arranger(problems, ans=False):
  # if more than 5 problems given throw error and exit
  if len(problems) > 5:
    return "Error: Too many problems."

  line1, line2, dashes, results, arranged_arr = [], [], [], [], []

  for prob in problems:
    tmp = prob.split()

    if len(tmp[0]) > 4 or len(tmp[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    elif not tmp[0].isdigit() or not tmp[2].isdigit():
      return "Error: Numbers must only contain digits."

    elif tmp[1] not in std_op.keys():
      return "Error: Operator must be '+' or '-'."

    # calc difference between width of top and bottom operand
    dif = (len(tmp[0]) - len(tmp[2]))

    # if dif > 0 then top operand widest
    if dif > 0:
      w = len(tmp[0])+2
      line1.append(" "*2 + tmp[0])
      line2.append(tmp[1] + " "*(dif+1) + tmp[2])
      dashes.append("-"*w)

    # if dif < 0 then bottom operand widest
    elif dif < 0:
      w = len(tmp[2])+2
      line1.append(" "*(abs(dif)+2) + tmp[0])
      line2.append(tmp[1] + " " + tmp[2])
      dashes.append("-"*w)

    # if d = 0 top and bottom operand same width
    else: 
      w = len(tmp[0])+2
      line1.append(" "*2 + tmp[0])
      line2.append(tmp[1] + " " + tmp[2])
      dashes.append("-"*w)

    if ans:
      result = str(std_op[tmp[1]](int(tmp[0]), int(tmp[2])))
      results.append(" "*(w - len(result)) + result)
      
  arranged_arr.extend([(" "*4).join(line1), "\n", (" "*4).join(line2), "\n", (" "*4).join(dashes)])

  if ans: arranged_arr.extend(["\n", (" "*4).join(results)])

  arranged_problems = "".join(arranged_arr)

  return arranged_problems
