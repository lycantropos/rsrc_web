from hypothesis import given

from rsrc_web.models import WebStream
from tests import strategies


@given(strategies.writeable_web_streams, strategies.readable_web_streams)
def test_basic(destination: WebStream, source: WebStream) -> None:
    result = destination.receive(source)

    assert result is None
