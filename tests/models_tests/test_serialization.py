from hypothesis import given
from rsrc.models import Resource

from tests import strategies


@given(strategies.web_streams)
def test_round_trip(resource: Resource) -> None:
    assert resource.from_string(str(resource)) == resource
