import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 似乎作者十分清楚怎么来编写一个扑克牌的类
    suits = 'spades diamonds clubs hearts'.split()  # 构建四个花色的列表，使用了split()方法，把一个字符串分割成一个字符串列表

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]  # 生成一个列表，包含52张扑克牌的元组,可以学到列表解析的编码结构

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """
spades_high 函数的具体实现是这样的：
首先，它找到了给定牌的点数（rank）在 FrenchDeck.ranks 列表中的索引（使用 index 方法），这个索引相当于牌的大小（如2, 3, 4等）。
然后，它乘以花色值（suit_values）的长度，这会确保不同花色的牌有足够的间距，以便在排序时区分开。
最后，它将计算出的值与给定牌花色（suit）对应的权重相加，这个权重是从 suit_values 字典中获取的。这样，牌的大小和花色都被考虑在内。
因此，spades_high 函数生成的值可以用来区分每张牌，并且可以作为 sorted 函数的 key 参数，帮助对扑克牌进行排序。
    :param card:
    :return:
    """
    rank_value = FrenchDeck.ranks.index(card.rank)  # 通过index方法来获取元素的索引
    return rank_value * len(suit_values) + suit_values[card.suit]  # 通过索引来获取元素的值


if __name__ == '__main__':
    card = FrenchDeck()
    for i in sorted(card, key=spades_high):
        print(i)


"""
我先来简单说一下我自己的感想吧，我先入为主地从这个具体项目来展示自己的收获
首先，我深深地被魔术方法震惊了，你能够看到在这里我们只是建立了一个表示扑克牌的类，但是实现了以下功能：
使用len即可获得自己创建的扑克牌的长度
使用getitem可以让我的类获取索引的功能
最后作者还很贴心地指出了一个点：在python中有一个内置库random，其中有个函数choice可以直接选择序列中的一个元素
"""
"""
下边总结作者的一些编码技巧：
1.使用namedtuple来构建一个类，这个类可以直接使用点号来访问元素，而不是使用索引
2.使用split()方法，把一个字符串分割成一个字符串列表
3.使用列表解析的编码结构
4.使用random库中的choice函数，可以直接选择序列中的一个元素
"""
"""
__getitem__:
1.索引
2.choice
3.切片
4.迭代（反向迭代）
"""
"""
in:
若容器没有包含__contains__方法，那么in会按顺序做一次迭代搜索,即查找变量是否在容器中，当然前提是该类可以迭代，而迭代由__getitem__方法提供
"""
"""
spades_high 函数的目的是为了给每张扑克牌分配一个权重，这个权重将用于在排序时确定牌的顺序。
在这个例子中，使用 sorted 函数对 FrenchDeck 类的实例（即一副扑克牌）进行排序时，key 参数设置为 spades_high 函数，
这意味着排序将根据每张牌的 spades_high 值进行。
"""