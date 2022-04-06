import db_conn as db

def get_meaning(kanjis):
    list_meanings = []
    for item in kanjis:
        meaning = item['meanings']
        for i in meaning:
            if i in list_meanings:
                pass
            else:
                list_meanings.append(i)
    counter = 1
    for item in list_meanings:
        sql = "INSERT INTO meaning VALUES (" + str(counter) + ",'" + item.replace("\'", "\'\'") + "')"
        #db.db_exe(sql)
        counter += 1
    return list_meanings

def get_onyomi(kanjis):
    list_onyomi = []
    for item in kanjis:
        onyomi = item['on_readings']
        for i in onyomi:
            if i in list_onyomi:
                pass
            else:
                list_onyomi.append(i)
    counter = 1
    for item in list_onyomi:
        sql = "INSERT INTO onyomi VALUES (" + str(counter) + ",'" + item.replace("\'", "\'\'") + "')"
        print(sql)
        #db.db_exe(sql)
        counter += 1
    return list_onyomi

def get_kunyomi(kanjis):
    list_kunyomi = []
    for item in kanjis:
        kunyomi = item['kun_readings']
        for i in kunyomi:
            if i in list_kunyomi:
                pass
            else:
                list_kunyomi.append(i)
    counter = 1
    for item in list_kunyomi:
        sql = "INSERT INTO kunyomi VALUES (" + str(counter) + ",'" + item.replace("\'", "\'\'") + "')"
        print(sql)
        #db.db_exe(sql)
        counter += 1
    return list_kunyomi

def fill_kanji(kanjis, meaning_list, onyomi_list, kunyomi_list):
    counter = 1
    counter_m = 1
    counter_o = 1
    counter_k = 1
    for item in kanjis:
        symbol = item['kanji']
        jlpt = item['jlpt']
        sql_kanji = "INSERT INTO kanji VALUES (" + str(counter) + ",'" + symbol + "'," + str(jlpt) + ")"
        print(sql_kanji)
        db.db_exe(sql_kanji)
        meaning = item['meanings']
        kunyomi = item['kun_readings']
        onyomi = item['on_readings']
        for m in meaning:
            meaning_id = meaning_list.index(m) + 1
            sql_kanji_meaning = "INSERT INTO kanji_meanings VALUES (" + str(counter_m) + "," + str(counter) + "," + str(meaning_id) + ")"
            print(sql_kanji_meaning)
            db.db_exe(sql_kanji_meaning)
            counter_m += 1
        for k in kunyomi:
            kunyomi_id = kunyomi_list.index(k) + 1
            sql_kanji_kunyomi = "INSERT INTO kanji_kunyomis VALUES (" + str(counter_k) + "," + str(counter) + "," + str(kunyomi_id) + ")"
            print(sql_kanji_kunyomi)
            db.db_exe(sql_kanji_kunyomi)
            counter_k += 1
        for o in onyomi:
            onyomi_id = onyomi_list.index(o) + 1
            sql_kanji_onyomi = "INSERT INTO kanji_onyomis VALUES (" + str(counter_o) + "," + str(counter) + "," + str(onyomi_id) + ")"
            print(sql_kanji_onyomi)
            db.db_exe(sql_kanji_onyomi)
            counter_o += 1
        counter += 1
    return