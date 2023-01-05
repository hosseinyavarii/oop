class students: 
  def __init__(self, fname, lname , age , section):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.section = section
  def person(self):
    result = 2022 - self.age
    print(self.fname, self.lname, result, self.section)

s1 = students("hossein", "yavari", 2001, "karshenasi")
s1.person()