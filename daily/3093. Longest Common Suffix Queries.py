class TrieNode:
    __slots__ = ('children', 'best_len', 'best_idx')
    def __init__(self):
        self.children = {}
        self.best_len = float('inf')
        self.best_idx = -1

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()
        for idx, w in enumerate(wordsContainer):
            rev = w[::-1]
            node = root
            if len(w) < node.best_len or (len(w) == node.best_len and idx < node.best_idx):
                node.best_len = len(w)
                node.best_idx = idx
            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(w) < node.best_len or (len(w) == node.best_len and idx < node.best_idx):
                    node.best_len = len(w)
                    node.best_idx = idx

        ans = []
        for q in wordsQuery:
            rev = q[::-1]
            node = root
            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]
            ans.append(node.best_idx)
        return ans