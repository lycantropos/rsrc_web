from hypothesis import given

from rsrc_web.models import WebStream
from tests import strategies
from tests.utils import (URL_SEPARATOR,
                         implication)


@given(strategies.web_streams)
def test_top_level_resource(web_stream: WebStream) -> None:
    top_level_resource = web_stream.from_string(str(web_stream.url
                                                    .join(URL_SEPARATOR)))

    assert implication(web_stream.exists(), top_level_resource.exists())
