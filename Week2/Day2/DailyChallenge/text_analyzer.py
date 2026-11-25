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

analyzer = TextAnalyzer("Python")
print(analyzer)
# output: TextAnalyzer object with 1 words
print(analyzer.__len__())
# output: 6