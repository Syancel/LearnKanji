CREATE TABLE kanji (kanji_id INT PRIMARY KEY, symbol NVARCHAR(10), jlpt_level INT);
CREATE TABLE kanji_meaning (id INT PRIMARY KEY, kanji_id INT, meaning_id INT);
CREATE TABLE kanji_kunyomi (id INT PRIMARY KEY, kanji_id INT, kunyomi_id INT);
CREATE TABLE kunyomi (kunyomi_id INT PRIMARY KEY, reading NVARCHAR(50));
CREATE TABLE kanji_onyomi (id INT PRIMARY KEY, kanji_id INT, onyomi_id INT);
CREATE TABLE onyomi (onyomi_id INT PRIMARY KEY, reading NVARCHAR(50));
CREATE TABLE meaning (meaning_id INT PRIMARY KEY, word VARCHAR(MAX));

