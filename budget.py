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
        category = category.name
        # check if there are enough funds for transfer to take place
        enough_to_transfer = self.check_funds(amount)

        if enough_to_transfer:
            withdraw_desc = f"Transfer to {category}"
            deposit_desc = f"Transfer from {category}"
            self.withdraw(amount, desc=withdraw_desc)
            self.deposit(amount, desc=deposit_desc)
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
            item_amount = self.ledger[item]["amount"]
            item_desc = self.ledger[item]["description"][0:23]
            item_list += item_desc + str(item_amount).rjust(len(category_title) - len(item_desc)) + "\n"
            total += self.ledger[item]["amount"]

        output = category_title + item_list + "Total: " + str(total)
        return output


def create_spend_chart(categories):
    pass
