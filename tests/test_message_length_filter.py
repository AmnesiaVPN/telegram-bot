import pytest
from dataclasses import dataclass

from filters import MessageLengthFilter


@dataclass(frozen=True, slots=True)
class FakeMessage:
    text: str


TEXT_LENGTH_TO_TEXT: dict[int, str] = {
    10: 'hello word',
    55: 'Lorem ipsum dolor sit amet, consectetur adipisicing eli',
}


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'min_length,max_length,text,result',
    [
        (10, 15, TEXT_LENGTH_TO_TEXT[10], True),
        (11, 15, TEXT_LENGTH_TO_TEXT[10], False),
        (8, 9, TEXT_LENGTH_TO_TEXT[10], False),
        (8, 10, TEXT_LENGTH_TO_TEXT[10], True),
        (53, 54, TEXT_LENGTH_TO_TEXT[55], False),
        (53, 55, TEXT_LENGTH_TO_TEXT[55], True),
        (55, 58, TEXT_LENGTH_TO_TEXT[55], True),
        (56, 58, TEXT_LENGTH_TO_TEXT[55], False),
    ]
)
async def test_message_length_filter(min_length, max_length, text, result):
    message = FakeMessage(text=text)
    assert await MessageLengthFilter(min_length=min_length, max_length=max_length).check(message) == result
