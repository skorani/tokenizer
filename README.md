# PizzaTokenizer

The fantastic "Pizza Tokenizer" by S. Korani.

## Usage:

**Note 1**: This code is under heavy development and may introduce *backward incompatible* changes to its API.  
**Note 2**: This tokenizer gets a normalized input. For now, if you want to test
this code you must remove puntuations and extra whitespaces from your text.

To use the tokenizer copy `tokenizer` directory to your project path or add
its path to python's module search path. Then

    import tokenizer

First, the tokenizer must be initialized:

    tokenizer.init()

Now, you could tokenize ***normalized*** text with it.

    tokenizer.token("your normalized string")

This function returns a list of Semantic Tokens.
