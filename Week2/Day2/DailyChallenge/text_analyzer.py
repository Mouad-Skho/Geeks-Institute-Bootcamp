class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        if not self.text:
            raise Exception("Text cannot be empty")
    def __str__(self):
        count = self.text.split()
        return f"TextAnalyzer object with {len(count)} words"
    def __len__(self):
        return len("".join(self.text.split()))
    def word_count(self):
        return len(self.text.split())
    def count_word(self,word):
        if not word:
            raise Exception("Word cannot be empty")
        return self.text.lower().count(word.lower())



analyzer = TextAnalyzer("Python is fun and Python is powerful")
print(analyzer)
print(analyzer.__len__())
print(analyzer.word_count())

print(analyzer.count_word("Python"))
# output : 2