from generic_app.models import *

from generic_app.submodels.DemoProject.TabularInput.Windpark import Windpark
class Cashflows(Model):
    
    id = AutoField(default=0)
    windpark = ForeignKey(to=Windpark, on_delete=)
    date = DateTimeField(default=)
    amount = FloatField(default=)
    