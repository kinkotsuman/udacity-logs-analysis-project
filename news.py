#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def get_titles():
    """ Get the most popular three articles of all time. """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title, count(log.path) as views \
                from articles left join log \
                on articles.slug = replace(log.path, '/article/', '') \
                group by log.path, articles.title \
                order by views desc \
                limit 3;")
    result = c.fetchall()
    print("\nTop 3 Articles by Views\n-------------------------")
    for row in result:
        print("\"" + row[0] + "\"" + " -- " + str(row[1]) + " views")
    db.close()


def get_authors():
    """Get the most popular article authors of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view topfive as \
                select articles.author, articles.title, \
                count(log.path) as views \
                from articles left join log \
                on articles.slug = replace(log.path, '/article/', '') \
                group by log.path, articles.title, articles.author \
                order by views desc; \
                select authors.name, sum(topfive.views) as views \
                from authors join topfive \
                on topfive.author = authors.id group by authors.name \
                order by views desc;")
    result = c.fetchall()
    print("\nThe Most Popular Article Authors of All Time\n \
            ------------------------------------------------")
    for row in result:
        print("\"" + row[0] + "\"" + " -- " + str(row[1]) + " views")
    db.close()


def get_errors():
    """Get days that have more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view step1 as \
                select time::date, count(*) as base \
                from log group by time::date; \
            create view step2 as \
                select log.time::date, log.status, \
                count(log.status) as total_errors \
                from log where log.status = '404 NOT FOUND' \
                group by log.time::date, log.status \
                order by log.time::date; \
            select step1.time as day, \
                (round(((step2.total_errors::float/step1.base::float)*100)\
                ::numeric,2) || '%') as error \
                from step1 join step2 \
                on step1.time = step2.time \
                and ((step2.total_errors::decimal/step1.base::decimal)\
                *100)>= 1;")
    result = c.fetchall()
    print("\nDays That Have More Than 1% of Requests Lead to Errors\n \
            -------------------------------------------------------")
    for row in result:
        print("\"" + str(row[0]) + "\"" + " -- " + row[1])
    db.close()

if __name__ == "__main__":
    get_titles()
    get_authors()
    get_errors()
