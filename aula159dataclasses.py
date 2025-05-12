#dataclasses - o que são dataclasses
#o modulo dataclasses fornece um decoracador
#e funções para criar métodos como __init__(),
# __repr__(),__eq__() (entre outros) em classes
#definidas pelo usuario.
#Em resumo: dataclasses são syntax sugar para criar classes
#normais.Foi descrito na PEP 557 e adicionado
# na versão 3.7 do Python
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass,field
@dataclass
class Pessoa:
    nome: str
    sobrenome: str 
    idade: int = 100
    enderecos: list[str] = field(default_factory=list)
    
   
if __name__ == '__main__':
 p1 = Pessoa('Luiz','jucarlos')

print(p1)