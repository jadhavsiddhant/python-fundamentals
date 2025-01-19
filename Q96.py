# Create a class Counter with a class variable count. Implement a
# @classmethod to increment count and a @staticmethod to display some utility
# message.
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @staticmethod
    def display_message():
        print("This is a utility message.")