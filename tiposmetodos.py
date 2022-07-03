class MethodTypes:

    name = "Ragnar"  # Variable de clase

    def instanceMethod(self):   # Metodo de Instancia
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod    #Metodo de clase
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)

    @staticmethod   # Metodo Estatico
    def staticMethod():
        print("This is a static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()

m.classMethod()
m.staticMethod()
