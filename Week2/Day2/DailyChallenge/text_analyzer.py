class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        if not self.text:
            raise Exception("Text cannot be empty")
    def __str__(self):
        count = self.text.split()
        return f"TextAnalyzer object with {len(count)} words"

analyzer = TextAnalyzer("Python is fun")
print(analyzer)