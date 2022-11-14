from datetime import datetime, timedelta
import random
from typing import Callable


class BoundedRandom(object):
    """
    Generates random values between 2 set values for items that can be expressed in numeric form.
    Generated values are within interval [n, m) by default.
    """
    # Using DI here as the random library is technically only pseudo-random so allows for better/different algorithms to be added if required.
    __generator_func: Callable[[float, float], float] = random.uniform

    def __init__(self, generator_func: Callable[[float, float], float] = None) -> None:
        """
        Generates random values between 2 set values for items that can be expressed in numeric form.

        Args:
            generator_func (Callable[[float,float], float], optional): A function that accepts a start and end number then returns a random number between the 2 bounds.
            Defaults to `random.uniform` if not provided. Defaults to None.
        """
        if generator_func:
            self.__generator_func = generator_func

    @classmethod
    def datetime(self, start: datetime, end: datetime) -> datetime:
        """
        Generates a random datetime between two dates.

        Args:
            start (datetime): Lower bound.
            end (datetime): Upper bound.

        Returns:
            datetime: A random datetime between start and end bounds.
        """
        # Get the time delta between the 2 bounds, calculate a new random delta between zero (start) and the delta (end) then add that to start.
        delta = end - start
        return start + timedelta(seconds=self.__generator_func(0, delta.total_seconds()))

    @classmethod
    def float(self, a: float, b: float) -> float:
        """
        Generates a random float between two values.

        Args:
            a (float): Lower bound.
            b (float): Upper bound.

        Returns:
            float: A random number between a and b.
        """
        return self.__generator_func(a, b)
