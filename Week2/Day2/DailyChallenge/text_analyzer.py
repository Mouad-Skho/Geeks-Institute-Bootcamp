class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        if not self.text:
            raise Exception("Text cannot be empty")
analyzer = TextAnalyzer("")
