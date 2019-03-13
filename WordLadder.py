class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord,1))
        while bfs:
            word,length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i] + c + word[i+1:]
                    if newword in wordset:
                        bfs.append((newword,length+1))
                        wordset.remove(newword)
        return 0
