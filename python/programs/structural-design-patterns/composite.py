from abc import ABC, abstractmethod

class FileStructure(ABC):
    """Interface"""
    @abstractmethod
    def get_size(self):
        """returns size of the component in mb"""

class File(FileStructure):
    
    def __init__(self, name, size):
        self._name = name
        self._size = size
    
    def get_size(self):
        return self._size
    
class Folder(FileStructure):
    
    def __init__(self, name, components):
        self._name = name
        self._components = components
        
    def get_size(self):
        total_size = 0
        for c in self._components:
            total_size += c.get_size()
        return total_size

if __name__ == "__main__":
    sprint_report = File("sprint_report.csv",5)
    print (sprint_report.get_size())
    
    milestone_report = File("milestone.pptx",150)
    print (milestone_report.get_size())

    progress = Folder("progress",[sprint_report,milestone_report])
    print (progress.get_size())