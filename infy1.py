# class Emp:
#     __counter = 100
#     def __init__(self,name):
#         Emp.__counter+=1
#     @staticmethod
#     def get():
#         return Emp.__counter

# emp1 = Emp('sid')
# emp1 = Emp('siddd')
# emp1 = Emp('sidd')
# print(Emp.get()-100)
class team:
    con = 0
    def __init__(self):
        self.no_of_players = 11
        team.con += 1
    @staticmethod
    def get():
        print(team.con)
cri = team()
print(id(cri))
foot = team()
print(id(foot))
hock = foot
print(id(hock))
foot = cri
print(id(foot))
foot = team()
print(id(foot))
cri = hock
print(id(cri))
team.get()