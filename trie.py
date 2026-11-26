class TrieNode:
    """
    Represents one node in the Trie.
    """

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie data structure for efficient word and prefix searching.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """

        if not isinstance(word, str) or not word:
            return

        node = self.root

        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        """
        Check whether a complete word exists in the Trie.
        """

        if not isinstance(word, str) or not word:
            return False

        node = self.root

        for char in word.lower():
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word

    def starts_with(self, prefix):
        """
        Check whether any inserted word starts with the prefix.
        """

        if not isinstance(prefix, str):
            return False

        node = self.root

        for char in prefix.lower():
            if char not in node.children:
                return False

            node = node.children[char]

        return True