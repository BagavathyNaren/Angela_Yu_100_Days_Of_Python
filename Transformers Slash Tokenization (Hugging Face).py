from transformers import AutoTokenizer
tokenizer= AutoTokenizer.from_pretrained("bert-base-cased")
sequence = "Transformer has the changed the domain of NLP"
tokens = tokenizer.tokenize(sequence)
print(tokens)



"""
Explanation:

You are using BERT’s WordPiece tokenizer (bert-base-cased) from Hugging Face.

WordPiece breaks unknown or uncommon words into subword tokens with ## prefixes.

"Transformer" is not in BERT’s vocab as a whole, so it is split into:

"Trans"

"##former"

"NLP" is also split as:

"NL"

"##P"

Common words (has, the, changed, domain, of) remain intact.

So the output is:

['Trans', '##former', 'has', 'the', 'changed', 'the', 'domain', 'of', 'NL', '##P']


"""