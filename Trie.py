class TrieNode:
    '''
    Definition for TrieNode with instance variables for children, is_end_of_word, and word
    '''
    # Initialize TrieNode instance with an empty dictionary for children, False for is_end_of_word, and an empty string for word
    def __init__(self):
        self.children = {} # dictionary to store children nodes
        self.is_end_of_word = False # indicates if the node is the end of a word
        self.word = "" # store the word associated with the node

class Trie:
    '''
    Definition for Trie with a root node initialized with TrieNode instance
    '''
    # Initialize Trie instance with a root node initialized with TrieNode instance
    def __init__(self):
        self.root = TrieNode() # root node of the Trie

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root # start from the root node
        for char in word:
            # If the character is not in children, insert a new TrieNode instance as the child
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # move to the next node
        node.is_end_of_word = True # mark the node as the end of the word
        node.word = word # store the word

    # Visualize the Trie
    def visualise(self, node=None, level=0, prefix=""):
        # if node is None, start from the root node
        if node is None:
            node = self.root
        for char, child in node.children.items():
            # print the node with the prefix and level of indentation
            print(" " * level + prefix + char)
            self.visualise(child, level + 1, prefix + char)

    # Search for all words in the Trie with the given prefix
    def search(self, prefix):
        node = self.root # start from the root node
        for char in prefix:
            # if the character is not in children, return an empty list
            if char not in node.children:
                return []
            node = node.children[char] # move to the next node

        results = [] # list to store the results
        self._search_helpter(node, prefix, results) # call the helper function to search for the words
        # if there is only one result, return the result directly
        return results

    # Helper function for search() to find all words starting from the node with the given prefix
    def _search_helpter(self, node, prefix, results):
        # if the node is the end of a word, add the prefix to the results
        if node.is_end_of_word:
            results.append(prefix)
        for child_char in node.children.keys():
            # call the helper function for each child node with the updated prefix
            self._search_helpter(node.children[child_char], prefix + child_char, results)



if __name__ == "__main__":
    # Example usage
    trie = Trie()
    trie.insert("Action")
    trie.insert("Action-Adventure")
    trie.insert("Action Role-Playing")
    trie.insert("Beat 'Em Up")
    # first_word = trie.search("Action")
    # print(first_word) # Output: "action"
    words = trie.search("Action ")
    print(words)
    # trie.visualise()
