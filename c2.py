class Udacian:
    def __init__(self, name, city,enrollment,nanodegree,status):
      self.name = name
      self.city = city
      self.enrollment = enrollment
      self.nanodegree = nanodegree
      self.status = status

    def print_udacian(self):
     print(self.name+" "+self.city+" "+self.nanodegree)

u = Udacian("elaaf","jeddah","enrollment","full stack","s")
u.print_udacian()
