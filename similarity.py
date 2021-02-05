# Ezra Zinberg

# text similarity

def similarity(t1, t2):

  # define a few stopwords
  stops = ["the", "it", "i", "you", "he", "she", "him", "her",
           "a", "in", "or", "and", "", " "]

  # UNIGRAMS

  # preprocess t1
  t1 = t1.lower()
  no_punc1 = t1.replace('.', '').replace('\n', '')
  words1 = no_punc1.split(' ')
  # remove stopwords
  words1 = [word for word in words1 if word not in stops]

  # contains unigram counts for words
  unigrams1 = {}
  for word in words1:
    if word in unigrams1:
      unigrams1[word] = unigrams1[word] + 1
    else:
      unigrams1[word] = 1

  # preprocess t2
  t2 = t2.lower()
  no_punc2 = t2.replace('.', '').replace('\n', '')
  words2 = no_punc2.split(' ')
  words2 = [word for word in words2 if word not in stops]

  # contains unigram counts for words
  unigrams2 = {}
  for word in words2:
    if word in unigrams2:
      unigrams2[word] = unigrams2[word] + 1
    else:
      unigrams2[word] = 1

  # merge 2 dicts to count total unique words
  unique_words = unigrams1.copy()
  for k, v in unigrams2.items():
    if k in unique_words:
      unique_words[k] += v
    else:
      unique_words[k] = v

  diff_sum = 0

  for word in unigrams1.keys():
    if word not in unigrams2.keys():
      diff_sum += unigrams1[word]
    else:
      diff_sum += abs(unigrams1[word] - unigrams2[word])

  for word in unigrams2.keys():
    if word not in unigrams1.keys():
      diff_sum += unigrams2[word]

  total_unique_count = 0
  for word, count in unique_words.items():
    total_unique_count += count


  # BIGRAMS

  words1 = [word for word in words1 if word not in stops]

  bigrams1 = {}
  for i in range(len(words1) - 1):
    k = words1[i] + ' ' + words1[i+1]
    if k in bigrams1.keys():
      bigrams1[k] = bigrams1[k] + 1
    else:
      bigrams1[k] = 1

  words2 = [word for word in words2 if word not in stops]
  bigrams2 = {}
  for i in range(len(words2) - 1):
    k = words2[i] + ' ' + words2[i+1]
    if k in bigrams2.keys():
      bigrams2[k] = bigrams2[k] + 1
    else:
      bigrams2[k] = 1


  # merge 2 dicts to count total unique words
  bi_unique_words = bigrams1.copy()
  for k, v in bigrams2.items():
    if k in bi_unique_words:
      bi_unique_words[k] += v
    else:
      bi_unique_words[k] = v

  bi_diff_sum = 0

  for word in bigrams1.keys():
    if word not in bigrams2.keys():
      bi_diff_sum += bigrams1[word]
    else:
      bi_diff_sum += abs(bigrams1[word] - bigrams2[word])

  for word in bigrams2.keys():
    if word not in bigrams1.keys():
      bi_diff_sum += bigrams2[word]

  bi_total_unique_count = 0
  for word, count in bi_unique_words.items():
    bi_total_unique_count += count


  unigram_score = 1 - (diff_sum / total_unique_count)
  bigram_score = 1 - (bi_diff_sum / bi_total_unique_count)


  # weighted average of uni and bigram scores to create overall similarity score
  return (unigram_score*2 + bigram_score) / 3

def main():

  # sample text

  s1 = '''The easiest way to earn points with Fetch Rewards is to just shop for
  the products you already love. If you have any participating brands on your
  receipt, you'll get points based on the cost of the products. You don't need
  to clip any coupons or scan individual barcodes. Just scan each grocery
  receipt after you shop and we'll find the savings for you.'''

  s2 = '''The easiest way to earn points with Fetch Rewards is to just shop for
   the items you already buy. If you have any eligible brands on your receipt,
   you will get points based on the total cost of the products. You do not need
   to cut out any coupons or scan individual UPCs. Just scan your receipt after
   you check out and we will find the savings for you.'''

  s3 = '''We are always looking for opportunities for you to earn more points,
  which is why we also give you a selection of Special Offers. These Special
  Offers are opportunities to earn bonus points on top of the regular points
  you earn every time you purchase a participating brand. No need to pre-select
  these offers, we'll give you the points whether or not you knew about the
  offer. We just think it is easier that way.'''

  # identical to s3
  s4 = '''We are always looking for opportunities for you to earn more points,
  which is why we also give you a selection of Special Offers. These Special
  Offers are opportunities to earn bonus points on top of the regular points
  you earn every time you purchase a participating brand. No need to pre-select
  these offers, we'll give you the points whether or not you knew about the
  offer. We just think it is easier that way.'''

  # random text
  r1 = '''sdlfkjsf ruhvek ebke skufvh weub e dfvub skduhf'''
  r2 = '''xeomxoe wygeyg vkmkj ueueue vkbvk torihjg'''

  # almost identical
  almost1 = '''i hope you have a great day, full of python, strings, and functions'''
  almost2 = '''i hope you have a great, full of python, strings, and functions'''

  # reverse (same unigrams, none of the same bigrams)
  rev1 = '''i am writing this sentence to test my program hoping it works'''
  rev2 = '''works it hoping program my test to sentence this writing am i'''


  print(similarity(s1,s2))
  print(similarity(s2,s3))
  print(similarity(s3,s4))
  print(similarity(r1,r2))
  print(similarity(almost1,almost2))
  print(similarity(rev1,rev2))


main()
