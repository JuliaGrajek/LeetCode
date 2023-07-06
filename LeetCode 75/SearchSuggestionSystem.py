class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        class TrieNode():
            def __init__(self, text='', isEnd=0):
                self.text=text
                self.isEnd=isEnd
                self.children = dict()

        class Trie():
            def __init__(self):
                self.root=TrieNode()
        
            def insert(self, word: str) -> None:
                node = self.root
                for i,c in enumerate(word):
                    if c not in node.children:
                        prefix = word[0:i+1]
                        isEnd = 1 if i==len(word)-1 else 0
                        node.children[c]=TrieNode(text=prefix, isEnd=isEnd)
                    node=node.children[c]
                node.isEnd=1

            def endOfPrefix(self, prefix: str) -> TrieNode:
                node = self.root
                i=0
                while i<len(prefix):
                    if prefix[i] not in node.children:
                        return None          
                    node= node.children[prefix[i]]
                    i+=1
                return node

            def getAllWordSuggestion(self, node, lst, visited)->List[str]: 
                if not node:
                    return None         
                if node.isEnd:                                 
                    lst.append(node.text)
                while node.children:
                    if node not in visited:
                        visited.append(node)                                
                        for k, v in node.children.items():
                            self.getAllWordSuggestion(v, lst, visited.copy())
                    else:
                        break
                return lst
            
            def getThreeWordSuggestions(self, lst) -> List[str]:
           
                if not lst:
                    return None
                else:
                    lst.sort()
                    return lst[0:3]

        
        #populate trie
        trie = Trie()
        for p in products:
            
            trie.insert(p)
        

        #find words with given prefix and return first three in lexicographical order
        res : List[List[str]]=[]
        tmp : List[str]=[]
    

        # for i in range(len(searchWord)):
        for i in range(1,len(searchWord)+1):
            c = searchWord[0:i]
            node = trie.endOfPrefix(c) 
            tmp = trie.getAllWordSuggestion(node, [],[])
            tmp = trie.getThreeWordSuggestions(tmp)
            res.append(tmp)
        return res
