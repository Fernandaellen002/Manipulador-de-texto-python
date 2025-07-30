from manipulador import ManipuladorTexto

def main():
    manipulador = ManipuladorTexto('texto.txt')

    print(manipulador)  #__str__ eh usado para que fique mais legivel

    print("\n1. Palavras que começam com 'p':")
    print(manipulador.palavras_comecam_com('p'))

    print("\n2. Palavras que contêm a letra 'a':")
    print(manipulador.palavras_contem_letra('a'))

    print("\n3. Texto com vírgulas substituídas por pontos:")
    print(manipulador.substituir_virgulas())

    print("\n4. Datas encontradas:")
    print(manipulador.extrair_datas())

    print("\n6. Quantidade de palavras no texto:")
    print(len(manipulador))  # __len__ eh usado para essa funçao de palavras no texto

if __name__ == "__main__":
    main()
