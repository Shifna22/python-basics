# Create a Teacher class with a teach() method and a Researcher class with
# a research() method. Create a Professor class that inherits from both. Create an
# object and call both methods.

class teacher:
    def teach():
        print("teacher teach")
class researcher:
    def research():
        print("researcher research")
class professor(teacher,researcher):
    pass
professor1=professor()
teacher.teach()
researcher.research()