import db_conn as db
import file_read as file
import fill_db

kanjis = file.json_read('/Users/marcel/Projects/Berufsschule/LearnKanji/Datenbank/kanjiapi_full.json')

meaning = fill_db.get_meaning(kanjis)
onyomi = fill_db.get_onyomi(kanjis)
kunyomi = fill_db.get_kunyomi(kanjis)

fill_db.fill_kanji(kanjis, meaning, onyomi, kunyomi)
