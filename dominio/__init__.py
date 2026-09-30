# Este arquivo serve para facilitar os imports do nosso projeto.
# Aqui estamos dizendo quais classes podem ser importadas
# diretamente da pasta "dominio".

from .item import Item, Bebida, Prato

# Importamos as três classes de desconto.
from .desconto import SemDesconto, Percentual, ValorFixo

# Importamos a Comanda e o erro específico de comanda fechada.
from .comanda import Comanda, ComandaFechadaError