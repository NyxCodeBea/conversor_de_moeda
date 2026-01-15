# A Primeira versão converte apenas do Real para as outras moedas

# --- 1. Configurações e Dados ---

valor_coverter = 0
moeda_conversao = 0
moeda_convertida = 0
valor_covertido = 0

moeda_conversao = {
    1: "Dólar Americano",
    2: "Euro",
    3: "Libra Esterlina",
    4: "Yuan Chinês",
    5: "Won sul-coreano"
}


moeda_convertida = {
    1: "Real Brasileiro"
}


def conversor_moeda_rb(valor_coverter,moeda_conversao,): ## Convertido para Real Brasileiro
    moeda_calculo = "Real Brasileiro"
    if(moeda_conversao == 1):
        valor_covertido = float(valor_coverter * (1 * 5.38)) ## Aqui o calculo (1 * 5.38) o 1 representa a moeda de conversão e o 5.38 é a moeda convertida
        print(f"Quanto vale $ {valor_coverter:.2f} Dólar Americano em {moeda_calculo}?")
        print(f"$ {valor_coverter:.2f} == R$ {valor_covertido:.2f}")
    elif(moeda_conversao == 2):
        valor_covertido = float(valor_coverter * (1 * 6.27))
        print(f"Quanto vale € {valor_coverter:.2f} Euro em {moeda_calculo}?")
        print(f"€ {valor_coverter:.2f} == R$ {valor_covertido:.2f}")
    elif(moeda_conversao == 3):
        valor_covertido = float(valor_coverter * (1 * 7.24))
        print(f"Quanto vale £ {valor_coverter:.2f} Libra Esterlina em {moeda_calculo}?")
        print(f"£ {valor_coverter:.2f} == R$ {valor_covertido:.2f}")
    elif(moeda_conversao == 4):
        valor_covertido = float(valor_coverter * (1 * 0.77))
        print(f"Quanto vale ¥ {valor_coverter:.2f} Yuan Chinês em {moeda_calculo}?")
        print(f"¥ {valor_coverter:.2f} == R$ {valor_covertido:.2f}")
    elif(moeda_conversao == 5):
        valor_covertido = float(valor_coverter * (1 * 0.0037))
        print(f"Quanto vale ₩ {valor_coverter:.2f} Won sul-coreano em {moeda_calculo}?")
        print(f"₩ {valor_coverter:.2f} == R$ {valor_covertido:.2f}")
    else:
        print("Erro.")
# --- 2. Recebendo as Informações do usuário ---

print("Calculadora Conversor de Moeda")

while True:
    comecar = input("Converter Moedas? S (sim) ou N (não)")
    if(comecar.upper() == "N"):
        print("Encerrando Calculo de conversor...\n")
        break
    else:
        try:
            valor_coverter = float(input("Insira o valor a converter: "))

            print("Convertemos para: 1 - Dólar Americano / 2 - Euro / 3 - Libra Esterlina / 4 - Yuan Chinês / 5 - Won sul-coreano")
            moeda_conversao = int(input("Moeda para conversão: "))
            print("Convertemos para: 1 - Real Brasileiro")
            moeda_convertida_usuario = int(input("Moeda convertida: "))

            # --- 2. Resultado da Conversão ---
            print(f"{conversor_moeda_rb(valor_coverter,moeda_conversao)}")

        except ValueError:
            print("Ops! Você precisa digitar um número válido.")
