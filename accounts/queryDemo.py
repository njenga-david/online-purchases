from .models import *

customer=Customer.objects.all()
firstCustomer=Customer.objects.first()
lastCustomer=Customer.objects.last()
CustomerByName=Customer.objects.get(name='Maina muhia')
CustomerById=Customer.objects.get(id=4)
