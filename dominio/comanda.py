# Este arquivo representa a Comanda.


# Importamos o desconto padrão.
from .desconto import SemDesconto

# Importamos a classe Item.
from .item import Item


# Criamos um erro específico para quando alguém
# tentar mexer em uma comanda que já foi fechada.
class ComandaFechadaError(Exception):

    # Não precisamos colocar nada aqui.
    # A existência dessa classe já permite criar
    # um erro específico para esse problema.
    pass


# Criamos a classe Comanda.
class Comanda:

    # Este método é executado quando criamos uma nova comanda.
    #
    # mesa = número da mesa
    # desconto = desconto que será usado
    def __init__(self, mesa, desconto=None):

        # O número da mesa precisa ser maior que zero.
        if mesa <= 0:

            # Se for zero ou negativo, mostramos um erro.
            raise ValueError("número da mesa deve ser positivo")

        # Guardamos o número da mesa.
        self.mesa = mesa

        # Criamos uma lista vazia para guardar os itens.
        #
        # A Comanda TEM itens.
        # Isso é composição.
        self._itens = []

        # Guardamos o desconto escolhido.
        #
        # Se nenhum desconto for informado,
        # usamos SemDesconto().
        self.desconto = desconto or SemDesconto()

        # No começo, a comanda está aberta.
        #
        # False significa "não está fechada".
        self._fechada = False

    # @property permite usar o método como se fosse uma variável.
    #
    # Em vez de:
    # c.itens()
    #
    # podemos usar:
    # c.itens
    @property
    def itens(self):

        # Retornamos uma cópia da lista.
        #
        # Isso impede que alguém de fora
        # altere diretamente nossa lista original.
        return list(self._itens)

    # Propriedade que informa se a comanda está fechada.
    @property
    def fechada(self):

        # Retorna True ou False.
        return self._fechada

    # Método usado para adicionar um item na comanda.
    def adicionar_item(self, item):

        # Primeiro verificamos se a comanda já está fechada.
        if self._fechada:

            # Se estiver fechada, não podemos adicionar nada.
            raise ComandaFechadaError(
                "comanda fechada não recebe itens"
            )

        # Verificamos se o que foi enviado realmente é um Item.
        if not isinstance(item, Item):

            # Se não for Item, mostramos um erro.
            raise TypeError(
                "só é possível adicionar um Item"
            )

        # Se passou pelas validações,
        # colocamos o item dentro da lista.
        self._itens.append(item)

    # Método usado para trocar o desconto.
    def trocar_desconto(self, desconto):

        # Não podemos trocar o desconto depois
        # que a comanda foi fechada.
        if self._fechada:

            # Mostramos um erro.
            raise ComandaFechadaError(
                "comanda fechada não muda de desconto"
            )

        # Se a comanda ainda estiver aberta,
        # guardamos o novo desconto.
        self.desconto = desconto

    # Método responsável por fechar a comanda.
    def fechar(self):

        # Não podemos fechar uma comanda sem itens.
        if not self._itens:

            # Mostramos um erro.
            raise ValueError(
                "não é possível fechar uma comanda vazia"
            )

        # Se tiver pelo menos um item,
        # mudamos o estado para fechada.
        self._fechada = True

    # Propriedade que calcula o subtotal.
    @property
    def subtotal(self):

        # sum() soma os preços de todos os itens.
        #
        # Para cada item dentro de self._itens,
        # pegamos o preço dele.
        return sum(i.preco for i in self._itens)

    # Propriedade que calcula o total final.
    @property
    def total(self):

        # Chamamos o método aplicar() do desconto.
        #
        # Aqui acontece o polimorfismo:
        # pode ser SemDesconto, Percentual ou ValorFixo.
        return self.desconto.aplicar(self.subtotal)