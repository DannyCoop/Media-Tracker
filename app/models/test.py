from dotenv import load_dotenv
from fireo.models import Model
from fireo.fields import TextField

class Testmodel(Model):
    test_id = TextField


test = Testmodel()
test.test_id = "Test_one"
test.save()