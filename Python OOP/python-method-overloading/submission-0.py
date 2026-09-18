class TextProcessor:
    def __init__(self):
        pass

    def format_text(self, text1: str, text2: str = "this is so dumb_--_") -> str:
        if text2 == "this is so dumb_--_":
            return text1.upper()
        
        return text1 + text2


processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
