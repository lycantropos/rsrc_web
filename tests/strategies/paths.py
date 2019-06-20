from functools import partial
from operator import add
from string import (ascii_letters,
                    digits)
from urllib.parse import urlencode

from hypothesis import strategies
from rsrc.models import URL

from tests.utils import URL_SEPARATOR

web_url_schemes = strategies.sampled_from(['http', 'https'])
urls_parts = strategies.text(strategies.sampled_from(ascii_letters + digits),
                             min_size=1)
url_parameters_strings = (strategies.dictionaries(urls_parts, urls_parts)
                          .map(urlencode))
url_path_strings = (strategies.lists(urls_parts,
                                     max_size=10)
                    .map(URL_SEPARATOR.join)
                    .map(partial(add, URL_SEPARATOR)))
web_url_strings = (strategies.builds(URL,
                                     web_url_schemes,
                                     urls_parts,
                                     url_path_strings,
                                     url_parameters_strings,
                                     url_parameters_strings,
                                     urls_parts)
                   .map(str))
base_readable_web_url = URL.from_string('https://postman-echo.com/get')
base_writeable_web_url = URL.from_string('https://postman-echo.com/post')
readable_web_url_strings = (strategies.builds(base_readable_web_url._replace,
                                              query=url_parameters_strings)
                            .map(str))
writeable_web_url_strings = (strategies.builds(base_writeable_web_url._replace,
                                               query=url_parameters_strings)
                             .map(str))
