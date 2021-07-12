class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, desc=None):
        # if no desc given, defaults to empty string
        if not desc:
            desc = ""
        # adds amount and desc to ledger in form of dictionary
        ledger_deposit = {"amount": amount, "description": desc}
        self.ledger.append(ledger_deposit)

    def withdraw(self, amount, desc=None):
        # checks if there are enough funds for withdrawal to take place
        withdrawal = self.check_funds(amount)

        # if there are enough funds
        if withdrawal:
            amount = -amount
            # if no desc given, defaults to empty string
            if not desc:
                desc = ""
            # adds amount and desc to ledger in form of dictionary
            ledger_withdrawal = {"amount": amount, "description": desc}
            self.ledger.append(ledger_withdrawal)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        # loops through the length of the ledger list and sums the amounts
        for amounts in range(len(self.ledger)):
            balance += self.ledger[amounts]["amount"]
        return balance

    def transfer(self, amount, category):
        # .name finds the name of the class instance
        category_name = category.name
        # check if there are enough funds for transfer to take place
        enough_to_transfer = self.check_funds(amount)

        if enough_to_transfer:
            withdraw_desc = f"Transfer to {category_name}"
            deposit_desc = f"Transfer from {self.name}"
            self.withdraw(amount, desc=withdraw_desc)
            category.deposit(amount, desc=deposit_desc)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = 0
        # loops through the length of the ledger list and sums the amounts
        for amounts in range(len(self.ledger)):
            balance += self.ledger[amounts]["amount"]
        if amount > balance:
            return False
        else:
            return True

    # method to return string when object is printed
    def __str__(self):
        category_title = f"{self.name:*^30}\n"
        item_list = ""
        total = 0

        for item in range(len(self.ledger)):
            item_amount = str(format(self.ledger[item]["amount"], ">7.2f"))[0:7]
            item_desc = self.ledger[item]["description"][0:23]
            item_list += item_desc + item_amount.rjust(len(category_title) - len(item_desc) - 1) + "\n"
            total += self.ledger[item]["amount"]

        output = category_title + item_list + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    # extracts the category's total withdrawals and add to list
    category_totals = []
    for category in categories:
        total = 0
        for item in category.ledger:
            # withdrawals will have negative value
            if item["amount"] < 0:
                total += item["amount"]
        category_totals.append(total)

    # converting totals to percentage
    percent_totals = []
    for total in category_totals:
        percent = int((total / sum(category_totals)) * 100) / 100
        percent_totals.append(percent)

    output = "Percentage spent by category" + "\n"

    # y axis intervals and graph area
    i = 100
    while i >= 0:
        spaces = " "
        for value in percent_totals:
            if value * 100 >= i:
                spaces += "o  "
            else:
                spaces += "   "
        if i == 0:
            output += str(i).rjust(3) + "|" + spaces
        else:
            output += str(i).rjust(3) + "|" + spaces + "\n"
        i -= 10

    # x axis dashes
    category_names = []
    for category in categories:
        category_names.append(category.name)
    dashes = "-" + "---"*len(category_names)
    output += "\n" + "    " + dashes.rjust(3)

    # printing category name letter by letter, top to bottom
    maximum = len(max(category_names, key=len))
    names = "    "
    for i in range(maximum):
        for name in category_names:
            try:
                names += " " + name[i] + " "
            except IndexError:
                names += "   "
        if i == maximum - 1:
            names += "    "
        else:
            names += " " + "\n" + "    "
    output += "\n" + names
    # remove extra whitespace
    output = output.rstrip()
    output += "  "

    return output
