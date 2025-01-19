from datetime import datetime, timedelta


class FoodProduct:
    def __init__(self, name, price, category, production_date, expiration_date):
        self.__name = name
        self.__price = price
        self.__category = category
        self.__production_date = production_date
        self.__expiration_date = expiration_date

    # Name Property with validation
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Product name must be at least 3 characters long")
        if value == value[0] * len(value):
            raise ValueError("Product name cannot be the same letter repeated")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not (0.1 <= value <= 100):
            raise ValueError("Price must be between 0.1 and 100")
        self.__price = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in ["Dairy", "Parve", "Meat"]:
            raise ValueError("Category must be 'Dairy', 'Parve', or 'Meat'")
        self.__category = value

    @property
    def production_date(self):
        return self.__production_date

    @production_date.setter
    def production_date(self, value):
        if value > datetime.now():
            raise ValueError("Production date must be in the past")
        self.__production_date = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if value < datetime.now() + timedelta(weeks=1):
            raise ValueError("Expiration date must be at least one week in the future")
        self.__expiration_date = value

    @property
    def remaining(self):
        return (self.__expiration_date - datetime.now()).days

    def __add__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price + other.__price
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price - other.__price
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price * other.__price
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price == other.__price and self.__name == other.__name
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, FoodProduct):
            return not self.__eq__(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price > other.__price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, FoodProduct):
            return self.__price < other.__price
        return NotImplemented

    def __hash__(self):
        return hash((self.__name, self.__price, self.__category, self.__production_date, self.__expiration_date))

    def __len__(self):
        return (self.__expiration_date - self.__production_date).days

    def __str__(self):
        return (f"Name: {self.__name}, Price: {self.__price}, Category: {self.__category}, "
                f"Production Date: {self.__production_date}, Expiration Date: {self.__expiration_date}")

    def __repr__(self):
        return (f"FoodProduct(name={self.__name!r}, price={self.__price!r}, category={self.__category!r}, "
                f"production_date={self.__production_date!r}, expiration_date={self.__expiration_date!r})")
