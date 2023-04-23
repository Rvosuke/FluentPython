"""
我们在这个类中只是为了操作特殊方法，一些问题做了一些简化处理
"""
import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        当你把这个特殊方法注释掉你就知道发生什么了，这个方法是用来返回一个对象的字符串表示，这个字符串表示是给开发者看的，而不是给用户看的
        也就是说在交互式控制台和调试的时候，这个方法会被调用，如果不定义，直接使用print，那么会打印出对象的内存地址
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        """Return the magnitude of the vector."""
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """在这里仿佛实现了+的重载，作为中缀运算符，他们会在运算后创建一个新的对象"""
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """仿佛实现了*的重载"""
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print(v1 * 3)
    print(abs(v1))
    print(bool(v1))