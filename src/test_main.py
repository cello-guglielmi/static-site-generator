import unittest
from main import extract_title

class TestExtractTitle(unittest.TestCase):
    # extract_title() test cases

    def test_title_regular(self):
        # Case: Default h1 title present
        text = '# Wonderful Title\nAs you might have seen, the title is quite wonderful.'
        result = extract_title(text)
        expected = 'Wonderful Title'
        self.assertEqual(result, expected)

    def test_title_missing(self):
        # Case: Missing h1 title
        with self.assertRaises(Exception):
            text = 'This text is missing a header'
            result = extract_title(text)

    def test_title_double(self):
        # Case: Multiple h1 titles present
        text = '# Wonderful Title\n# A Second Title?\nAs you might have seen, the title is quite wonderful.'
        result = extract_title(text)
        expected = 'Wonderful Title'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()