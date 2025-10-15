# -*- coding: utf-8 -*-

import sqlite3

def create_db(name):
    with sqlite3.connect(name) as db:
        cursor = db.cursor()

        cursor.executescript('''

            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS code_year(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "назва_кафедри" TEXT,
                "роки" TEXT
            );

            CREATE INDEX IF NOT EXISTS index_code_year_id ON code_year(id);
            CREATE INDEX IF NOT EXISTS index_code_year_назва_кафедри ON code_year("назва_кафедри");
            CREATE INDEX IF NOT EXISTS index_code_year_роки ON code_year("роки");


            CREATE TABLE IF NOT EXISTS job(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                "посада" TEXT NOT NULL,
                "код_рік_id" INTEGER NOT NULL,
                "вчене_звання_вчена_ступінь" TEXT,
                "знак_сумісності" TEXT,
                "НПП_ПП" TEXT,
                FOREIGN KEY (код_рік_id) REFERENCES code_year(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_job_id ON job(id);
            CREATE INDEX IF NOT EXISTS index_job_посада ON job("посада");
            CREATE INDEX IF NOT EXISTS index_job_код_рік_id ON job("код_рік_id");
            CREATE INDEX IF NOT EXISTS index_job_вчене_звання_вчена_ступінь ON job("вчене_звання_вчена_ступінь");
            CREATE INDEX IF NOT EXISTS index_job_знак_сумісності ON job("знак_сумісності");

            CREATE TABLE IF NOT EXISTS person(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "ім_я" TEXT,
                "прізвище" TEXT,
                "по-батькові" TEXT,
                "job_id" INTEGER NOT NULL,
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_person_id ON person(id);
            CREATE INDEX IF NOT EXISTS index_person_імя ON person("ім'я");
            CREATE INDEX IF NOT EXISTS index_person_прізвище ON person("прізвище");
            CREATE INDEX IF NOT EXISTS index_person_побатькові ON person("по-батькові");
            CREATE INDEX IF NOT EXISTS index_person_job_id ON person("job_id");

            CREATE TABLE IF NOT EXISTS vacancy(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "назва" TEXT,
                "номер" INTEGER,
                "job_id" INTEGER NOT NULL,
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_vacancy_id ON vacancy(id);
            CREATE INDEX IF NOT EXISTS index_vacancy_назва ON vacancy("назва");
            CREATE INDEX IF NOT EXISTS index_vacancy_номер ON vacancy("номер");
            CREATE INDEX IF NOT EXISTS index_vacancy_job_id ON vacancy("job_id");

            CREATE TABLE IF NOT EXISTS first_semester(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "ставка" REAL,
                "лекції" REAL,
                "практичні_(семінарські)_заняття" REAL,
                "лабораторні_роботи" REAL,
                "екзамени" REAL,
                "консультації_перед_екзаменами" REAL,
                "заліки" REAL,
                "кваліфікаційна_робота" REAL,
                "атестаційний_екзамен" REAL,
                "виробнича_практика" REAL,
                "навчальна_практика" REAL,
                "поточні_консультації" REAL,
                "індивідуальні" REAL,
                "курсові_роботи" REAL,
                "аспірантські_екзамени" REAL,
                "керівництво_аспірантами" REAL,
                "консультування_докторантів_здобувачів" REAL,
                "керівництво_ФПК" REAL,
                "робота_приймальної_комісії" REAL,
                "інше" REAL,
                "всього" REAL,
                "job_id" INTEGER NOT NULL,
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_first_semester_id ON first_semester(id);
            CREATE INDEX IF NOT EXISTS index_first_semester_ставка ON first_semester("ставка");
            CREATE INDEX IF NOT EXISTS index_first_semester_лекції ON first_semester("лекції");
            CREATE INDEX IF NOT EXISTS index_first_semester_практичні_семінарські_заняття ON first_semester("практичні_(семінарські)_заняття");
            CREATE INDEX IF NOT EXISTS index_first_semester_лабораторні_роботи ON first_semester("лабораторні_роботи");
            CREATE INDEX IF NOT EXISTS index_first_semester_екзамени ON first_semester("екзамени");
            CREATE INDEX IF NOT EXISTS index_first_semester_консультації_перед_екзаменами ON first_semester("консультації_перед_екзаменами");
            CREATE INDEX IF NOT EXISTS index_first_semester_заліки ON first_semester("заліки");
            CREATE INDEX IF NOT EXISTS index_first_semester_кваліфікаційна_робота ON first_semester("кваліфікаційна_робота");
            CREATE INDEX IF NOT EXISTS index_first_semester_атестаційний_екзамен ON first_semester("атестаційний_екзамен");
            CREATE INDEX IF NOT EXISTS index_first_semester_виробнича_практика ON first_semester("виробнича_практика");
            CREATE INDEX IF NOT EXISTS index_first_semester_навчальна_практика ON first_semester("навчальна_практика");
            CREATE INDEX IF NOT EXISTS index_first_semester_поточні_консультації ON first_semester("поточні_консультації");
            CREATE INDEX IF NOT EXISTS index_first_semester_індивідуальні ON first_semester("індивідуальні");
            CREATE INDEX IF NOT EXISTS index_first_semester_курсові_роботи ON first_semester("курсові_роботи");
            CREATE INDEX IF NOT EXISTS index_first_semester_аспірантські_екзамени ON first_semester("аспірантські_екзамени");
            CREATE INDEX IF NOT EXISTS index_first_semester_керівництво_аспірантами ON first_semester("керівництво_аспірантами");
            CREATE INDEX IF NOT EXISTS index_first_semester_консультування_докторантів_здобувачів ON first_semester("консультування_докторантів_здобувачів");
            CREATE INDEX IF NOT EXISTS index_first_semester_керівництво_ФПК ON first_semester("керівництво_ФПК");
            CREATE INDEX IF NOT EXISTS index_first_semester_робота_приймальної_комісії ON first_semester("робота_приймальної_комісії");
            CREATE INDEX IF NOT EXISTS index_first_semester_інше ON first_semester("інше");
            CREATE INDEX IF NOT EXISTS index_first_semester_всього ON first_semester("всього");
            CREATE INDEX IF NOT EXISTS index_first_semester_job_id ON first_semester("job_id");

            CREATE TABLE IF NOT EXISTS second_semester (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                "ставка" REAL,
                "лекції" REAL,
                "практичні_(семінарські)_заняття" REAL,
                "лабораторні_роботи" REAL,
                "екзамени" REAL,
                "консультації_перед_екзаменами" REAL,
                "заліки" REAL,
                "кваліфікаційна_робота" REAL,
                "атестаційний_екзамен" REAL,
                "виробнича_практика" REAL,
                "навчальна_практика" REAL,
                "поточні_консультації" REAL,
                "індивідуальні" REAL,
                "курсові_роботи" REAL,
                "аспірантські_екзамени" REAL,
                "керівництво_аспірантами" REAL,
                "консультування_докторантів_здобувачів" REAL,
                "керівництво_ФПК" REAL,
                "робота_приймальної_комісії" REAL,
                "інше" REAL,
                "всього" REAL,
                "job_id" INTEGER NOT NULL,
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_second_semester_id ON second_semester(id);
            CREATE INDEX IF NOT EXISTS index_second_semester_ставка ON second_semester("ставка");
            CREATE INDEX IF NOT EXISTS index_second_semester_лекції ON second_semester("лекції");
            CREATE INDEX IF NOT EXISTS index_second_semester_практичні_семінарські_заняття ON second_semester("практичні_(семінарські)_заняття");
            CREATE INDEX IF NOT EXISTS index_second_semester_лабораторні_роботи ON second_semester("лабораторні_роботи");
            CREATE INDEX IF NOT EXISTS index_second_semester_екзамени ON second_semester("екзамени");
            CREATE INDEX IF NOT EXISTS index_second_semester_консультації_перед_екзаменами ON second_semester("консультації_перед_екзаменами");
            CREATE INDEX IF NOT EXISTS index_second_semester_заліки ON second_semester("заліки");
            CREATE INDEX IF NOT EXISTS index_second_semester_кваліфікаційна_робота ON second_semester("кваліфікаційна_робота");
            CREATE INDEX IF NOT EXISTS index_second_semester_атестаційний_екзамен ON second_semester("атестаційний_екзамен");
            CREATE INDEX IF NOT EXISTS index_second_semester_виробнича_практика ON second_semester("виробнича_практика");
            CREATE INDEX IF NOT EXISTS index_second_semester_навчальна_практика ON second_semester("навчальна_практика");
            CREATE INDEX IF NOT EXISTS index_second_semester_поточні_консультації ON second_semester("поточні_консультації");
            CREATE INDEX IF NOT EXISTS index_second_semester_індивідуальні ON second_semester("індивідуальні");
            CREATE INDEX IF NOT EXISTS index_second_semester_курсові_роботи ON second_semester("курсові_роботи");
            CREATE INDEX IF NOT EXISTS index_second_semester_аспірантські_екзамени ON second_semester("аспірантські_екзамени");
            CREATE INDEX IF NOT EXISTS index_second_semester_керівництво_аспірантами ON second_semester("керівництво_аспірантами");
            CREATE INDEX IF NOT EXISTS index_second_semester_консультування_докторантів_здобувачів ON second_semester("консультування_докторантів_здобувачів");
            CREATE INDEX IF NOT EXISTS index_second_semester_керівництво_ФПК ON second_semester("керівництво_ФПК");
            CREATE INDEX IF NOT EXISTS index_second_semester_робота_приймальної_комісії ON second_semester("робота_приймальної_комісії");
            CREATE INDEX IF NOT EXISTS index_second_semester_інше ON second_semester("інше");
            CREATE INDEX IF NOT EXISTS index_second_semester_всього ON second_semester("всього");
            CREATE INDEX IF NOT EXISTS index_second_semester_job_id ON second_semester("job_id");

            CREATE TABLE IF NOT EXISTS  academic_year (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                "ставка" REAL,
                "лекції" REAL,
                "практичні_(семінарські)_заняття" REAL,
                "лабораторні_роботи" REAL,
                "екзамени" REAL,
                "консультації_перед_екзаменами" REAL,
                "заліки" REAL,
                "кваліфікаційна_робота" REAL,
                "атестаційний_екзамен" REAL,
                "виробнича_практика" REAL,
                "навчальна_практика" REAL,
                "поточні_консультації" REAL,
                "індивідуальні" REAL,
                "курсові_роботи" REAL,
                "аспірантські_екзамени" REAL,
                "керівництво_аспірантами" REAL,
                "консультування_докторантів_здобувачів" REAL,
                "керівництво_ФПК" REAL,
                "робота_приймальної_комісії" REAL,
                "інше" REAL,
                "всього" REAL,
                "розподіл_ставок_навчального_навантаження" TEXT,
                "job_id" INTEGER NOT NULL,
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_academic_year_id ON academic_year(id);
            CREATE INDEX IF NOT EXISTS index_academic_year_ставка ON academic_year("ставка");
            CREATE INDEX IF NOT EXISTS index_academic_year_лекції ON academic_year("лекції");
            CREATE INDEX IF NOT EXISTS index_academic_year_практичні_семінарські_заняття ON academic_year("практичні_(семінарські)_заняття");
            CREATE INDEX IF NOT EXISTS index_academic_year_лабораторні_роботи ON academic_year("лабораторні_роботи");
            CREATE INDEX IF NOT EXISTS index_academic_year_екзамени ON academic_year("екзамени");
            CREATE INDEX IF NOT EXISTS index_academic_year_консультації_перед_екзаменами ON academic_year("консультації_перед_екзаменами");
            CREATE INDEX IF NOT EXISTS index_academic_year_заліки ON academic_year("заліки");
            CREATE INDEX IF NOT EXISTS index_academic_year_кваліфікаційна_робота ON academic_year("кваліфікаційна_робота");
            CREATE INDEX IF NOT EXISTS index_academic_year_атестаційний_екзамен ON academic_year("атестаційний_екзамен");
            CREATE INDEX IF NOT EXISTS index_academic_year_виробнича_практика ON academic_year("виробнича_практика");
            CREATE INDEX IF NOT EXISTS index_academic_year_навчальна_практика ON academic_year("навчальна_практика");
            CREATE INDEX IF NOT EXISTS index_academic_year_поточні_консультації ON academic_year("поточні_консультації");
            CREATE INDEX IF NOT EXISTS index_academic_year_індивідуальні ON academic_year("індивідуальні");
            CREATE INDEX IF NOT EXISTS index_academic_year_курсові_роботи ON academic_year("курсові_роботи");
            CREATE INDEX IF NOT EXISTS index_academic_year_аспірантські_екзамени ON academic_year("аспірантські_екзамени");
            CREATE INDEX IF NOT EXISTS index_academic_year_керівництво_аспірантами ON academic_year("керівництво_аспірантами");
            CREATE INDEX IF NOT EXISTS index_academic_year_консультування_докторантів_здобувачів ON academic_year("консультування_докторантів_здобувачів");
            CREATE INDEX IF NOT EXISTS index_academic_year_керівництво_ФПК ON academic_year("керівництво_ФПК");
            CREATE INDEX IF NOT EXISTS index_academic_year_робота_приймальної_комісії ON academic_year("робота_приймальної_комісії");
            CREATE INDEX IF NOT EXISTS index_academic_year_інше ON academic_year("інше");
            CREATE INDEX IF NOT EXISTS index_academic_year_всього ON academic_year("всього");
            CREATE INDEX IF NOT EXISTS index_academic_year_розподіл_ставок_навчального_навантаження ON academic_year("розподіл_ставок_навчального_навантаження");
            CREATE INDEX IF NOT EXISTS index_academic_year_job_id ON academic_year("job_id");

            CREATE TABLE IF NOT EXISTS  check_db (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "зменшення" INTEGER,
                "мінімум" INTEGER,
                "максимум" INTEGER,
                "загальний_мінімум" INTEGER,
                "загальний_максимум" INTEGER,
                "job_id" INTEGER NOT NULL,
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS index_check_db_id ON check_db(id);
            CREATE INDEX IF NOT EXISTS index_check_db_мінімум ON check_db("мінімум");
            CREATE INDEX IF NOT EXISTS index_check_db_максимум ON check_db("максимум");
            CREATE INDEX IF NOT EXISTS index_check_db_загальний_мінімум ON check_db("загальний_мінімум");
            CREATE INDEX IF NOT EXISTS index_check_db_загальний_максимум ON check_db("загальний_максимум");
            CREATE INDEX IF NOT EXISTS index_check_db_job_id ON check_db("job_id");

            CREATE TABLE IF NOT EXISTS  check_assistant_teacher (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                "помилка" INTEGER,
                "job_id" INTEGER NOT NULL, 
                FOREIGN KEY ("job_id") REFERENCES job (id) ON DELETE CASCADE,
                UNIQUE("помилка", "job_id")
            );

            CREATE INDEX IF NOT EXISTS index_check_assistant_teacher_id ON check_assistant_teacher(id);
            CREATE INDEX IF NOT EXISTS index_check_assistant_teacher_помилка ON check_assistant_teacher("помилка");
            CREATE INDEX IF NOT EXISTS index_check_assistant_teacher_job_id ON check_assistant_teacher("job_id");


            CREATE TABLE IF NOT EXISTS  load (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL, 
                npp_pp TEXT NOT NULL, 
                value REAL NOT NULL
            );

            CREATE INDEX IF NOT EXISTS index_load_id ON load(id);
            CREATE INDEX IF NOT EXISTS index_load_name ON load(name);
            CREATE INDEX IF NOT EXISTS index_load_npp_pp ON load(npp_pp);
            CREATE INDEX IF NOT EXISTS index_load_load ON load(value);


        ''')
   
        db.commit()

