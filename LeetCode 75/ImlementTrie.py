class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        node = self.root
        for i,c in enumerate(word):
            if c not in node.children:
                prefix = word[0:i+1]
                isEnd = 1 if i==len(word)-1 else 0
                node.children[c]=TrieNode(text=prefix, isEnd=isEnd)
            
            node=node.children[c]
        node.isEnd=1
     

    def search(self, word: str) -> bool:
        node = self.root
        i=0
        while i<len(word):
            if word[i] not in node.children:
                print('got here')
                return False
                          
            
            node= node.children[word[i]]
            i+=1
        if node.isEnd:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        i=0
        while i<len(prefix):
            if prefix[i] not in node.children:
                return False
          
            node= node.children[prefix[i]]
            i+=1
        return True


class TrieNode:
    def __init__(self, text='', isEnd=0):
        self.text = text
        self.children = dict()
        self.isEnd = isEnd


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
Console
