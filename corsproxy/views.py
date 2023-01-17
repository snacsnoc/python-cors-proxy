import urllib.request as req
import urllib.parse as parse
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.cache import cache_page

# Set cache to 60 mins
@cache_page(60 * 60)
def index(request):
    if not request.GET:
        return HttpResponse("No URL supplied", status=400)
    if not request.GET.get("url"):
        return HttpResponse("Parameter not specified", status=400)
    if request.method != "GET":
        return HttpResponse("This endpoint only accepts GET requests", status=405)

    url = parse.quote(request.GET.get("url"))
    url = url.replace("%3A", ":")
    url = url.replace("%3F", "?")
    url = url.replace("%3D", "=")

    host = request.META.get("HTTP_ORIGIN")
    if host not in settings.ALLOWED_ORIGINS:
        return HttpResponse("Invalid origin: "+ host, status=403)

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Firefox/106.0.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "application/gzip",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
    }

    try:
        remote_request = req.Request(url, None, headers)
        with req.urlopen(remote_request) as response:
            content = response.read()
    except req.HTTPError as err:
        return HttpResponse("HTTP ERROR " + url, status=err.code)
    except req.URLError as err:
        return HttpResponse('URL ERROR ' + url, status=500)
    except:
        return HttpResponse("REQUEST ERROR " + url, status=500)
    return HttpResponse(content, status=200)
