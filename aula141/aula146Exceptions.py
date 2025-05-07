#Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, voce só
# precisa herdar de alguma exceção da linguagem.
# A recomendaçao da doc é herdar de Exception.
# https://doc.python.org/3/library/exceptions.html
#Criando exceções (comum colocar Error ao final)
#Levantando(raise)/lançando (throw) exceções
#Relançando exceções
#Adicionando notas em exceções(3.11.0)
class MeuError(Exception):
    ...

def levantar():
    exception_ = MeuError('a mensagem do erro')
    raise exception_

try:
    levantar()
except MeuError as error:
    print(error)