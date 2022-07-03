class SoftwareEngineer:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Software Engineer named {self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}(name = {self.name})"


se = SoftwareEngineer("Eddie")
se1 = SoftwareEngineer("Ricardo")

print(repr(se))
print(str(se))
print(se)
print()
print(str(se1))
print(se1)
