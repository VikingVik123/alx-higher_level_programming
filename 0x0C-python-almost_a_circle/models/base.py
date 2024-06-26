#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.
    This class represents the blueprint for all other classes in project 0x0C*.

    Private Class Attribute:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        obj initialization
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """json to string conv func"""
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries: A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs: A list of inherited Base instances.
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.

        Args:
            json_string: A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    def __str__(self):
        """
        Returns string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def display(self):
        """
        Prints the Rectangle instance with '#' character considering x and y.
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to attributes.
        Args:
            *args: Non-keyworded arguments. Ignored if **kwargs is present.
            **kwargs: Keyworded arguments representing attribute-value pairs.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            dictionary: A dictionary representing attributes and their values.
        Returns:
            An instance of the class with attributes set based on the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)  # Creating a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            dummy = cls(1)  # Creating a dummy Square instance
        else:
            raise ValueError("Unsupported class type")

        dummy.update(**dictionary)  # Update dummy instance with dictionary
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a JSON file.

        Returns:
            A list of instances loaded from the JSON file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                data = cls.from_json_string(file.read())
                return [cls.create(**item) for item in data]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of objects and writes to a CSV file.

        Args:
            list_objs: A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes objects from a CSV file and returns a list of instances.

        Returns:
            A list of instances loaded from the CSV file.
        """
        filename = f"{cls.__name__}.csv"
        instances = []
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    instances.append(cls.create(id=int(row[0]), width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4])))
                elif cls.__name__ == 'Square':
                    instances.append(cls.create(id=int(row[0]), size=int(row[1]), x=int(row[2]), y=int(row[3])))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        # Set up the window
        window = turtle.Screen()
        window.title("Rectangles and Squares")

        # Create a turtle object
        pen = turtle.Turtle()

        # Draw rectangles
        pen.color("blue")
        pen.penup()
        for rect in list_rectangles:
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.forward(rect.width)
            pen.left(90)
            pen.forward(rect.height)
            pen.left(90)
            pen.penup()

        # Draw squares
        pen.color("red")
        pen.penup()
        for square in list_squares:
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.penup()

        # Close the window on click
        window.mainloop()