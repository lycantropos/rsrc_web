from hypothesis import given
from rsrc.models import Resource

from tests import strategies
from tests.utils import implication


@given(strategies.web_streams)
def test_reflexivity(resource: Resource) -> None:
    assert resource == resource


@given(strategies.web_streams, strategies.web_streams)
def test_symmetry(left_resource: Resource, right_resource: Resource) -> None:
    assert implication(left_resource == right_resource,
                       right_resource == left_resource)


@given(strategies.web_streams, strategies.web_streams, strategies.web_streams)
def test_transitivity(left_resource: Resource,
                      mid_resource: Resource,
                      right_resource: Resource) -> None:
    assert implication(left_resource == mid_resource
                       and mid_resource == right_resource,
                       left_resource == right_resource)
