# --- 1. Configurações e Dados ---

valor_converter = 0
valor_convertido = 0

moeda_conversao = {
    1: "Dólar Americano",
    2: "Euro",
    3: "Libra Esterlina",
    4: "Yuan Chinês",
    5: "Won sul-coreano"
}

taxas_conversao = {
    (1, 1): 5.38,   # Dólar Americano para Real Brasileiro
    (2, 1): 5.90,   # Euro para Real Brasileiro
    (3, 1): 6.80,   # Libra Esterlina para Real Brasileiro
    (4, 1): 0.78,   # Yuan Chinês para Real Brasileiro
    (5, 1): 0.0042  # Won sul-coreano para Real Brasileiro
}

moeda_convertida = {
    1: "Real Brasileiro"
}


id_moeda = []

def conversor_moeda_rb(valor_converter,moeda_conversao,): 

    taxa = taxas_conversao[id_moeda, moeda_convertida]
    nome_moeda = moeda_conversao[id_moeda]

    valor_convertido = float(valor_converter * taxa) 

    print(f"Quanto vale $ {valor_converter:.2f} {nome_moeda} em {moeda_convertida}?")
    print(f"$ {valor_converter:.2f} == R$ {valor_convertido:.2f}")
    print(f"Resultado: R$ {valor_convertido:.2f}")


# --- 2. Recebendo as Informações do usuário ---

print("Calculadora Conversor de Moeda")

while True:
    comecar = input("Converter Moedas? S (sim) ou N (não)")
    if(comecar.upper() == "N"):
        print("Encerrando Calculo de conversor...\n")
        break
    else:
        try:

            valor_cnoverter = float(input("Insira o valor a converter: "))

            print("Convertemos para: 1 - Dólar Americano / 2 - Euro / 3 - Libra Esterlina / 4 - Yuan Chinês / 5 - Won sul-coreano")
            moeda_conversao = int(input("Moeda para conversão: "))

            print("Convertemos para: 1 - Real Brasileiro")
            moeda_convertida_usuario = int(input("Moeda convertida: "))

            # --- 2. Resultado da Conversão ---
            conversor_moeda_rb(valor_converter,moeda_conversao)

        except ValueError:
            print("Ops! Você precisa digitar um número válido.")
