"""**Messages** are objects used in prompts and chat conversations.

**Class hierarchy:**

.. code-block::

    BaseMessage --> SystemMessage, AIMessage, HumanMessage, ChatMessage, FunctionMessage, ToolMessage
                --> BaseMessageChunk --> SystemMessageChunk, AIMessageChunk, HumanMessageChunk, ChatMessageChunk, FunctionMessageChunk, ToolMessageChunk

**Main helpers:**

.. code-block::

    ChatPromptTemplate

"""  # noqa: E501

from importlib import import_module

# TODO: finish up type checking

_message_types = {
    "AIMessage": "ai",
    "AIMessageChunk": "ai",
    "BaseMessage": "base",
    "BaseMessageChunk": "base",
    "ChatMessage": "chat",
    "ChatMessageChunk": "chat",
    "FunctionMessage": "function",
    "FunctionMessageChunk": "function",
    "HumanMessage": "human",
    "HumanMessageChunk": "human",
    "RemoveMessage": "modifier",
    "SystemMessage": "system",
    "SystemMessageChunk": "system",
    "ToolCall": "tool",
    "ToolCallChunk": "tool",
    "ToolMessage": "tool",
    "ToolMessageChunk": "tool",
    "InvalidToolCall": "tool",
    "AnyMessage": "utils",
    "MessageLikeRepresentation": "utils",
    "_message_from_dict": "utils",
    "convert_to_messages": "utils",
    "convert_to_openai_messages": "utils",
    "filter_messages": "utils",
    "get_buffer_string": "utils",
    "merge_message_runs": "utils",
    "message_chunk_to_message": "utils",
    "messages_from_dict": "utils",
    "messages_to_dict": "utils",
    "merge_content": "base",
    "message_to_dict": "base",
    "trim_messages": "utils",
}

__all__ = list(_message_types.keys())


def __getattr__(attr_name: str) -> object:
    if attr_name not in _message_types:
        raise AttributeError(f"module 'langchain_core.messages' has no attribute '{attr_name}'")
    
    module_name = _message_types[attr_name]
    module = import_module(f".{module_name}", package="langchain_core.messages")
    
    attr = getattr(module, attr_name)
    globals()[attr_name] = attr
    return attr


def __dir__() -> list[str]:
    return list(__all__)
