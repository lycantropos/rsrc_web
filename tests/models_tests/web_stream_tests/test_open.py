from collections import abc

from hypothesis import given

from rsrc_web.models import WebStream
from tests import strategies


@given(strategies.readable_web_streams, strategies.booleans)
def test_basic(web_stream: WebStream, binary_mode: bool) -> None:
    result = web_stream.open(binary_mode=binary_mode)

    assert isinstance(result, abc.Iterable)
    assert all(isinstance(line, bytes if binary_mode else str)
               for line in result)
