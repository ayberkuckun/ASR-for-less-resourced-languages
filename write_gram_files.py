from collections import defaultdict
import nltk
from tqdm import tqdm


def frequency_dicts(file):
    """Creates frequency dictionaries and returns them. Dictionaries set up as
    {uni/(bi/tri/quadgram) : probability}."""

    quadgram_freqs = defaultdict(int)  # tracks hard count
    trigram_freqs = defaultdict(int)  # tracks hard count
    bigram_freqs = defaultdict(int)  # tracks hard count
    word_freqs = defaultdict(int)  # tracks hard count
    tokenizer = nltk.RegexpTokenizer(r'[A-Za-z]+[\S]?[A-Za-z0-9]+|[A-Za-z]+|\d+[a-z]+|\d+.?\d+|\d+')

    with open(file, "r", encoding="utf8") as f:
        for no, line in tqdm(enumerate(f)):
            if no == 10000000:
                break

            text = line.rstrip().lower()
            tokens = tokenizer.tokenize(text)
            for index in range(len(tokens)):
                # word_freqs[tokens[index]] += 1
                # if index < len(tokens) - 1:
                #     bigram_freqs[(tokens[index], tokens[index + 1])] += 1
                if index < len(tokens) - 2:
                    trigram_freqs[(tokens[index], tokens[index + 1], tokens[index + 2])] += 1
                if index < len(tokens) - 3:
                    quadgram_freqs[(tokens[index], tokens[index + 1], tokens[index + 2], tokens[index + 3])] += 1

            # for index in range(0, len(tokens) - 3):  # creates quadgram frequency dictionary
            #     quadgram_freqs[(tokens[index], tokens[index + 1], tokens[index + 2], tokens[index + 3])] += 1
            # for index in range(0, len(tokens) - 2):  # creates trigram frequency dictionary
            #     trigram_freqs[(tokens[index], tokens[index + 1], tokens[index + 2])] += 1
            # for index in range(0, len(tokens) - 1):  # creates bigram frequency dictionary
            #     bigram_freqs[(tokens[index], tokens[index + 1])] += 1
            # for token in tokens:  # creates unigram frequency dictionary
            #     word_freqs[token] += 1

    # word_freqs = {k: v for k, v in word_freqs.items() if v > 300}
    # bigram_freqs = {k: v for k, v in bigram_freqs.items() if v > 200}
    trigram_freqs = {k: v for k, v in trigram_freqs.items() if v > 100}
    quadgram_freqs = {k: v for k, v in quadgram_freqs.items() if v > 50}

    # word_freqs = dict(sorted(word_freqs.items(), key=lambda x: x[1], reverse=True))
    # bigram_freqs = dict(sorted(bigram_freqs.items(), key=lambda x: x[1], reverse=True))
    trigram_freqs = dict(sorted(trigram_freqs.items(), key=lambda x: x[1], reverse=True))
    quadgram_freqs = dict(sorted(quadgram_freqs.items(), key=lambda x: x[1], reverse=True))

    # with open("final_unigrams.txt", "w", encoding="utf8") as u:
    #     for k in word_freqs.keys():
    #         u.write(f"{k} {word_freqs[k]}\n")

    # with open("final_bigrams.txt", "w", encoding="utf8") as b:
    #     for k in bigram_freqs.keys():
    #         b.write(f"{k[0]} {k[1]} {bigram_freqs[k]}\n")

    with open("final_trigrams.txt", "w", encoding="utf8") as t:
        for k in trigram_freqs.keys():
            t.write(f"{k[0]} {k[1]} {k[2]} {trigram_freqs[k]}\n")

    with open("final_quadgrams.txt", "w", encoding="utf8") as q:
        for k in quadgram_freqs.keys():
            q.write(f"{k[0]} {k[1]} {k[2]} {k[3]} {quadgram_freqs[k]}\n")

    return word_freqs, bigram_freqs, trigram_freqs, quadgram_freqs


uni, bi, tri, quad = frequency_dicts("hungarian.txt")  # Oscar Dataset
