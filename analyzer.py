import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives=set()
        self.negatives=set()
        with open(positives) as lines:
                for line in lines:
                    if line.startswith(';') == False:
                        self.positives.add(line.rstrip("\n"))
        with open(negatives) as lines:
                for line in lines:
                    if line.startswith(';') == False:
                        self.negatives.add(line.rstrip("\n"))
        
                    
        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        sum=0.0
        #print(self.positives)
        for i in tokens:
            if i.lower() in self.positives:
                sum += 1
            elif i.lower() in self.negatives:
                sum -= 1
            else:
                continue
        # TODO
        return sum
