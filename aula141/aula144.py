# polimorfismo em Python orientado a objetos'
# Polimorfismo é o principio que permite que
# classes derivadas de uma mesma superclasse
# tenham métodos iguais(com a mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = mesmo nome e quantidade 
# de parametros(retorno não faz parte da assinatura)
# Opiniao + principios que contam:
# Assinatura do método: nome, parametros e retornos iguais
# So"L"ID 
# Principio da substituição de liskov
# Objetos de uma superclasse devem ser substituiveis
# por objetos de uma subclasse sem quebrar a aplicação
# sobrecarga de métodos (overload)
# sobreposição de métodos(override)
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('email: enviando: ',self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando: ',self.mensagem)   
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificacao enviada ')
    else:
        print('Notficacao nao enviada')

notificar(NotificacaoEmail('testando email'))
notificar(NotificacaoSMS('testando sms'))