class Trie(object):

    def __init__(self):

        self.root = dict()

    def add_word(self, word):

        node = self.root

        for c in word:
            if c not in node:
                node[c] = dict()

            node = node[c]

        node['#'] = '#'

        return

    def get_all_words_in_big_str(self, big_str):

        node = self.root

        words = []
        for i, c in enumerate(big_str):
            if c in node:
                node = node[c]
            else:
                break
            if '#' in node:
                words.append(big_str[:i+1])

        return words


def get_words_from_big(list_of_words, big_str):

    trie = Trie()

    for word in list_of_words:
        trie.add_word(word)

    all_words = set()

    for i in range(len(big_str)):
        all_words = all_words | set(trie.get_all_words_in_big_str(big_str[i:]))

    return all_words


def main():

    long_str = 'abbbbcasdfasdf'
    word_list = ['ab', 'bc', 'cc']
    print(get_words_from_big(word_list, long_str))

if __name__ == '__main__':
    main()
