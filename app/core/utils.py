class ResultResponse():
    def __init__(self, success=False, message=""):
        self.success= success
        self.message = message

    def to_dict(self):
        return {"success":self.success, "message":self.message}
