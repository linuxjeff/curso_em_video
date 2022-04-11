# aula-6-desafio-2.py mostra varios "is"
#
# Site :  https://github.com/linuxjeff
# Autor:  Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
# Pede ao uauário que digite algo e devolve varios "is" como informações.
#
#       Exemplos:
#		./aula-6-desafio-2.py
# -----------------------------------------------------------------------------
# Histórico:
#
#   v0.0.1 2022-03-19, Jefferson Santana:
#       - Versão inicial
#
# -----------------------------------------------------------------------------
# Licença: MTI

###############################################################################
#                             Variáveis                                       #
###############################################################################

algos = input('Digite algo: ')

###############################################################################
#                             Programa Principal                              #
###############################################################################

print('O que foi digitado é alfabeto?\n {}'.format(algos.isalpha()))
print('O que foi digitado é número?\n {}'.format(algos.isnumeric()))
print('O que foi digitado é alfanumerico?\n {}'.format(algos.isalnum()))
print('O que foi digitado está em letras minúsculas?\n {}'.format(algos.islower()))
print('O que foi digitado está em letras maiúsculas?\n {}'.format(algos.isupper()))
print('O que foi digitado é um espaço em branco?\n {}'.format(algos.isspace()))
print('O que foi digitado esta dentro da tabela ASCII?\n {}'.format(algos.isascii()))
