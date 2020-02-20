# PizzaTokenizer

The Semantic Tokenizer "Pizza Tokenizer" by S. Korani.

## Usage:

**Note 1**: We are constantly developing new features, and it may cause incompatibility with older versions.  
**Note 2**: This tokenizer needs normalized data. For testing this module, you need to remove punctuations and extra whitespaces from your text.

To use the tokenizer copy `tokenizer` directory to your project path or add
its path to python's module search path. Then

    import tokenizer

Initialize tokenizer by instantiating `Tokenizer` class:

    tokenizer_object = tokenizer.Tokenizer()

Now, you could tokenize ***normalized*** text with the method below:

    tokenizer_object("your normalized string")

This function returns a list of Semantic Tokens.
