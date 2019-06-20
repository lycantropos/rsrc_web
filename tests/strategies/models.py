from rsrc_web.models import WebStream
from .paths import (readable_web_url_strings,
                    web_url_strings,
                    writeable_web_url_strings)

readable_web_streams = readable_web_url_strings.map(WebStream.from_string)
writeable_web_streams = writeable_web_url_strings.map(WebStream.from_string)
existent_web_streams = readable_web_streams | writeable_web_streams
web_streams = web_url_strings.map(WebStream.from_string) | existent_web_streams
