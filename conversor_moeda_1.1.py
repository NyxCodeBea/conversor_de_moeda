# --- 1. Configurações e Dados ---

# Dicionário de Nomes (A Agenda)
nomes_moedas = {
    1: "Dólar Americano",
    2: "Euro",
    3: "Libra Esterlina",
    4: "Yuan Chinês",
    5: "Won sul-coreano"
}

# Dicionário de Taxas (A Tabela de Preços)
taxas_conversao = {
    (1, 1): 5.38,   # Dólar -> Real
    (2, 1): 5.90,   # Euro -> Real
    (3, 1): 6.80,   # Libra -> Real
    (4, 1): 0.78,   # Yuan -> Real
    (5, 1): 0.0042  # Won -> Real
}

# Dicionário de Símbolos
simbolos_moedas = {
    1: "$",   # Dólar
    2: "€",   # Euro
    3: "£",   # Libra
    4: "¥",   # Yuan
    5: "₩"    # Won
}

# Nome da moeda de destino (Fixo no Real por enquanto)
nomes_destino = {
    1: "Real Brasileiro"
}

def conversor_moeda(valor, id_origem, id_destino): 
    # Agora a função recebe tudo o que precisa para trabalhar!
    
    # 1. Busca a taxa usando a TUPLA (origem, destino)
    # Exemplo: Se id_origem for 2 e id_destino for 1, busca (2, 1)
    taxa = taxas_conversao[id_origem, id_destino]
    
    # 2. Busca o nome da moeda e simbolos
    nome_origem = nomes_moedas[id_origem]
    nome_destino = nomes_destino[id_destino]
    simbolo_origem = simbolos_moedas[id_origem]

    # 3. Faz o cálculo
    valor_final = valor * taxa

    # 4. Mostra o resultado
    print(f"Quanto vale {simbolo_origem} {valor:.2f} {nome_origem} em {nome_destino}?")
    print(f"Resultado: R$ {valor_final:.2f}")


# --- 2. Recebendo as Informações do usuário ---

print("Calculadora Conversor de Moeda")

while True:
    comecar = input("\nConverter Moedas? S (sim) ou N (não): ")
    if comecar.upper() == "N":
        print("Encerrando Calculo de conversor...\n")
        break
    else:
        try:
            # 1. Pede o VALOR e guarda na variável 'valor_usuario'
            valor_usuario = float(input("Insira o valor a converter: "))

            print("Moedas disponíveis: 1-Dólar / 2-Euro / 3-Libra / 4-Yuan / 5-Won")
            
            # 2. Pede a ORIGEM e guarda na variável 'escolha_origem'
            escolha_origem = int(input("Moeda de origem (código): "))

            # 3. Pede o DESTINO e guarda na variável 'escolha_destino'
            print("Converter para: 1 - Real Brasileiro")
            escolha_destino = int(input("Moeda de destino (código): "))

            # --- CHAMADA DA FUNÇÃO ---
            # Aqui enviamos as 3 informações que coletamos para a função trabalhar
            conversor_moeda(valor_usuario, escolha_origem, escolha_destino)

        except ValueError:
            print("Ops! Você precisa digitar um número válido.")
        except KeyError:
            print("Erro: Código de moeda não encontrado no sistema.")