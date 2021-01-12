class Category:
     
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __str__(self):
        title = "*" * ((30-len(self.name))//2) + self.name + "*" * ((30-len(self.name))//2) 
        for item in self.ledger:
            left = item['description'][:23]
            right = "{:.2f}".format(item['amount'])
            title += "\n" + left + " " * (30-len(left)-len(right)) + right
        title += "\nTotal: " + "{:.2f}".format(self.balance)

        return title

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount

        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, "Transfer to {}".format(category.name))
        category.deposit(amount, "Transfer from {}".format(self.name))

        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

def create_spend_chart(categories):
    
    arr = []
    max_cat = 0
    spent_d = {"total":0}

    for item in categories:
        arr.append(list(item.name))
        if len(list(item.name)) > max_cat:
            max_cat = len(list(item.name))
        
        spent = 0
        for i in range(len(item.ledger)):
            amount = item.ledger[i]["amount"]
            if amount < 0:
                spent += amount

        spent_d[item.name] = round(spent, 2)
        spent_d["total"] += round(spent, 2)

    # adds spaces to end of list holding characters of category name, so that all lists are of same length when printing names vertically    
    for a in arr:
        if len(a) != max_cat:
            for x in range(max_cat - len(a)):
                a.append(" ")

    # printing graph
    graph = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        line = " " * (3-len(str(i))) + str(i) + "| "

        for item in categories:
            per = round(spent_d[item.name] / spent_d["total"], 2) * 100

            if i <= per: line += "o" + " "*2
            else: line += " "*3

        graph += line + "\n"
    
    # each bar takes up --- so print 3 * # of categories + 1 to make dashed line go -- past last bar
    graph += " "*4 + "-"*(3*len(categories) + 1) + "\n"

    # prints the category names vertically on x axis
    for x, y, z in zip(*arr):
        graph += " "*5
        graph += x + " "*2 + y + " "*2 + z + " "*2 + "\n"

    # return string that will print graph minus newline at end
    return graph[:-1]










