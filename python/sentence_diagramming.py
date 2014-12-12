from textblob import TextBlob

# From http://www.ling.upenn.edu/courses/Fall_2007/ling001/penn_treebank_pos.html
def name_from_tag(tag):
    tags = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW':	'Foreign word',
        'IN':	'Preposition or subordinating conjunction',
        'JJ':	'Adjective',
        'JJR':	'Adjective, comparative',
        'JJS':	'Adjective, superlative',
        'LS':	'List item marker',
        'MD':	'Modal',
        'NN':	'Noun, singular or mass',
        'NNS':	'Noun, plural',
        'NNP':	'Proper noun, singular',
        'NNPS':	'Proper noun, plural',
        'PDT':	'Predeterminer',
        'POS':	'Possessive ending',
        'PRP':	'Personal pronoun',
        'PRP$':	'Possessive pronoun',
        'RB':	'Adverb',
        'RBR':	'Adverb, comparative',
        'RBS':	'Adverb, superlative',
        'RP':	'Particle',
        'SYM':	'Symbol',
        'TO':	'to',
        'UH':	'Interjection',
        'VB':	'Verb, base form',
        'VBD':	'Verb, past tense',
        'VBG':	'Verb, gerund or present participle',
        'VBN':	'Verb, past participle',
        'VBP':	'Verb, non-3rd person singular present',
        'VBZ':	'Verb, 3rd person singular present',
        'WDT':	'Wh-determiner',
        'WP':	'Wh-pronoun',
        'WP$':	'Possessive wh-pronoun',
        'WRB':	'Wh-adverb',
    }
    
    return tags.get(tag, tag)

phrase = raw_input('Enter a sentence: ')
if not phrase:
    phrase = 'The red cars drove slowly down the street'
tb = TextBlob(phrase)
for word, tag in tb.tags:
    print "%10s: %s" % (word, name_from_tag(tag))
