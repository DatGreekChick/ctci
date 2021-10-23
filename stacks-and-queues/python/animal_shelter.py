# 3.6: Animal Shelter

from sq_exceptions import EmptyQueueException


class Animal:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, name: str, category: str):
        animal = Animal(name, category)

        if self.last:
            self.last.next = animal

        self.last = animal

        if not self.first:
            self.first = animal

    def remove(self):
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")

        animal = self.first
        self.first = self.first.next

        if not self.first:
            self.last = None

        return animal

    def peek(self):
        return self.first

    def is_empty(self):
        return self.first is None


class AnimalShelter:
    def __init__(self):
        self.animals = Queue()

    def enqueue(self, name: str, category: str):
        self.animals.add(name, category)

    def dequeue_any(self):
        animal = self.animals.remove()
        print(f"name: {animal.name} | category: {animal.category}")
        return animal

    def dequeue_helper(self, category: str):
        prev = self.animals.first
        curr = self.animals.first

        while curr:
            if curr.category == category:
                if curr == self.animals.first:
                    self.animals.first = curr.next
                else:
                    prev.next = curr.next

                print(f"name: {curr.name} | category: {curr.category}")
                return curr

            prev = curr
            curr = curr.next

    def dequeue_dog(self):
        return self.dequeue_helper("dog")

    def dequeue_cat(self):
        return self.dequeue_helper("cat")


shelter = AnimalShelter()
shelter.enqueue("Ab", "dog")
shelter.enqueue("Ac", "cat")
shelter.enqueue("Ba", "dog")
shelter.enqueue("Cd", "dog")
shelter.enqueue("Be", "cat")

shelter.dequeue_any()
shelter.dequeue_dog()
shelter.dequeue_cat()
shelter.dequeue_cat()
