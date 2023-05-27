class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        original_words = [''] * len(words)

        for word in words: 
            position_end = len(word) - 1
            while word[position_end].isdigit():
                position_end -= 1
            position = int(word[position_end+1:]) - 1
            original_words[position] = word[:position_end+1]

        original_sentence = ' '.join(original_words)
        return original_sentence

s = "is2 sentence4 This1 a3"
print(Solution().sortSentence(s))