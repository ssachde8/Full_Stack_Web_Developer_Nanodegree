#!/usr/bin/env python3
import psycopg2

DB_NAME = "news"
db = psycopg2.connect(database=DB_NAME)


def print_article_result(query):
    print(query['ques'])
    for res in query['ans']:
        print('\t' + str(res[0]) + ' --- ' + str(res[1]) + ' views')
    return


def print_error_result(query):
    print(query['ques'])
    for result in query['ans']:
        print('\t' + str(result[0]) + ' --- ' + str(result[1]) + ' %')
    return


def run_query(query):
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    return results

# 1. What are the most popular three articles of all time?
q1 = "select title, Hits from articles_view limit 3";

# 2. Who are the most popular article authors of all time?
q2 = """select a.name,sum(av.Hits) as Hits from
articles_view as av, authors as a where a.id = av.author
group by a.name order by Hits desc"""

# 3. On which days did more than 1% of requests lead to errors?
q3 = "select * from error_log_view where \"Percent_Error\" > 1"

# Question names
(q1_res, q2_res, q3_res) = dict(), dict(), dict()
q1_res['ques'] = "\n1. The 3 most popular articles of all time are:\n"
q2_res['ques'] = "\n2. The most popular article authors of all time are:\n"
q3_res['ques'] = "\n3. Days with more than 1% of request that lead to an error:\n"

# Store query results
(q1_res['ans'], q2_res['ans'], q3_res['ans']) = run_query(q1), run_query(q2), run_query(q3)

# Print Output
print_article_result(q1_res)
print_article_result(q2_res)
print_error_result(q3_res)
db.close()
