from datetime import *
def diffDate(x):
    x = datetime.strptime(x,'%Y-%m-%d').date()
    y = datetime.date(datetime.now())
    z = y - x
    return z

a = diffDate('2018-12-30')
print('selisihnya adalah', a.days, 'hari')