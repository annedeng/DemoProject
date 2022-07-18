from generic_app.models import *

class Period(UploadModelMixin, Model):
    
    id = AutoField(default=0)
    unit_list = FileField(default=)
    cashflow_list = FileField(default=)
    
    def update(self):
        # TODO specify what you want to do once the model has been saved

        

        pass
