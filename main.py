from http.server import HTTPServer, SimpleHTTPRequestHandler
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pprint import pprint
import datetime



env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
now = datetime.datetime.now()
now = now.year - 1920
winms =[{'title': 'Изабелла',
         'grade': 'Изабелла',
         'price': 350,
         'image': 'images/izabella.png'},
        
        {'title': 'Гранатовый браслет',
         'grade': 'Мускат розовый',
         'price': 350,
         'image': 'images/granatovyi_braslet.png'},
        
        {'title': 'Шардоне',
         'grade': 'Шардоне',
         'price': 350,
         'image': 'images/shardone.png'},
        
        {'title': 'Белая леди',
         'grade': 'Дамский пальчик',
         'price': 399,
         'image': 'images/belaya_ledi.png'},
        
        {'title': 'Ркацители',
         'grade': 'Ркацители',
         'price': 499,
         'image': 'images/rkaciteli.png'},
        
        {'title': 'Хванчкара',
         'grade': 'Александраули',
         'price': 550,
         'image': 'images/hvanchkara.png'}]

         
rendered_page = template.render(winms=winms)








with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
