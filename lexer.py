import re


class Lexer:
    def __init__(self, input_code):
        self.input_code = input_code
        self.tokens = []
        self.token_spec = [
            ("NUMBER", r"\d+"),
            ("STRING", r"\".*?\""),
            ("KEYWORD", r"make_pizza|add_topping|bake|slice|deliver"),
            ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
            ("OPERATOR", r"[=(),]"),
            ("NEWLINE", r"\n"),
            ("SKIP", r"[ \t]+"),
        ]

    def tokenize(self):
        token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in self.token_spec)
        for match in re.finditer(token_regex, self.input_code):
            kind = match.lastgroup
            value = match.group()
            if kind == "SKIP":
                continue
            self.tokens.append((kind, value))
        return self.tokens
