# assorted class utilities and tools
# Provides an inheritable display overload method that will
# show instances w their classes and name = value pair for each
# attribute


class AttrDisplay:
    """
    Provides an inheritable display overload method that will
    show instances w their classes and name = value pair for each
    attribute``
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s: %s' % (key, getattr(self, key)))
        return ', '. join(attrs)

    def __repr__(self):
        return '[%s,%s]' % (self.__class__.__name__, self.gatherAttrs())

#   Use cases


if __name__ == '__main__':

    class TopTest(AttrDisplay):

        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()

    print(X)
    print(Y)
