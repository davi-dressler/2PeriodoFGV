"""Primeira aula sobre programação orientada a objetos.

Data: 24/10
Prof.: Rafael Pinho


"""

from datetime import datetime

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
        self.owner = owner
        self.currency = currency
        self._balance = float(initial_balance) #Membro de dados/Atributo protegido, só pode ser usado na própria classe ou em objetos herdados dessa classe.
        self.created_at = datetime.now().isoformat(timespec = "seconds")
        
        print(f"[INFO] Account created for {self.owner} in {self.currency} currency.")
        
    def get_balance(self) -> float:
        return self._balance
    
    def set_balance(self, new_balance: float) -> float:
        if new_balance != new_balance:
            print("[ERROR] Balance cannot be set to NaN.")
            return
        
        self._balance = float(new_balance)
        return self._balance
    
    def show_balance(self) -> None:
        print("#"* 60)
        print(f"Owner: {self.owner}")
        print(f"Balance: {self._balance:.2f} {self.currency}")
        print(f"Created at: {self.created_at}")
        print("#"* 60)
        
    def withdraw(self, amount: float):
        if  amount <= 0:
            print("Withdrawal must be positive.")
            return
        
        if self._balance < amount:
            print(f"[ERROR] Insuficient balance: {self._balance:.2f} {self.currency}")
            return
        
        self._balance -= amount
        
        print(f"[OK] \nWithdrawal: {amount:.2f} \nNew balance: {self._balance:.2f} {self.currency}")
        
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("[ERROR] \nValue must be positive.")
            return
        
        self._balance += amount
        
        print(f"[OK] \nDeposited: {amount:.2f} \nNew balance: {self._balance:.2f} {self.currency}")
        
        

# Driver Code

acc1 = Account("Lethicia", "BRL", 2000.0)
acc2 = Account("Vitor", "USD", 30.0)

print("Diretório do meu objeto:")
print(dir(acc1))

print("\n", "="*60,"\n")

acc1.withdraw(100)


acc1.show_balance()


        
    
        
        
    
    