# traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

import abc

class Container:
    def __init__(self, container_name,container_image):
        self.container_name = container_name
        self.container_image = container_image

    def __str__(self):
        return f"name:{self.container_name},image:{self.container_image}"

class ContainerIterator:
    def __init__(self, containers):
        self.position = 0
        self.containers = containers

    def has_next(self):
        return False if self.position >= len(self.containers) else True

    def next(self):
        container = self.containers[self.position]
        self.position += 1
        return container

    def remove(self):
        return self.containers.pop()

class Pod:
    def __init__(self,name):
        self.name = name
        self.containers = []

    def add(self, pod):
        self.containers.append(pod)

    def iterator(self):
        return ContainerIterator(self.containers)

if __name__  == '__main__':

    c1 = Container("nginx","nginx:latest")
    c2 = Container("fluentbit","fluentbit:latest")

    pod = Pod("nginx-pod")
    pod.add(c1)
    pod.add(c2)

    print("\nDisplaying all containers in the pod:",pod.name,end="\n")
    iterator = pod.iterator()

    while iterator.has_next():
        container = iterator.next()
        print(container)

    print("\nRemoving last container returned\n")
    iterator.remove()

    print("Displaying all containers in the pod:", pod.name,end="\n")
    iterator = pod.iterator()
    while iterator.has_next():
        container = iterator.next()
        print(container)
