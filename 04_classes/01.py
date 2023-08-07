class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'(Initialized SchoolMember: {self.name})')

    def tell(self):
        '''Tell my details.'''
        print(f'Name:{self.name} Age:{self.age}', end=' ')


class Teacher(SchoolMember):
    '''Represents a teacher.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f'(Initialized Teacher: {self.name})')

    def tell(self):
        SchoolMember.tell(self)
        print(f'Salary: {self.salary}')


class Student(SchoolMember):
    '''Represents a student.'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f'(Initialized Student: {self.name})')

    def tell(self):
        SchoolMember.tell(self)
        print(f'Marks: {self.marks}')


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Meow', 25, 75)
# prints a blank line
print()
members = [t, s]
for member in members:
    # Works for both Teachers and Students
    member.tell()
