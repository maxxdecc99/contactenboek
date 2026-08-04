class Contact:
    def __init__(self, name, number, email) -> None:
        self.name = name
        self.number = number
        self.email = email


    def __str__(self) -> str:
        return f"mr/ms {self.name} is available on telephone number: {self.number} and email-adress: {self.email}"


    def to_dict(self):
        return {"name": self.name, "number": self.number, "email": self.email}


if __name__ == "__main__":
    c = Contact("Jan Jansen", "0612345678", "jan@mail.com")
    print(c)
