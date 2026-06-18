# Lista global para armazenar as anotações (Item 2 do passo a passo)
anotacoes = []


def exibir_menu():
    """Exibe as opções do menu no terminal."""
    print("\n" + "=" * 35)
    print("      MINI-ASSISTENTE DE ANOTAÇÕES      ")
    print("=" * 35)
    print("1. Adicionar uma anotação")
    print("2. Listar todas as anotações")
    print("3. Buscar anotações")
    print("4. Remover uma anotação")
    print("5. Sair do sistema")
    print("=" * 35)


def adicionar_anotacao():
    """Solicita o texto ao usuário e salva na lista."""
    texto = input("Digite a sua anotação: ").strip()
    if texto:
        anotacoes.append(texto)
        print("✓ Anotação adicionada com sucesso!")
    else:
        print("⚠ Erro: Não é possível adicionar uma anotação vazia.")


def listar_anotacoes():
    """Itera sobre a lista e imprime as anotações com seus índices."""
    if not anotacoes:
        print("i Nenhuma anotação registrada ainda.")
        return False  # Retorna False para ajudar a função de remoção
    else:
        print("\n--- SUAS ANOTAÇÕES ---")
        for indice, anotacao in enumerate(anotacoes):
            print(f"[{indice}] {anotacao}")
        return True


def buscar_anotacao():
    """Verifica se uma palavra-chave está contida nas anotações."""
    if not anotacoes:
        print("i Nenhuma anotação cadastrada para realizar a busca.")
        return

    palavra_chave = input("Digite a palavra-chave para buscar: ").strip().lower()
    encontradas = []

    for indice, anotacao in enumerate(anotacoes):
        if palavra_chave in anotacao.lower():
            encontradas.append((indice, anotacao))

    if encontradas:
        print(f"\n--- RESULTADOS PARA '{palavra_chave}' ---")
        for indice, anotacao in encontradas:
            print(f"[{indice}] {anotacao}")
    else:
        print(f"i Nenhuma anotação contém a palavra '{palavra_chave}'.")


def remover_anotacao():
    """Exibe os índices disponíveis e permite escolher qual remover com validação."""
    # Só tenta remover se existirem anotações listadas
    tem_anotacoes = listar_anotacoes()
    if not tem_anotacoes:
        return

    try:
        indice_input = input(
            "\nDigite o número da anotação que deseja remover: "
        ).strip()
        indice = int(indice_input)

        if 0 <= indice < len(anotacoes):
            removida = anotacoes.pop(indice)
            print(f"✓ Anotação '[{indice}] {removida}' removida com sucesso!")
        else:
            print("⚠ Erro: Índice inválido. Número fora do alcance.")
    except ValueError:
        print("⚠ Erro: Entrada inválida. Você deve digitar um número inteiro.")


def principal():
    """Loop principal que controla o menu e as escolhas."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            adicionar_anotacao()
        elif opcao == "2":
            listar_anotacoes()
        elif opcao == "3":
            buscar_anotacao()
        elif opcao == "4":
            remover_anotacao()
        elif opcao == "5":
            print("\nEncerrando o Mini-Assistente... Até logo!")
            break
        else:
            print("⚠ Opção inválida! Digite um número de 1 a 5.")


# Inicializa o programa
if __name__ == "__main__":
    principal()