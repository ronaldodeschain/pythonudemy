#Criando datas com modulo datetime
#https://dateutil.readthedocs.io/en/stable/relativedelta.html
#instalando o pytz
#pip install pytz types-pytz

from datetime import datetime,timedelta
from pytz import timezone
# data = datetime(2022,4,20)
# print(data)
# print(datetime.now(timezone('Asia/Hong_Kong')))
fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('03/02/1985 09:00:00',fmt)
data_fim = datetime.strptime('12/05/2025 16:04:00',fmt)
#essa função vai ser util para criar um verificador do tempo
#entre postagem e prazo de verificacao do status
delta = timedelta(days=10)
print(data_fim - delta)