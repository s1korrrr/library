import argparse
from book import BookSQLData

parser = argparse.ArgumentParser(
    description="basic application for managing library"
)

parser.add_argument('action',
                    help='choose action',
                    choices=['list', 'add',
                             'book', 'del',
                             'update'])

parser.add_argument('--name',
                    help="name of book - need in 'add', "
                         "'update', 'book', 'del' commands",
                    required=False)

parser.add_argument('--author',
                    help="author of book - need in 'add', "
                         "'update' commands",
                    required=False)

arguments = parser.parse_args()

if arguments.action == 'add':
    book = {}
    book['name'] = arguments.name
    book['author'] = arguments.author
    print("Book: " + book['name'] + " added. Author is: " + book['author'])
    b1 = BookSQLData('database.db')
    b1.add('dziady', 'ktos')
    b1.add('d', 'a')


