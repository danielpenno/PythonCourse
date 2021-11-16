class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)
