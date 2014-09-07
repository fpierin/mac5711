"""
btreeprint.py -- V.1.3, Feb 8 2007, by leonardo maffi.

This Python module contains the build_strtree(tree, space=3) function
that return a Strtree that can be used to print binary trees with ASCII art like this:

1


  1
+---+
2   3


      1
  +-------+
  2       3
+---+   +---+
4   5       6


Given a class defined like this node N (already defined in this module):
class N:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

The input cam be a nested structure of nodes:
>>> t1 =  N(1)
>>> print btreestr(t1)
1

>>> t2 =  N(1, N(2), N(3))
>>> print btreestr(t2) #doctest: +NORMALIZE_WHITESPACE
  1
+---+
2   3

>>> t3 =  N(1, N("leaf"), N(3))
>>> st = build_strtree(t3)
>>> print st #doctest: +NORMALIZE_WHITESPACE
    1
  +----+
leaf   3

Alternative representation, here are the "printing commands":
>>> st
<['+----+', 1, 2], [<['leaf', 0, 0]>, 2, 0], [<['3', 0, 0]>, 2, 7], ['1', 0, 4]>

With the right accessor function it can be used with arbitrary representations of
binary trees:
>>> t2 = [1, [2, [4], [5]], [3, None, [6]]]
>>> st2 = build_strtree(t2, accessor=list_accessor)
>>> print st2 #doctest: +NORMALIZE_WHITESPACE
      1
  +-------+
  2       3
+---+   +---+
4   5       6
>>> st2 #doctest: +NORMALIZE_WHITESPACE
<['+-------+', 1, 2], [<['+---+', 1, 0], [<['4', 0, 0]>, 2, 0], [<['5', 0, 0]>, 2, 4],
['2', 0, 2]>, 2, 0], [<['+---+', 1, 0], [<>, 2, 0], [<['6', 0, 0]>, 2, 4], ['3', 0, 2]>,
2, 8], ['1', 0, 6]>


The program uses a lazy printing algorithm. build_strtree() calls itself recursively
  to create a tree of "printing commands" listed inside Strtree() objects, that contain
  the textual representation of the given subtrees.
When you call the __str__() method of the Strtree, it computes the textual representation
  of the whole tree.
There is a single matrix of chars that become recursively written with all the strings
  contained into the tree structure of Strtree().
Note that the Strtree class has __slot__, if you want to subclass it, you can comment it out.
"""

# The following base 64-encoded block contains a PNG image that shows
# the meaning of the various variables used inside build_strtree()
_img = """\
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
BJRU5ErkJggg=="""
import binascii
assert binascii.crc32(_img) == 696728376
# decomment the following line to save and see the image
# file("btreeprint_img.png", "wb").write(_img.decode("base64"))


from array import array
import re

class Charmat(object):
    """Charmat(nrows, ncols): class that manages a 2D matrix of chars, implemented
    with array.array("c")
    If alllows printing, and pasting of string at desired positions.

    >>> c = Strtree()
    >>> c.add("hello", 0, 0)
    >>> c.add("how", 2, 3)
    >>> c.nrows, c.ncols, c.data
    (3, 6, [['hello', 0, 0], ['how', 2, 3]])
    >>> print c #doctest: +NORMALIZE_WHITESPACE
    hello
    <BLANKLINE>
       how

    >>> c2 = Strtree()
    >>> c2.add("hallo", 0, 0)
    >>> c2.add("hew", 2, 3)
    >>> c.add(c2, 1, 7)
    >>> c.nrows, c.ncols, c.data
    (4, 13, [['hello', 0, 0], ['how', 2, 3], [<['hallo', 0, 0], ['hew', 2, 3]>, 1, 7]])
    >>> print c #doctest: +NORMALIZE_WHITESPACE
    hello
           hallo
       how
              hew
    """
    def __init__(self, nrows, ncols):
        assert ncols > 0
        assert nrows > 0
        self.nrows = nrows
        self.ncols = ncols
        self.mat = array("c", " " * (nrows * ncols))

    def __str__(self):
        nr = self.nrows
        nc = self.ncols
        return "\n".join(self.mat[i:i+nc].tostring() for i in xrange(0, len(self.mat), nc))

    def paste(self, txt, row_coord, col_coord):
        """Charmat.paste(txt, row_coord, col_coord): to paste a string on the Charmap
        at the given row and column coordinate."""
        assert isinstance(txt, str)
        # This is slow, but it seems it's not an important part of code.
        for col, char in enumerate(txt):
            c = col_coord + col
            if row_coord >= 0 and row_coord < self.nrows and c >= 0 and c < self.ncols:
                self.mat[self.ncols * row_coord + c] = char


class Strtree(object):
    """Strtree(stalk=0): class used to represent the tree of "printing operations".
    Stalk is the column coordinate of the center of the horizonal +-----+  line,
    used to attach the supertree too."""
    # If you want you can comment this __slot__ out
    __slot__ = "nrows ncols data stalk".split()
    def __init__(self, stalk=0):
        # To simplify the rendering, the minimal dimension of a Strtree is 1x1
        self.nrows = 1
        self.ncols = 1
        self.data = []
        self.stalk = stalk

    def add(self, obj, row_coord, col_coord):
        """add(obj, row_coord, col_coord): to add a an object to the Strtree, in
        the desired location.
        Obj can be a self.__class__ (usually a Strtree) or any other object that
        becomes immediately converted to a string.
        This metod doesn't add the Strtree/string to character matrix, the
        [obj, row_coord, col_coord] is just added to the data list.
        """
        assert row_coord >= 0
        assert col_coord >= 0
        if isinstance(obj, self.__class__):
            # self.nrows = max(self.nrows, row_coord + obj.nrows)
            if row_coord + obj.nrows > self.nrows:
                self.nrows = row_coord + obj.nrows
            # self.ncols = max(self.ncols, col_coord + obj.ncols)
            if col_coord + obj.ncols > self.ncols:
                self.ncols = col_coord + obj.ncols
        else:
            obj = str(obj)
            # self.nrows = max(self.nrows, row_coord + 1)
            if row_coord + 1 > self.nrows:
                self.nrows = row_coord + 1
            # self.ncols = max(self.ncols, col_coord + len(obj))
            aux = col_coord + len(obj)
            if aux > self.ncols:
                self.ncols = aux
        self.data.append([obj, row_coord, col_coord])

    def __repr__(self): # mostly for debugging
        return "<" + repr(self.data)[1:-1] + ">"

    def _render(self, cmat, r=0, c=0):
        """Internal method. Given the char matrix to print on, and the coordinates of
        the start point, prints the current Strtree on the matrix, using recursion."""
        assert cmat.nrows >= self.nrows
        assert cmat.ncols >= self.ncols
        for obj, row_coord, col_coord in self.data:
            if isinstance(obj, self.__class__):
                obj._render(cmat, row_coord+r, col_coord+c)
            else:
                cmat.paste(obj, row_coord+r, col_coord+c)

    def __str__(self):
        # creates a char matrix, renders it, and return its conversion to a string
        cm = Charmat(self.nrows, self.ncols)
        self._render(cm)
        return str(cm)


class N:
    """N(data, left=None, right=None): class that represents a node of the binary tree.

    >>> N()
    Traceback (most recent call last):
      ...
    TypeError: __init__() takes at least 2 arguments (1 given)
    >>> N(1)
    (1)
    >>> N(1, None, None)
    (1)
    >>> N(1, N(2))
    (1 L(2) R*)
    >>> N(1, N(2, None, N(3)), N(4))
    (1 L(2 L* R(3)) R(4))
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        # creates a recursive representation of the tree
        if self.left is self.right is None:
            return "(%s)" % (self.data,)
        repr_left = "*" if self.left is None else repr(self.left)
        repr_right = "*" if self.right is None else repr(self.right)
        return "(%s L%s R%s)" % (self.data, repr_left, repr_right)


# 1x1 empty spacer useful to improve the printing representation of an empty
# node that has a real brother node
LITTLE = Strtree()


def node_accessor(node):
    """node_accessor(node): accessor function useful to build_strtree to access
    the attributes of an N() node."""
    return node.data, node.left, node.right


def list_accessor(node):
    """list_accessor(node): accessor function useful to build_strtree to access
    the elements of a list that contains the data, left_pointer, right_pointer
    that represent the node of a binary tree.
    The acceptable list configurations are like N(data, left=None, right=None):
      [data]
      [data, None]
      [data, None, None]
      [data, left_pointer]
      [data, None, right_pointer]
      [data, left_pointer, right_pointer]
    """
    data = node[0]
    len_node = len(node)
    tree_left = (node[1] if len_node>1 else None)
    tree_right = (node[2] if len_node>2 else None)
    return data, tree_left, tree_right


def build_strtree(tree, accessor=node_accessor, space=3):
    """build_strtree(tree, accessor=node_accessor, space=3): function that creates
    a nested structure of Strtree, from the given binary tree.
    accessor: function that takes a node of the tree, and return its
      data, tree_left, tree_right. Two possibile function are already defined:
      node_accessor() and list_accessor() and (). The first one is useful to access the
      attributes of N() nodes, the second one for binary trees represented ad nested lists.
      If necessary you can use your own accessor function.
    space: the minimal horizonal space beteen two children."""
    if tree is None:
        return LITTLE # 1x1 blank char matrix

    data, tree_left, tree_right = accessor(tree)
    data = str(data)
    data_width = len(data)

    if tree_left is tree_right is None:
        # then it's a leaf
        st = Strtree(stalk=data_width // 2)
        # fill the leaf with the current data, at the starting position, it's just a label.
        st.add(data, 0, 0)
    else:
        left_subtree = build_strtree(tree_left, space=space, accessor=accessor)
        width_left_subtree = left_subtree.ncols

        right_subtree = build_strtree(tree_right, space=space, accessor=accessor)
        width_right_subtree = right_subtree.ncols

        # height of the current whole string tree
        # the 0 row is for the data, the 1 row is for the +---------+
        height = 2 + max(left_subtree.nrows, right_subtree.nrows)

        # Starting column coordinate of the +---------+ line
        start_line = left_subtree.stalk
        # len of the +---------+ line
        line_width = max(data_width+2, (left_subtree.ncols - left_subtree.stalk) + space + right_subtree.stalk)
        # End column coordinate of the +---------+ line
        stop_line = start_line + line_width

        # width of the current whole string tree
        width = left_subtree.stalk + line_width + 1 + (right_subtree.ncols - right_subtree.stalk)
        st = Strtree()

        # Creates the +---------+ line and adds it to the empty Strtree, at row 1
        line = "+%s+" % ("-" * (stop_line - start_line - 1))
        st.add(line, 1, start_line)

        # add the left subtree to the current Strtree. The upper-left position is
        # third row and first column.
        st.add(left_subtree, 2, 0)
        # add the right subtree to the current Strtree
        st.add(right_subtree, 2, width - width_right_subtree - 1)

        # define the column coordinate of the stalk of the current Strtree
        # as the median point of the +---------+ line
        st.stalk = (start_line + stop_line) // 2
        # finally add the data label on the top, centered around the stalk
        st.add(data, 0, st.stalk - (data_width // 2))

    return st


def btreestr(bintree, space=3, accessor=node_accessor):
    """btreestr(bintree, space=3, accessor=node_accessor): function that return
    the string representation of th given binary tree.
    accessor: function that takes a node of the tree, and return its
      data, tree_left, tree_right. Two possibile function are already defined:
      node_accessor() and list_accessor() and (). The first one is useful to access the
      attributes of N() nodes, the second one for binary trees represented ad nested lists.
      If necessary you can use your own accessor function.
    space: the minimal horizonal space beteen two children.
    """
    return str(build_strtree(bintree, accessor=accessor, space=space))


def unicode_html_converter(txt_tree):
    r"""unicode_html_converter(txt_tree): given a textual matrix containing a
    rendered binary tree, converts the lines in HTML unicode elements with
    a nicer look.

    >>> txt_tree = '  1\n+---+\n2   3'
    >>> print txt_tree
      1
    +---+
    2   3
    >>> print unicode_html_converter(txt_tree)
    <html><pre>
      1
    &#9484;&#9472;&#9524;&#9472;&#9488;
    2   3
    </pre></html>
    """
    # &#9472;  &#9524;  &#9484;  &#9488;
    #             |        _       _
    #   ---      ---      |         |
    def line_repl(match_obj):
        line = match_obj.group()
        start_line, stop_line = match_obj.span()
        line_stalk = (start_line + stop_line) // 2 - start_line - 1
        if (stop_line - start_line) & 1:
            line_stalk += 1
        line_core_sx = line[1:line_stalk].replace("-", "&#9472;")
        line_core_dx = line[line_stalk+1:-1].replace("-", "&#9472;")
        return "&#9484;%s&#9524;%s&#9488;" % (line_core_sx, line_core_dx)

    line_find = re.compile(r"\+[-]+\+")
    rows = txt_tree.splitlines()
    for nrow, row in enumerate(rows):
        if nrow & 1:
            rows[nrow] = line_find.sub(line_repl, row)
    rows = ["<html><pre>"] + rows + ["</pre></html>"]
    return "\n".join(rows)


try: # Use Psyco if avalable
    import psyco
    psyco.full()
except ImportError:
    pass

__all__ = ["build_strtree", "list_accessor", "node_accessor", "N", "btreestr",
           "unicode_html_converter"]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print "Doctests finished.\n"

    if 1:
        print "Basic tests of N() node trees representation:"
        t1 = N(1)
        t2 = N(1, N(2), N(3))
        t3 = N(1, None, N(2))
        t4 = N(1, N(2), None)
        t5 = N(1, N(2, N(4), N(5)), N(3, None, N(6)))
        t6 = N("abcdef", N("hello"), N("ugly"))
        t7 = N("hello", t5, t5)
        t8 = N("abcdefg", N(1), N(2))
        t9 = N(1, N(2), N("abcdefghilmnop"))
        t10 = N("0123456789", t9, t8)
        t11 = N("hellllllllo", t7, t7)
        t12 = N(1, N(" "), N(""))
        t13 = N("abcdefghilmnopqrs"*4, N("abcdefghilmnopqrs"*2), N(""))

        for t in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13]:
            tree_txt = str(build_strtree(t))
            print tree_txt
            print "\n"
            print unicode_html_converter(tree_txt)
            print "\n\n"


    def fulltree(n):
        "Return the full binary tree of order n, represented with N() nodes."
        return N("X", fulltree(n-1), fulltree(n-1)) if n else None

    def fulltreel(n):
        "Return the full binary tree of order n, represented with nested lists."
        return ["X", fulltreel(n-1), fulltreel(n-1)] if n else None

    if 1:
        print "Mixed tests with trees represented with N() nodes:"
        n = 7
        print "Complete binary tree depth:", n
        tree_txt = str(build_strtree(fulltree(n), space=1))
        print tree_txt
        print "\n"
        print unicode_html_converter(tree_txt)
        print "\n\n"

        n = 15
        tree = fulltree(n)
        from time import clock
        t = clock()
        build_strtree(tree, space=1)
        print "Complete binary tree depth:", n, "rendering time:", round(clock()-t,2), "s\n"


    if 1:
        print "Test with random tree represented with N() nodes:"
        from random import random, choice, randint
        from string import lowercase

        def rndtree():
            if random() < 0.55:
                return None
            else:
                rnd_data = "".join(choice(lowercase) for _ in xrange(randint(1, 20)))
                return N(rnd_data, rndtree(), rndtree())

        for _ in xrange(10):
            tree_txt = str(build_strtree(rndtree()))
            print tree_txt
            print "\n"
            print unicode_html_converter(tree_txt)
            print "\n\n"
        print


    if 1:
        print "Basic tests of nested list trees representation:"
        t1 = [1]
        t2 = [1, [2], [3]]
        t3 = [1, None, [2]]
        t4 = [1, [2], None]
        t5 = [1, [2, [4], [5]], [3, None, [6]]]
        t6 = ["abcdef", ["hello"], ["ugly"]]
        t7 = ["hello", t5, t5]
        t8 = ["abcdefg", [1], [2]]
        t9 = [1, [2], ["abcdefghilmnop"]]
        t10 = ["0123456789", t9, t8]
        t11 = ["hellllllllo", t7, t7]
        t12 = [1, [" "], [""]]
        t13 = ["abcdefghilmnopqrs"*4, ["abcdefghilmnopqrs"*2], [""]]

        for t in [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13]:
            print build_strtree(t, accessor=list_accessor), "\n\n"

    if 1:
        print "build_strtree demo with nested lists:"
        n = 7
        print "Complete binary tree depth:", n
        print build_strtree(fulltreel(n), space=1, accessor=list_accessor), "\n\n"


    if 1:
        print "Speed build_strtree demo with nested lists:"
        n = 15
        tree = fulltreel(n)
        from time import clock
        t = clock()
        build_strtree(tree, space=1, accessor=list_accessor)
        print "Complete binary tree depth:", n, "rendering time:", round(clock()-t,2), "s"
        print


    if 0:
        print "Test with random tree represented with nested lists:"
        from random import random, choice, randint
        from string import lowercase

        def rndtree():
            if random() < 0.55:
                return None
            else:
                rnd_data = "".join(choice(lowercase) for _ in xrange(randint(1, 20)))
                return [rnd_data, rndtree(), rndtree()]

        for _ in xrange(10):
            print build_strtree(rndtree(), accessor=list_accessor), "\n\n"


    if 1:
        print "Other kinds of binary trees too can be printed using the right accessor:"
        def pair_accessor(node):
            if isinstance(node, (list, tuple)):
                return "|", node[0], (node[1] if len(node)>1 else None)
            else:
                return node, None, None

        dendrogram = ((('hello', 'b'), 'c'), (('', 1233456), ('f', 'g')))
        print build_strtree(dendrogram, accessor=pair_accessor)
        print

    print "Demos and tests finished."