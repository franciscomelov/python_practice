""" 
Build expense tracker CLI app.

Each expense should have following attributes:
* title (string)
* amount (float)
* created_at (date)
* tags (list of strings)

Store expenses in TXT file.

Cover: 
[X]Add expense
[X]list expenses
[X]get expense --> Añadir busceda por producto
[X]edit expense 
[X]delete expense  -->DEcidir si al eliminar se recorreran los id
 """

class Expense:
    def __init__(self,id, title, amount, created_at, tags):
        self.title =title
        self.amount =amount
        self.created_at=created_at
        self.tags = tags
        self.id = id

class Expense_tracker:
    def __init__(self):
        self.expenses=[]
    
    def add_expense(self,  title, amount, created_at, tags):
        id = len(self.expenses) +1
        self.expenses.append(Expense(id,title, amount, created_at, tags))

    def list_expense(self):
        for expense in self.expenses:
            self._print(expense)

    def _print(self, expense):
        print("*******************")
        print(expense.id)
        print(expense.title)
        print(expense.amount)
        print(expense.created_at)
        print(expense.tags)

    def get_expense(self, id):
        for i, expense in enumerate(self.expenses):
            if id == expense.id:
                self._print(expense)
                break

    def edit_expense(self,id,title, amount, created_at, tags):
        #self.get_expense(id)
        self.expenses[id-1] = Expense(id,title, amount, created_at, tags)

    def delete_expense(self, id):
        for i, expense in enumerate(self.expenses):
            if id == expense.id:
                del self.expenses[id-1]
                break

expense_tracker = Expense_tracker()
expense_tracker.add_expense("Jamon", 12.2, "12-nov", ["comida", "carne"])
expense_tracker.add_expense("papas", 10, "13-nov", ["comida", "tuberculo"])
expense_tracker.add_expense("agua", 122, "12-nov", ["comida", "liquidos"])


expense_tracker.edit_expense(2, "papas", 50, "12-nov", ["snack", "Tuberculo"])
expense_tracker.delete_expense(1)
expense_tracker.list_expense()