from generic_app.models import *

from generic_app.submodels.DemoProject.UploadFile.Period import Period
class Windpark(Model):
    
    id = AutoField(default=0)
    period = ForeignKey(to=Period, on_delete=CASCADE)
    name = TextField(default=)
    country = TextField(default=)
    