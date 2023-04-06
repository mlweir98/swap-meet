from uuid import uuid4
from uuid import getnode

class Item:
    def __init__(self, id = None, condition = 0, age = 0):
        self.id = id if id is not None else uuid4().int
        # self.id = int(uuid4())
        self.condition = condition
        self.conditions_dict = {
            0: "There is a very evil, ancient spirit attached to this item",
            1: "We unearthed this from a haunted gravesite",
            2:"We unearthed this from an unhaunted gravesite",
            3:"This item has never been buried in a gravesite",
            4:"This item is used, but has never been haunted",
            5:"This item is brand new and has had no opportunity to be touched by the spirits...yet"}
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        return self.conditions_dict[self.condition]
        
# In Wave 2 we will create the `Item` class and the `Vendor` class' `get_by_id` method.

# - There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

# - Inside this module, there is a class named `Item`
# - Each `Item` will have an attribute named `id`, which is a unique integer by default
#   - There are many ways to generate numbers, but generating numbers without duplicates takes some care. Happily, Python has a package called `uuid` that can help!
#     - If we import the [`uuid` package](https://docs.python.org/3/library/uuid.html) in `item.py`, with a little research we can use one of the functions `uuid` provides to create large ***unique*** numbers meant to be used as identifiers
#     - Specifically, you'll need to choose which of the `uuid` package's functions to use, so be sure to consider which function will work best for creating a unique integer
#     - Note that this package's functions return `UUID` objects, not integers as such, **but** `UUID` objects have [an attribute `int`](https://docs.python.org/3/library/uuid.html#uuid.UUID.int) which allow us to access their value as an integer
# - When we initialize an instance of `Item`, we can optionally pass in an integer with the keyword argument `id` to manually set the `Item`'s `id`
# - Each `Item` will have a function named `get_category`, which will return a string holding the name of the class
    
# print(hex)
# print(int(uuid4()))