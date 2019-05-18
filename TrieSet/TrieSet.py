from TrieNode import TrieNode


class TrieSet(object):

    def __init__(self):
        self.root = None;

    def insert(self,word):

        if (self.root is False or self.root is None):
            self.root = TrieNode()
        current = self.root
        for w in word:
            test = current.children.get(w)
            if not test:
                current.children[w] = TrieNode(w)
                current.children[w].parent = current
            current = current.children[w]
        current.end = True

    def find(self,word):
        if(self.root is False or self.root is None):
            return False
        node = self.root
        output = []
        for w in word:
            try:
                if (node.children[w]):
                    node = node.children[w]
                else:
                    return output
            except:
                pass
        self.find_all_words(node,output)
        return output

    def find_all_words(self,node,arr):

        test = node.end
        if test:
            arr.insert(0,node.get_word())
        for child in node.children:
            if (child):
                self.find_all_words(node.children[child],arr)
            else:
                print("stuff")
    def reset(self):
        self.root = None

