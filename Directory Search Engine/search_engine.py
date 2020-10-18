import math
import os
from hashtables import HashTableSepchain, import_stopwords


def main():
    """ Main Function that runs search engine
    """
    user_input = input("Input path of directory: ")
    stopwords = import_stopwords("stop_words.txt", HashTableSepchain())
    search_engine = SearchEngine(user_input, stopwords)
    search_input = input("Search Engine: ")
    if search_input.find("s: ") == -1:
        print("Prepend 's: ' prior to your search query")
        search_input = input("Search Engine: ")
    else:
        search_input = search_input.replace("s: ", "")
    while search_input != "q:":
        result = SearchEngine.search(search_engine, search_input)
        print(result)
        search_input = input("Search Engine: ")
        if search_input.find("s: ") == -1:
            print("Prepend 's: ' prior to your search query")
            search_input = input("Search Engine: ")
        else:
            search_input = search_input.replace("s: ", "")


class SearchEngine:
    """ Search Engine
    Attributes:
        directory (str): a directory name
        stopwords (HashTableSepchain): a sepchain hash table containing stopwords
        doc_length (HashTableSepchain): a sepchain hash table containing
                                      total num of words in each doc
        term_freqs (HashTableSepchain): a sepcahin hash table of hash tables
                                      containing freq of each term in docs
    """

    def __init__(self, directory, stopwords):
        self.doc_length = HashTableSepchain()
        self.term_freqs = HashTableSepchain()
        self.stopwords = stopwords
        self.index_files(directory)

    def __eq__(self, other):
        return isinstance(other, type(self)) \
               and self.doc_length == other.doc_length \
               and self.term_freqs == other.term_freqs \
               and self.stopwords == other.stopwords

    def __repr__(self):
        return "Doc Length: (%s), Term Freq: (%s), Stop Words: (%s)" \
               % (self.doc_length, self.term_freqs, self.stopwords)

    def read_file(self, infile):
        """ A helper function to read a file
        Arguments:
            infile (str): the path to a file
        Returns:
            list: a list of str read from a file
        """
        words = []
        with open(infile) as file:
            for line in file:
                words.append(line)
        return words

    def parse_words(self, lines):
        """ Splits strings into words by spaces
        Arguments:
            lines (list): a list of strings
        Returns:
            list: a list of words
        """
        lines_list = []
        for line in lines:
            line_split = line.split()
            for word in line_split:
                word = word.lower()
                word = word.replace(",", "")
                word = word.replace(".", "")
                word = word.replace("?", "")
                word = word.replace("!", "")
                word = word.replace("[", "")
                word = word.replace("]", "")
                word = word.replace("{", "")
                word = word.replace("}", "")
                word = word.replace("(", "")
                word = word.replace(")", "")
                word = word.replace("\\n", "")
                lines_list.append(word)
        words = self.exclude_stopwords(lines_list)
        return words

    def exclude_stopwords(self, terms):
        """ Exclude stopwords from the list of terms
        Arguments:
            terms (list): a list of strings
        Returns:
            list: a list of strings with stopwords removed
        """
        set_bool = True
        no_stopwords = []
        keys = HashTableSepchain.keys(self.stopwords)
        for word in terms:
            for key in keys:
                if word == key:
                    set_bool = False
                    break
                else:
                    set_bool = True
            if set_bool:
                no_stopwords.append(word)
        return no_stopwords

    def count_words(self, file_path_name, words):
        """ Counts words in a file and store freq of each
        Arguments:
            file_path_name (str): the file name
            words (list): a list of words
        """
        for word in words:
            if self.term_freqs.contains(word) is False:
                self.term_freqs[word] = HashTableSepchain()
            if self.term_freqs[word].contains(file_path_name) is False:
                self.term_freqs[word][file_path_name] = 1
            else:
                self.term_freqs[word][file_path_name] += 1
        self.doc_length[file_path_name] = len(words)

    def index_files(self, directory):
        """ Index all text files in a given directory
        Arguments:
            directory (str): the path of a directory
        """
        list_files = os.listdir(directory)
        parts = []
        for item in list_files:
            if os.path.isfile(item):
                os.path.join(directory, item)
                parts.append(os.path.splitext(item))
        for idx, part in enumerate(parts):
            if parts[idx][1] == '.txt':
                txt_file = ''.join(parts[idx])
                lines = self.read_file(txt_file)
                parse_words = self.parse_words(lines)
                self.count_words(txt_file, parse_words)

    def get_wf(self, term_freq):
        """ Computes the weighted freq
        Arguments:
            term_freq (float): term frequency
        Returns:
            float: the weighted frequency
        """
        if term_freq > 0:
            weighted_freq = 1 + math.log(term_freq)
        else:
            weighted_freq = 0
        return weighted_freq


    def get_scores(self, terms):
        """ Creates a list of scores for each file in corpus
        Arguments:
            terms (list): a list of str
        Returns:
            list: a list of tuples, containing file_path name and relevancy score
        """
        scores = HashTableSepchain()
        scores_list = []
        for term in terms:
            if self.term_freqs.contains(term) is True:
                hash_table_term = self.term_freqs[term]
                for file in hash_table_term.keys():
                    val = self.get_wf(hash_table_term[file])
                    if scores.contains(file) is False:
                        scores[file] = val + self.get_wf(hash_table_term[file])
        for file in scores.keys():
            scores[file] /= self.doc_length[file]
            scores_list.append((file, scores[file]))
        return scores_list


    def rank(self, scores):
        """ Ranks files in the descending order of relevancy
        Arguments:
            scores (list): a list of tuples (file_path_name, score)
        Returns:
            list: a list of tuples (file_path_name, score) sorted in descending order
                  of relevancy
        """
        scores_tuples = self.bubble_sort(scores)
        return scores_tuples

    def bubble_sort(self, alist):
        """ Function to sort a list by bubble sort
        Arguments:
            alist (list): a list of ints to be sorted
        Returns:
            int: number of comparisons
        """
        alist_len = len(alist) - 1
        for i in range(alist_len):
            for j in range(alist_len - i):
                if alist[j][1] < alist[j + 1][1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]
        return alist

    def search(self, query):
        """ Search for the query terms in files
        Arguments:
            query (str): query input
        Returns:
            list: a list of tuples (file_path_name, score) sorted in descending order
        """
        parse_words = self.parse_words([query])
        scores = self.get_scores(parse_words)
        final = self.rank(scores)
        return final


if __name__ == '__main__':
    main()
