from taskecommerce.user.Registration import register
from taskecommerce.user.Authentication import login
from taskecommerce.order.order_management import order

register()
if login():
    order()
else:
    print("User doesnt exists")
