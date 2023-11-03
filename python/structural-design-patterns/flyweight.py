from enum import Enum
from abc import abstractmethod, ABC

class Group(ABC):
    @abstractmethod
    def setTeam(self, team):
        pass

    @abstractmethod
    def access(self, content):
        pass


class Role(Enum):
    READ = 1
    WRITE = 2
    ADMIN = 3


class DevOps(Group):
    roleType = Role.ADMIN
    team = None

    def setTeam(self, team):
        self.team = team

    def access(self, content):
        print(f"Accessing {content} as as part of the group: {self.__class__.__name__} from team: {self.team} with role type: {self.roleType}")


class Manager(Group):
    roleType = Role.READ
    team = None

    def setTeam(self, team):
        self.team = team

    def access(self, content):
        print(f"Accessing {content} as part of the group: {self.__class__.__name__} from team: {self.team} with role type: {self.roleType}")


class Dev(Group):
    roleType = Role.WRITE
    team = None

    def setTeam(self, team):
        self.team = team

    def access(self, content):
        print(f"Accessing {content} as as part of the group: {self.__class__.__name__} from team: {self.team} with role type: {self.roleType}")
        
class GroupFactory:
    groups = {}

    @staticmethod
    def getDevOpsGroup(team):
        key = team + "-ADMIN"
        if key not in GroupFactory.groups:
            group = DevOps()
            group.setTeam(team)
            GroupFactory.groups[key] = group
        return GroupFactory.groups[key]

    @staticmethod
    def getManagerGroup(team):
        key = team + "-READ"
        if key not in GroupFactory.groups:
            group = Manager()
            group.setTeam(team)
            GroupFactory.groups[key] = group
        return GroupFactory.groups[key]


    @staticmethod
    def getDevGroup(team):
        key = team + "-WRITE"
        if key not in GroupFactory.groups:
            group = Dev()
            group.setTeam(team)
            GroupFactory.groups[key] = group
        return GroupFactory.groups[key]

if __name__ == "__main__":
        group1 = GroupFactory.getDevOpsGroup("Frontend")
        group1.access("Jenkins")
        group2 = GroupFactory.getDevOpsGroup("Backend")
        group2.access("Jenkins")
        group3 = GroupFactory.getDevGroup("Mobile")
        group3.access("Jenkins")
        group4 = GroupFactory.getManagerGroup("Platform")
        group4.access("Jenkins")
        group5 = GroupFactory.getDevGroup("Mobile")
        group5.access("BitBucket")
        print(group1 == group2)
        print(group3.__hash__(),group5.__hash__())
        print (group1.__hash__(),group2.__hash__(),group4.__hash__())