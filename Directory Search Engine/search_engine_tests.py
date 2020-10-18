from hashtables import *
from search_engine import *
import unittest


class MyTest(unittest.TestCase):
    def test_search_engine(self):
        stopwords = import_stopwords("stop_words.txt", HashTableSepchain())
        search_1 = SearchEngine("docs", stopwords)
        search_2 = SearchEngine("docs", stopwords)
        self.assertEqual(search_1, search_2)
        print(search_1)
        search = SearchEngine("docs", stopwords)
        lines = search.read_file("test.txt")
        parse_words = search.parse_words(lines)
        self.assertEqual(search.parse_words(lines), ['computer', 'science'])
        search.count_words("test.txt", parse_words)
        self.assertEqual(search.get_scores(parse_words), [('test.txt', 1.6931471805599454),
                                                          ('hash_table.txt', 0.01904761904761905),
                                                          ('information_retrieval.txt', 0.034482758620689655)])
        self.assertAlmostEqual(search.get_wf(4), 2.386294361119891)
        self.assertAlmostEqual(search.get_wf(0), 0)
        scores = search.get_scores(parse_words)
        self.assertEqual(search.get_scores(parse_words), [('test.txt', 1.6931471805599454),
                                                                ('hash_table.txt', 0.01904761904761905),
                                                                ('information_retrieval.txt', 0.034482758620689655)])
        self.assertEqual(search.rank(scores), [('test.txt', 1.6931471805599454),
                                                ('information_retrieval.txt', 0.034482758620689655),
                                                ('hash_table.txt', 0.01904761904761905)])


    def test_sepchain(self):
        sepchain = HashTableSepchain()
        self.assertRaises(KeyError, sepchain.remove, "goodbye")
        sepchain.put("hello", hash_string("hello", sepchain.table_size))
        sepchain.put("lehlo", hash_string("hello", sepchain.table_size))
        self.assertEqual(sepchain.size(), 2)
        sepchain.put("abc", hash_string("abc", sepchain.table_size))
        sepchain.put("cba", hash_string("cba", sepchain.table_size))
        sepchain.put("bac", hash_string("bac", sepchain.table_size))
        sepchain.put("d", hash_string("d", sepchain.table_size))
        sepchain.put("e", hash_string("e", sepchain.table_size))
        sepchain.put("f", hash_string("f", sepchain.table_size))
        sepchain.put("g", hash_string("g", sepchain.table_size))
        sepchain.put("h", hash_string("h", sepchain.table_size))
        sepchain.put("i", hash_string("i", sepchain.table_size))
        sepchain.put("j", hash_string("j", sepchain.table_size))
        sepchain.put("k", hash_string("k", sepchain.table_size))
        sepchain.put("l", hash_string("l", sepchain.table_size))
        sepchain.put("m", hash_string("m", sepchain.table_size))
        sepchain.put("n", hash_string("n", sepchain.table_size))
        sepchain.put("o", hash_string("o", sepchain.table_size))
        sepchain.put("p", hash_string("p", sepchain.table_size))
        sepchain.put("q", hash_string("q", sepchain.table_size))
        self.assertEqual(sepchain.size(), 19)
        # test for resize
        self.assertEqual(sepchain.contains("hello"), True)
        self.assertEqual(sepchain.contains("lehlo"), True)
        self.assertEqual(sepchain.get("lehlo"), 6)
        self.assertEqual(sepchain.get("bac"), 0)
        self.assertEqual(sepchain.contains("hello"), True)
        self.assertEqual(sepchain.contains("goodbye"), False)
        sepchain.remove("hello")
        sepchain.remove("lehlo")
        sepchain.remove("d")
        sepchain.remove("e")
        sepchain.remove("f")
        sepchain.remove("g")
        sepchain.remove("h")
        sepchain.remove("i")
        sepchain.remove("j")
        sepchain.remove("k")
        sepchain.remove("l")
        sepchain.remove("m")
        sepchain.remove("n")
        sepchain.remove("o")
        sepchain.remove("p")
        sepchain.remove("q")
        self.assertEqual(sepchain.size(), 3)
        sepchain.put("g", hash_string("g", sepchain.table_size))
        sepchain.remove("g")
        self.assertEqual(sepchain.collisions(), 0)

    def test_node(self):
        node_1 = Node("hello", 2)
        node_2 = Node("hello", 2)
        self.assertEqual(node_1, node_2)
        node = Node("goodbye", 4)
        print(node)

    def test_hashtables(self):
        sepchain_1 = HashTableSepchain()
        sepchain_2 = HashTableSepchain()
        self.assertEqual(sepchain_1, sepchain_2)
        print(sepchain_1)


if __name__ == '__main__':
    unittest.main()

