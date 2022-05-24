from django.test import TestCase
from quiz.models import  Kunyomi, Onyomi, Meaning, Kanji

# Create your tests here.
class QuizTestCase(TestCase):
    kunyomi = None
    onyomi = None
    meaning = None
    kanji = None

    def setUp(self):
        self.kunyomi = Kunyomi.objects.create(kunyomi='き')
        self.onyomi = Onyomi.objects.create(onyomi='モク')
        self.meaning = Meaning.objects.create(meaning='tree')
        self.kanji = Kanji.objects.create(symbol='木', jlpt=5)
        self.kanji.kunyomis.set([self.kunyomi])
        self.kanji.onyomis.set([self.onyomi])
        self.kanji.meanings.set([self.meaning])

    # Model tests
    def test_kunyomi_has_kunyomi(self):
        self.assertEqual(self.kunyomi.kunyomi, 'き')

    def test_onyomi_has_onyomi(self):
        self.assertEqual(self.onyomi.onyomi, 'モク')

    def test_meaning_has_meaning(self):
        self.assertEqual(self.meaning.meaning, 'tree')
    
    def test_kanji_has_symbol(self):
        self.assertEqual(self.kanji.symbol, '木')

    def test_kanji_has_jlpt(self):
        self.assertEqual(self.kanji.jlpt, 5)

    def test_kanji_has_kunyomis(self):
        self.assertNotEqual(self.kanji.kunyomis, [])

    def test_kanji_onyomis(self):
        self.assertNotEqual(self.kanji.onyomis, [])

    def test_kanji_meanings(self):
        self.assertNotEqual(self.kanji.meanings, [])