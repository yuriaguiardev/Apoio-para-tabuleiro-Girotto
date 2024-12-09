def menu():
    print("\n=== Menu de Criptografia ===")
    print("1. Criptografia em Geral")
    print("2. Cifra de César")
    print("3. Cifra de Atbash")
    print("4. Criptografia usando a Tabela ASCII")
    print("5. Sair")
    return input("Escolha uma opção (1-5): ")

def criptografia_em_geral():
    print("\n=== Criptografia em Geral ===")
    print(
        "A criptografia é uma técnica usada para proteger informações, "
        "transformando-as de forma que só pessoas autorizadas possam entendê-las. "
        "Ela é amplamente utilizada em sistemas de segurança, como comunicação online, "
        "transações financeiras e armazenamento de dados sensíveis."
    )

def cifra_de_cesar():
    print("\n=== Cifra de César ===")
    print(
        "A Cifra de César é uma técnica de criptografia simples que desloca as letras do alfabeto por um número fixo. "
        "Por exemplo, com um deslocamento de 3, a letra 'A' se torna 'D', 'B' se torna 'E', e assim por diante. "
        "É fácil de implementar, mas também fácil de quebrar."
    )

def cifra_de_atbash():
    print("\n=== Cifra de Atbash ===")
    print(
        "A Cifra de Atbash é uma técnica de criptografia que inverte as letras do alfabeto. "
        "Por exemplo, a letra 'A' se torna 'Z', 'B' se torna 'Y', e assim por diante. "
        "É um método muito antigo e simples, usado em textos históricos."
    )

def criptografia_ascii():
    print("\n=== Criptografia usando a Tabela ASCII ===")
    print(
        "Esse método de criptografia transforma os caracteres de uma mensagem em seus valores ASCII. "
        "Por exemplo, a letra 'A' é representada como 65, e 'B' como 66. "
        "Os valores podem ser manipulados matematicamente (ex.: somando ou subtraindo) para criar uma mensagem cifrada."
    )


while True:
    opcao = menu()
    if opcao == "1":
        criptografia_em_geral()
    elif opcao == "2":
        cifra_de_cesar()
    elif opcao == "3":
        cifra_de_atbash()
    elif opcao == "4":
        criptografia_ascii()
    elif opcao == "5":
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 5.")
