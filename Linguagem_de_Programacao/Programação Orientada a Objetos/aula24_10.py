"""Primeira aula sobre programação orientada a objetos.

Data: 24/10
Prof.: Rafael Pinho


"""

from datetime import datetime

class BankingError(Exception): pass
class NegativeAmountError(BankingError): pass
class FundsNotFound(BankingError): pass

class Account:
    """
    Representa uma conta bancária simples
    
    Atributes:
        owner (str): Name of the account holder.
        currency (str): Account currency code (e. g. "BRL", "USD").
        balance (float): Current balance of the account.
        
    Methods:
        deposit(aomunt): ...
        withdraw(amount): ...
        show_balance(): ...
        
    Example:
        #(Faria um doctest)
        >>>
        >>>
        >>>
        
    """
    
    def __init__(self, owner: str, currency: str = "BRL", initial_balance: float = 0.0):
        """Docstring Lindo..."""
        
        # Atributos da minha classe
        self.customer = owner
        self.currency = currency
        self._balance = float(initial_balance) #Membro de dados/Atributo protegido, só pode ser usado na própria classe ou em objetos herdados dessa classe.
        self.created_at = datetime.now().isoformat(timespec = "seconds")
        
        if hasattr(self.customer, "add_accounts"):
            self.customer.add_accounts(self)
        
        print(f"[INFO] Account created for {self.customer} in {self.currency} currency.")
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, new_balance: float) -> float:
        if new_balance != new_balance:
            print("[ERROR] Balance cannot be set to NaN.")
            return
        
        self._balance = float(new_balance)
        
    
    def __str__(self):
        return f"Account (owner: {self.customer}), currency: {self.currency}, balance: {self._balance}"
    
    #SUBSTITUIDO POR __str__
    # def show_balance(self) -> None:
    #     print("#"* 60)
    #     print(f"Owner: {self.customer}")
    #     print(f"Balance: {self.balance:.2f} {self.currency}")
    #     print(f"Created at: {self.created_at}")
    #     print("#"* 60)
        
    def withdraw(self, amount: float):
        if  amount <= 0:
            raise NegativeAmountError("[ERROR] Withdrawal must be positive.")
            # print("Withdrawal must be positive.") #SUBSTITUIDO PELO raise
            return
        
        if self._balance < amount:
            print(f"[ERROR] Insuficient balance: {self.balance:.2f} {self.currency}")
            return
        
        self.balance -= amount
        
        return self.balance
        
        print(f"[OK] \nWithdrawal: {amount:.2f} \nNew balance: {self.balance:.2f} {self.currency}")
        
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise NegativeAmountError("[ERROR] Value must be positive.")
            # print("[ERROR] \nValue must be positive.") #SUBSTITUIDO PELO raise
            return
        
        self.balance += amount
        
        print(f"[OK] \nDeposited: {amount:.2f} \nNew balance: {self.balance:.2f} {self.currency}")
    
class Customer:
    """Docstring Lindo"""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._accounts: list[Account] = []
    
    @property
    def accounts(self) -> list[Account]:
        return list(self.accounts)
    
    def add_accounts(self, account: Account):
        if account not in self._account:
            self._account.append(account)
        
        

# Driver Code

acc1 = Account("Lethicia", "BRL", 2000.0)
acc2 = Account("Vitor", "USD", 30.0)

print("Diretório do meu objeto:")
print(dir(acc1))

print("\n", "="*60,"\n")

acc1.withdraw(300)


acc1.show_balance()
print(acc1)

