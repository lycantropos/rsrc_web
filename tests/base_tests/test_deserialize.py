from hypothesis import given

from rsrc_web.base import deserialize
from rsrc_web.models import WebStream
from tests import strategies


@given(strategies.web_url_strings)
def test_basic(string: str) -> None:
    result = deserialize(string)

    assert isinstance(result, WebStream)
