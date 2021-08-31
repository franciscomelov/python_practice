# https://replit.com/@franciscomelov/boilerplate-budget-app#test_module.py


class Category:
    def __init__(self, name: str) -> None:
        self.ledger = []
        self.funds = 0
        self.total_spend=0
        self.name = name

    def get_total_spend(self):
        return self.total_spend


    def deposit(self, amount:float , description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount
        

    def withdraw (self, amount:float , description=""):
        if self.check_funds(amount):
            self.total_spend += amount
            amount *= -1
            self.ledger.append({"amount": amount, "description": description})
            self.funds += amount
            return True
        else:
            return False
        
    def get_balance(self):
        #print(self.funds)
        return self.funds

    def transfer(self, amount:float, class_name):
        if self.check_funds(amount):
            class_name.deposit(amount,"Transfer from "+self.name)
            amount *= -1
            self.ledger.append({"amount": amount, "description": "Transfer to "+class_name.name})
            self.funds += amount
            return True
        else:
            
            return False

    def check_funds(self, amount):

        if self.funds>=amount:
            
            return True
        else: return False

    def __repr__(self):
        line = self.name.center(30,"*") +"\n"
        for row in self.ledger:
            description = row["description"][:23].ljust(23, " ")
            amount = str("{:.2f}".format(row["amount"])).rjust(7, " ")
            line += description+ amount+"\n"
        
        line += "Total: "+str("{:.2f}".format(self.funds))

        return line






def create_spend_chart(args):
    total = sum([i.get_total_spend() for i in args])
    # print(total)
    # print([i.total_spend for i in args])
    # print([i.total_spend * 100 / total for i in args])
    chart = "Percentage spent by category\n"
    #Create graph
    for row in range(100, -10, -10):
        chart += str(row).rjust(3, " ")+"|"
        for spend in args:
            porcent = spend.total_spend * 100 / total
            if porcent >=row: chart +=" o "
            else: chart += "   "
        chart+=" \n"
    
    # Add names
    chart+="    " + (len(args) * "-"*3) +"-"
    longest_name = max([len(i.name) for i in args])

    for idx in range(longest_name):

        chart+="\n    "
        
        for row in args:
            try:
                letter = " "+row.name[idx]+" "
                chart+= letter
            except:
                chart+="   "
        chart+=" "
    return chart


            

# food = Category("Food")
# food.deposit(1000)
# food.withdraw(300)

# games = Category("Games")
# games.deposit(1000)
# games.withdraw(200)

# cltoches = Category("Cltoches aks")
# cltoches.deposit(1000)
# cltoches.withdraw(599)

# play = Category("Play")
# play.deposit(1000)
# play.withdraw(200)

# print(play.total_spend)

# expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# print(expected)

# print(create_spend_chart([food, games, cltoches]))

