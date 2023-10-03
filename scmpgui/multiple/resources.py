from import_export import resources
from .models import *

#import nad export class
class BatchdatasetResource(resources.ModelResource):
    class Meta:
        model = Batchdataset