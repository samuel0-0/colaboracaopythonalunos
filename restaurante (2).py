
def bem_vindo ():
 print("=== Bem-vindo ao Restaurante 🤩🤩🤩=== \n Vamos começar sua reserva")

 nome = input("Por favor, informe seu nome: ")
 quantidade_pessoas = input("Quantas pessoas estarão na reserva? ")
 data_reserva = input("Para qual data deseja reservar? (ex: 08/07/2025): ")
 horario_reserva = input("Qual horário deseja reservar? (ex: 19:30): ")

 print(f"Nome: {nome}")
 print(f"Número de pessoas: {quantidade_pessoas}")
 print(f"Data: {data_reserva}")
 print(f"Horário: {horario_reserva}")
 print("\n.")
 print ("Reserva confirmada. \n Obrigada pela sua preferencia")

def cadrastar_restaurante ():
    print("=== Cadrastar restaurante ===")
    nome = input("Por favor, informe o nome do seu restaurante: ")
    cnpj = input ("Insira o CNPJ: ")
    endereco = input ("Insira o endereco do seu restaurante: ")
    print ({"nome": nome, "cnpj": cnpj, "endereco": endereco})
    print("Restaurante cadastrado com sucesso!\n")

def fazer_pedido ():
    pedidos = []

    while True:
        print("=== Fazer pedido ===")
        print("Hamburguer - 30,90\nPizza - 49,90\nSalada variada - 29,90\nBatata frita - 39,90\nPurê de batata - 35,99")
        nome = input("Por favor, informe o nome do pedido: ")
        pedidos.append(nome)
        print("Obrigado por pedir", nome)

        continuar = input("Quer fazer outro pedido? (s/n): ")
        if continuar != 's':
            break

    print("\nPedidos realizados:")
    for i, pedido in enumerate(pedidos, start=1):
        print(f"{i}. {pedido}")

    print("Obrigado! Volte sempre.")

def menu():
    while True:
        print("=== Bem-vindo ao Restaurante 🤩🤩🤩=== \n=== MENU PRINCIPAL ===")
        print("1. Cadastrar Restaurante")
        print("2. Cadastrar Reserva ")
        print("3. Fazer Pedido")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadrastar_restaurante()
        elif opcao == "2":
             bem_vindo ()
        elif opcao == "3":
            fazer_pedido()
        elif opcao == "4":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida.")


menu()