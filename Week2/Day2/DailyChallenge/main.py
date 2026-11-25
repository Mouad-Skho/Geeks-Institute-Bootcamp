from text_analyzer import TextAnalyzer

text = "Python is fun and Python is powerful language"

analyzer = TextAnalyzer(text)

print(analyzer)
print(len(analyzer))
print(analyzer.word_count())
print(analyzer.count_word("Python"))

# Step 8: Test Exceptions
test = TextAnalyzer("")
print(test)
print(len(test))
print(test.word_count())
print(test.count_word("Python"))