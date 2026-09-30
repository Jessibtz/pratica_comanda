# Este arquivo contém as classes responsáveis pelos descontos.


# Classe que representa uma comanda sem desconto.
class SemDesconto:

    # O método aplicar recebe o subtotal.
    def aplicar(self, subtotal):

        # Como não existe desconto,
        # simplesmente devolvemos o mesmo valor.
        return subtotal


# Classe que representa um desconto percentual.
#
# Exemplo:
# subtotal = 100
# desconto = 10%
# resultado = 90
class Percentual:

    # Criamos o desconto recebendo a porcentagem.
    def __init__(self, pct):

        # O desconto precisa estar entre 0 e 100.
        if not 0 <= pct <= 100:

            # Se estiver fora dessa faixa, mostramos um erro.
            raise ValueError("percentual deve estar entre 0 e 100")

        # Guardamos a porcentagem no objeto.
        self.pct = pct

    # Método responsável por aplicar o desconto.
    def aplicar(self, subtotal):

        # Calculamos o valor depois do desconto.
        #
        # Exemplo:
        # subtotal = 100
        # pct = 10
        #
        # 100 * (100 - 10) / 100
        # = 90
        return subtotal * (100 - self.pct) / 100


# Classe que representa um desconto de valor fixo.
#
# Exemplo:
# subtotal = 100
# desconto = R$ 20
# resultado = 80
class ValorFixo:

    # Criamos o desconto recebendo um valor.
    def __init__(self, valor):

        # O desconto não pode ser negativo.
        if valor < 0:

            # Se for negativo, mostramos um erro.
            raise ValueError("valor do desconto não pode ser negativo")

        # Guardamos o valor do desconto.
        self.valor = valor

    # Método responsável por aplicar o desconto.
    def aplicar(self, subtotal):

        # Subtraímos o desconto do subtotal.
        #
        # max(..., 0) garante que o resultado
        # nunca fique abaixo de zero.
        #
        # Exemplo:
        # subtotal = 50
        # desconto = 60
        #
        # 50 - 60 = -10
        #
        # Mas o total não pode ser negativo.
        # Então o resultado será 0.
        return max(subtotal - self.valor, 0)