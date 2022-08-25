from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]

def get_persons():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * from search_person left join search_country on search_person.country_id = search_country.country_id
                        left join search_region on search_person.region_id = search_region.region_id""")
        persons = dictfetchall(cursor)
        return persons

def get_encode():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT search_person.id, search_person.image from search_person""")
        natija = dictfetchall(cursor)
    return natija

########filter
