from generic_app.models import *

from generic_app.submodels.DemoProject.UploadFile.Period import Period
class Report(UploadModelMixin, Model):
    
    id = AutoField(default=0)
    period = ForeignKey(to=Period, on_delete=)
    cfs-py-pw = FileField(default=)
    
    def update(self):
        # TODO specify what you want to do once the model has been saved
        pass
