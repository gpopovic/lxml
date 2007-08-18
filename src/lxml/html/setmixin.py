class SetMixin(object):

    """
    Mix-in for sets.  You must define __iter__, add, remove
    """

    def __len__(self):
        return len(list(self))

    def __contains__(self, item):
        for has_item in self:
            if item == has_item:
                return True
        return False

    def issubset(self, other):
        for item in other:
            if item not in self:
                return False
        return True

    __le__ = issubset

    def issuperset(self, other):
        for item in self:
            if item not in other:
                return False
        return True

    __ge__ = issuperset

    def union(self, other):
        return self | other

    def __or__(self, other):
        new = self.copy()
        new |= other
        return new
    
    def intersection(self, other):
        return self & other

    def __and__(self, other):
        new = self.copy()
        new &= other
        return new

    def difference(self, other):
        return self - other

    def __sub__(self, other):
        new = self.copy()
        new -= other
        return new

    def symmetric_difference(self, other):
        return self ^ other

    def __xor__(self, other):
        new = self.copy()
        new ^= other
        return new

    def copy(self):
        return set(self)

    def update(self, other):
        for item in other:
            self.add(item)

    __ior__ = update

    def intersection_update(self, other):
        for item in self:
            if item not in other:
                self.remove(item)

    __iand__ = intersection_update

    def difference_update(self, other):
        for item in other:
            if item in self:
                self.remove(item)

    __isub__ = difference_update

    def symmetric_difference_update(self, other):
        for item in other:
            if item in self:
                self.remove(item)
            else:
                self.add(item)

    __ixor__ = symmetric_difference_update

    def discard(self, item):
        try:
            self.remove(item)
        except KeyError:
            pass

    def clear(self):
        for item in list(self):
            self.remove(item)
