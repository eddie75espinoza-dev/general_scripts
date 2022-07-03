from googlesearch import search

"""  ""try:
    print(int("eddie75espinoza"))
except Exception as e:
    query = "python:" + str(e)
    solution = search(query, lang = 'es')
    for i in solution:
        print(i)"""

res = search("f1")
print(list(res))