from functools import total_ordering


@total_ordering

class Opening:
    def __init__(self, name, freq, score, depth, weightedScore):
        self.name = name
        self.freq = freq
        self.score = score
        self.depth = depth
        self.weightedScore = weightedScore

    def __eq__(self, other):
        return self.weightedScore == other.weightedScore
    
    def __gt__(self, other):
        return self.weightedScore > other.weightedScore

    def __str__(self):
        return self.name
        