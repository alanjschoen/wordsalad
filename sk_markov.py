import re
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

# Set length of n-grams
NG=3

with open('text_samples/obama.txt', 'r') as f:
    text = f.read()[57:].decode('UTF-8').replace('\n', ' ')
    
#text = re.sub(r'","|",|"', ',', re.sub(r'(?:(\d+?),)',r'\1',text)) # get rid of the commas in large numbers

# find sentence beginnings
def get_beginning(ng, text):
    varpat = r'\s+\w+'*(NG-1)
    beginnings = Counter(re.findall(r'(?:\n|\.\s+)([A-Z]\w*'+ varpat +')\s', text))
    (beg, ct) = zip(*[(b, c) for b,c in beginnings.iteritems() if c > 1])
    beginning = np.random.choice(a=beg, p = np.array(ct).astype(float) / np.sum(ct))
    
    return beginning

# Vectorize the corpus
def vectorize(text, n):
    # Handle ends of sentences 
    text = re.sub('([a-zA-Z]+)([\.\?])', r'\1 \2', text)
    
    # Vectorize it. Don't citicize it.
    tf_vec = CountVectorizer(input=u'content', ngram_range=(n,n), tokenizer=lambda x: x.split(), lowercase=False)
    tf_matrix = tf_vec.fit_transform([text])
    tf_vocab = tf_vec.get_feature_names()
    
    # Format it
    vocab_counts = zip(tf_vocab, tf_matrix.toarray()[0,:])
    return vocab_counts



# Given a tuple, find the nuxt word
def get_next_word(gram, vocab_counts3):
    options = [(t3.split()[NG], c3)  for  t3, c3 in vocab_counts3 if ' '.join(t3.split()[:-1]) == gram]
    next_words, counts = zip(*options)
    return np.random.choice(a=next_words, p = np.array(counts).astype(float) / np.sum(counts))
    
# Check if a sentence is finished
def is_finished(sent):
    return sent[-2:] in [' .', ' ?']
    
# Mke a sentence, given a beginning
def make_sentence(beginning, vocab_counts3, ng=2):
    sent = beginning
    while len(sent) < 140:
        cur_gram = ' '.join(sent.split()[-ng:])#.lower()
        sent += ' ' + get_next_word(cur_gram, vocab_counts3)
        
        if is_finished(sent) and len(sent) > 80:
            return sent
        
    return sent

beginning = get_beginning(NG, text)
# vocab_counts2 = vectorize(text, NG)
# vocab_counts2 = [(t,c) for (t,c) in vocab_counts2 if c>2]
vocab_counts3 = vectorize(text, NG+1)
sentence = make_sentence(beginning, vocab_counts3, NG)


# Get one that's the right length
def format_sentence(sent):
    return sent.replace(' .', '.').replace(' ?', '?')

while len(format_sentence(sentence)) > 139:
    sentence = make_sentence(beginning, vocab_counts3, NG)
    
print format_sentence(sentence)