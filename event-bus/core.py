
from enum import Enum


class EventBus:

    def __init__(self, events: Enum):
        self.__subscribers = dict()
        self.__events = events

    @property
    def events(self):
        return self.__events

    def subscribe(self, event, callback):
        if event not in self.__subscribers:
            self.__subscribers[event] = []
        self.__subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.__subscribers:
            self.__subscribers[event].remove(callback)

    def emit(self, event, data=None):
        if event in self.__subscribers:
            for callback in self.__subscribers[event]:
                callback(data)
