from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import add_messages


class State(TypedDict):
    "Represents the structure of the state used in the graph."

    messages: Annotated[list, add_messages]
