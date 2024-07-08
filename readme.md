Add description of your project here, can contain images, e.g. ER diagram

Before the application is sent to the server, go into the settings.py file and change DEBUG from 'True' to 'False'

When logging on an admin site, register models (each individually) in admin.py:
admin.site.register(ModelName)
(do not forget to import the models to be registered from models.py)

Use an internal Meta class (i.e. nested class of the class concerned) to automatically order a list of items of a given 
category on the Django server

In models.py add a function that calculates the total cost of a list of chosen products
and updates the stock counts for them. When the order is placed, the total cost needs
to be stored in the database, stock counts updated accordingly and the shopping cart emptied. 
In the opposite scenario, when the shopping cart is not checked out within a certain time, 
deleting its content and refreshing the stock counts to the original values.

Forms can be defined either in views.py or in another (independent) file like forms.py

Consider using 'edit emojis' for updating and deleting forms

Installing 'Pillow' module to enable working with ImageField



