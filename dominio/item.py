# Criamos a classe Item.
# Ela representa qualquer item que pode existir na comanda.
class Item:

    # __init__ é executado automaticamente quando criamos um Item.
    #
    # "self" representa o próprio objeto.
    # "nome" será o nome do item.
    # "preco" será o preço do item.
    def __init__(self, nome, preco):

        # Verificamos se o nome está vazio.
        #
        # not nome verifica se não foi informado um nome.
        # nome.strip() remove espaços do começo e do final.
        if not nome or not nome.strip():

            # Se o nome estiver vazio, mostramos um erro.
            raise ValueError("nome do item não pode ser vazio")

        # Verificamos se o preço é menor que zero.
        if preco < 0:

            # Se for negativo, mostramos um erro.
            raise ValueError("preço não pode ser negativo")

        # Guardamos o nome dentro do objeto.
        # strip() remove espaços desnecessários.
        self.nome = nome.strip()

        # Guardamos o preço dentro do objeto.
        self.preco = preco

    # Este método serve para mostrar uma descrição do item.
    def descricao(self):

        # Retornamos o nome e o preço.
        #
        # O f antes das aspas permite colocar variáveis dentro do texto.
        return f"{self.nome}: R$ {self.preco}"


# Bebida é uma classe que HERDA de Item.
#
# Isso significa que uma Bebida é um tipo de Item.
class Bebida(Item):

    # Criamos uma bebida com nome, preço e quantidade em ml.
    def __init__(self, nome, preco, ml):

        # Chamamos o __init__ da classe Item.
        #
        # Isso faz a Bebida aproveitar as validações
        # de nome e preço que já fizemos em Item.
        super().__init__(nome, preco)

        # Guardamos a quantidade de ml da bebida.
        self.ml = ml

    # A Bebida terá uma descrição própria.
    def descricao(self):

        # Pegamos primeiro a descrição que existe em Item.
        base = super().descricao()

        # Acrescentamos a quantidade de ml.
        return f"{base} ({self.ml} ml)"


# Prato também HERDA de Item.
#
# Um prato também é um Item.
class Prato(Item):

    # Criamos um prato com nome, preço e tempo de preparo.
    def __init__(self, nome, preco, minutos):

        # Chamamos o __init__ da classe Item.
        #
        # Assim o prato também passa pelas validações
        # de nome e preço.
        super().__init__(nome, preco)

        # Guardamos o tempo de preparo.
        self.minutos = minutos

    # O prato terá uma descrição própria.
    def descricao(self):

        # Pegamos a descrição básica do Item.
        base = super().descricao()

        # Acrescentamos o tempo de preparo.
        return f"{base} (~{self.minutos} min)"