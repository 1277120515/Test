class Food:
    def __init__(self, cat:str, name:str, desc:str, ls_items:list):
        self.category = cat
        self.name = name
        self.description = desc
        self.ingredients = ls_items
        
    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category
    
    def get_description(self):
        return self.description
    
    def get_ingredients(self):
        return self.ingredients

    def contains(self, to_check) -> bool:
        '''
        Checks if the food description or ingredients contains contents from second argument
        to_check, iterable object or a single str object
        result, bool

        >>> chicken = Food("Mains", "Roast Chicken", "Tender chicken roasted to perfection", ["chicken", "honey"])
        >>> print(chicken.contains("chicken"))
        True
        >>> print(chicken.contains(["bread", "lamb"]))
        False
        >>> print(chicken.contains(["bread", "chicken"]))
        True
        '''
        # Write your answer for Q2.4 here.
        for item in self.ingredients:
            if item in to_check:
                return True
        return self.name in to_check or self.description in to_check
    
    def __str__(self)-> bool:
        '''
        Converts the object into a formatted string.
        Returns:
        str, showing the name of the food and its description on a new line

        Example:
        >>> chicken = Food("Mains", "Roast Chicken", "Tender chicken roasted to perfection", ["chicken", "honey"])
        >>> print(chicken)
        Roast Chicken
        Tender chicken roasted to perfection
        '''
        # Write your answer for Q2.4 here.
        return f"{self.name}\n{self.description}"


