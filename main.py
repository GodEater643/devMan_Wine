from http.server import HTTPServer, SimpleHTTPRequestHandler
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
from pprint import pprint
import exel



env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
Year_Open = 1920
template = env.get_template('template.html')
Time_now = datetime.datetime.now()
Time_now = Time_now.year - Year_Open
exel.winms
"""winms =[{'title': 'Изабелла',
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
"""
         
rendered_page = template.render(exel.winms)








with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
