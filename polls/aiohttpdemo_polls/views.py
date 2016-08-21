from aiohttp import web

from aiohttp import web
import aiohttp_jinja2
import jinja2
app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('C:/Users/ak66h_000/OneDrive/webscrap/polls/aiohttpdemo_polls/templates'))


async def index(request):
    return web.Response(body=b"Hello, world")

@aiohttp_jinja2.template('detail.html')
def handler(request):
    return {'name': 'Andrew', 'surname': 'Svetlov'}

@aiohttp_jinja2.template('detail.html')
def test(request):
    data = request.post()
    mp3 = data['mp3']
    return {'name': 'Andrew', 'surname': 'Svetlov', 'mp3': mp3}

@aiohttp_jinja2.template('detail.html')
def test1(request):
    mp3 = request.match_info['mp3']
    return {'name': 'Andrew', 'surname': 'Svetlov', 'mp3': mp3}
    
@aiohttp_jinja2.template('detail.html')
def test2(request):
    mp3 = request.match_info['mp3']
    return {'mp3': mp3}
    

from urllib.parse import urlparse, parse_qsl

from aiohttp import MultiDict

class HttpRequestHandler(aiohttp.server.ServerHttpProtocol):

    async def handle_request(self, message, payload):
        response = aiohttp.Response(
            self.writer, 200, http_version=message.version
        )
        data = await payload.read()
        post_params = MultiDict(parse_qsl(data))
        print("Passed in POST", post_params)


    
web.run_app(app)