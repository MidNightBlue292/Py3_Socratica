import logging  # print(dir(logging))
import math

# Logging
# Purpose: record progress and problems...
# Levels: Debug, Info, Warning, Error, Critical

# Level: NOTSET / DEBUG / INFO / WARNING / ERROR / CRITICAL
# Value: 0      / 10    / 20   / 30      / 40    / 50

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='bugs.log',
                    level= logging.DEBUG,  # DEBUG = all errors / ERROR = error, critical
                    format= LOG_FORMAT,
                    filemode= 'a')
logger = logging.getLogger()


def quadratic_formula(a, b, c):
    """
    Return the solutions to the equation
    ax² + bx + c = 0
    :param a:
    :param b:
    :param c:
    :return:
    """
    logger.info(f'quadratic_formula({a}, {b}, {c})')

    # Compute the discriminant
    logger.debug('# Compute the discriminant')
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug('# Compute the two roots')
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # Return the roots
    logger.debug('# Return the roots')
    return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)


"""
logger.info('Our first message')
print(logger.level)

# Test messages
logger.debug('Debug message.')
logger.info('Info message.')
logger.warning('Warning message.')
logger.error('Error message.')
logger.critical('Critical message.')
"""

"""
Modos de acesso a arquivos:

Os modos de acesso a um arquivo disponíveis em Python estão listados na tabela a seguir:

Modo 	Tipo de acesso

r 	    Somente leitura.
w 	    Escrita, apagando (truncando) o conteúdo existente no arquivo.
a 	    Escrita, preservando o conteúdo existente (append).
        O arquivo é criado, se não existir.
        O texto é inserido no final do arquivo.
b 	    Modo binário.
+ 	    Abre o arquivo para atualização – leitura e escrita.
x 	    Abre o arquivo para criação exclusiva, falhando se o arquivo já existir.
t 	    Modo de texto (padrão).

Podemos combinar os modos, por exemplo r+, w+, w+b.
"""
