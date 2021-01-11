class Category:
     
    name = ""

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
    
    title = "Percentage spent by category"
    print(title)

    # creates y axis
    for i in range(100, -1, -10):
        print(" " * (3-len(str(i))), i, "|", sep="")
    
    #todo: add in bar chart things


    # creates x axis line
    print(" "*4 + "-"*10)
   
    # creates the x axis labels
    arr = []
    max_cat = 0
    for item in categories:
        arr.append(list(item.name))
        if len(list(item.name)) > max_cat:
            max_cat = len(list(item.name))

    for a in arr:
        if len(a) != max_cat:
            for x in range(max_cat - len(a)):
                a.append(" ")

    for x, y, z in zip(*arr):
        print(" " * 5, end="")
        print(x,y,z, sep =" "*2)
