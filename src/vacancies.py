class Vacancy:
    def __init__(self, name, salary, url, requirements, location, *args):
        self.__name = name
        self.__salary = salary
        self.__url = url
        self.__requirements = requirements
        self.__location = location
        self.list = ','.join(args)

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def url(self):
        return self.__url

    @property
    def requirements(self):
        return self.__requirements

    @property
    def location(self):
        return self.__location

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.salary == other.salary

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.salary < other.salary
