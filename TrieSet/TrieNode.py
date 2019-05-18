class TrieNode(object):

    def __init__(self,*args):

        if(args):
            self.key = args[0]
        self.parent = None
        self.children = {}
        self.end = False

    def get_word(self):

        output = []
        node = self        
        while (node):
            try:
                output.insert(0,node.key)
            except:
                pass
            node = node.parent
        out = "".join(output)
        return out
