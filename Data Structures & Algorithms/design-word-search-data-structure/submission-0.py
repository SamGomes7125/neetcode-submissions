class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        index = 0
        def dfs(index, node):
            if index == len(word):
                return node.isEnd
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True

                return False
            else:
                if word[index] not in node.children:
                    return False

                return dfs(index + 1, node.children[word[index]])

            return dfs(index + 1, node.children[word[index]])
        return dfs(0, self.root)
        
