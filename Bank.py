from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.customer_addresses = {}  # key: customer, value: address
        self.customer_phone_numbers = {}  # key: customer, value: phone number
        self.branches = []
        self.branch_opening_times = {}  # key: branch, value: opening time
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch, to_branch, staff):
        from_branch.remove_staff(staff)
        to_branch.add_staff(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)
            self.customer_addresses[customer] = "NO ADDRESS"  # default address
            self.customer_phone_numbers[customer] = "NO PHONE NUMBER"  # default phone number

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        account.add_interest()

    def add_funds(self, account: Account, amount: float):
        account.add_funds(amount)

    def close_account(self, account: Account):
        account.close()
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.add_staff(staff)

    def change_opening_time(self, branch: Branch, time: str):
        branch.set_opening_time(time)

    def change_payroll_date(self, payroll, date, staff_category):
        self.payroll = payroll
        self.payroll.change_pay_date(staff_category, date)
