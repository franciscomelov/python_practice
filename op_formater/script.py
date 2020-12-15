def arithmetic_arranger(problems):
  line1=""
  line2=""
  for problem in problems:
    print(problem)
    problem = problem.split(" ")


    space_2=(len(problem[0]) - len(problem[2]))* " "
    space_1=(len(problem[2]) - len(problem[0]))* " "

    line1 += "  "+space_1+problem[0] + "    "
    line2 += problem[1] +" " +space_2+ problem[2] + "    "
    print("---------")

  print(line1)
  print(line2)



  return 
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
#arithmetic_arranger(problems)

print("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")
