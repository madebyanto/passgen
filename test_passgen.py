import unittest

from passgen import generate


class GeneratePasswordTests(unittest.TestCase):
    def test_generate_requires_positive_length(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            generate(0)

    def test_generate_includes_all_character_classes_by_default(self):
        password = generate(16)

        self.assertEqual(len(password), 16)
        self.assertTrue(any(character.islower() for character in password))
        self.assertTrue(any(character.isupper() for character in password))
        self.assertTrue(any(character.isdigit() for character in password))
        self.assertTrue(any(not character.isalnum() for character in password))


if __name__ == "__main__":
    unittest.main()
