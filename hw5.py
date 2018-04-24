import csv
import string
import json
import pickle

def main(filename):
    file=open(filename)
    lines = file.readlines()
    all_words = []

    for line in lines:
        words =line.split()
        
        for word in words:
            word = word.strip(string.punctuation)
            if word:
                all_words.append(word)
                
    from collections import Counter
    word_counter = Counter(all_words)

    with open("word_count.csv", "w") as csv_file:
        writer =csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(word_counter.most_common())

    json.dump(word_counter,open('word_count.json','w'))
    pickle.dump(word_counter,open('word_count.pkl','wb'))

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")
