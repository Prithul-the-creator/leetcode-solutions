class WordDictionary:

    def __init__(self):
        self.words = set()
        

    def addWord(self, word: str) -> None:
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        found = False
        count = 0
        indices = []
        for i in range(len(word)):
            if word[i] == ".":
                count += 1
                indices.append(i)
        
        if count == 0:
            return word in self.words
        elif count == 1:
            for char in "abcdefghijklmnopqrstuvwxyz":
                completed_word = word[:indices[0]] + char + word[indices[0] + 1:]
                if completed_word in self.words:
                    return True
            return False
        
        else:

            for i in "abcdefghijklmnopqrstuvwxyz":
                for j in "abcdefghijklmnopqrstuvwxyz":
                    completed_word = word[:indices[0]] + i + word[indices[0] + 1: indices[1]] + j + word[indices[1] + 1:]

                    if completed_word in self.words:
                        return True
            return False







        
        
            

        

