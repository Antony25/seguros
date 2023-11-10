
from datetime import datetime
from dateutil.relativedelta import relativedelta
class ResultResponse():
    def __init__(self, success=False, message=""):
        self.success= success
        self.message = message

    def to_dict(self):
        return {"success":self.success, "message":self.message}



def getAge(date) ->int:
    age = 0
    try:
        today = datetime.today()
        
        result = relativedelta(today,date)
        age =  result.years
    except Exception as e:
        print("Error al obtener la edad")

    return age
    