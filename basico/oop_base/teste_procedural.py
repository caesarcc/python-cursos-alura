from teste_procedural_conta import cria_conta, deposita, saca, extrato

if __name__ == "__main__":
    conta = cria_conta(123, "Nico", 55.0, 1000.0)
    deposita(conta, 300.0)
    extrato(conta)
    saca(conta, 100.0)
    extrato(conta)
