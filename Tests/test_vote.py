import pytest

from Tests.vote import vote


@pytest.mark.parametrize("votes, expected", [
    ([1, 1, 1, 2, 3], 1),
    ([1, 2, 3, 2, 2], 2),
    ([1, 1, 2, 2, 3], 1),
    ([3, 3, 3, 2, 2, 1], 3),
])
def test_vote(votes, expected):
    assert vote(votes) == expected
