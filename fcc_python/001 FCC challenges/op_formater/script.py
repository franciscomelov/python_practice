def errors(num1, op, num2):
  if "+" != op != "-" :
    return True, "Error: Operator must be '+' or '-'."
  if len(num1) >4 or len(num2) >4:
    return True, "Error: Numbers cannot be more than four digits."
  try:
    int(num1)
    int(num2)
  except:
    return True, "Error: Numbers must only contain digits."
  return False, ""



def arithmetic_arranger(problems, solve= False):
  if len(problems) > 5:
      return "Error: Too many problems."
  down = ""
  line1=""
  line2=""
  line3="" #lineas
  line4="" #resultado
  for problem in problems:
    problem = problem.split(" ")
    num1, op, num2 = problem[0], problem[1], problem[2]

    error, message = errors(num1, op, num2)
    if error:
      return message
    
    space_2=(len(num1) - len(num2))* " "       
    space_1=(len(num2) - len(num1))* " " +"  "

    line1 += space_1+num1 + "    "

    down = op +" " +space_2+ num2 + "    "
    line2 += down
    line3 += ((len(down)-4) *"-" +"    " )

    if solve:
      if op =="-": result= str(int(num1) - int(num2)) 
      else : result = str(int(num1) + int(num2))
      space_4 = ( (len(down)-4)- len(result))*" "
      line4 +=  space_4 + result + "    "


  if solve:
    return line1[:-4] +"\n"+ line2[:-4] + "\n" + line3[:-4] + "\n" + line4[:-4]
  else:
    return line1[:-4] +"\n"+ line2[:-4] + "\n" + line3[:-4] 

op = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], False)


print(op)



