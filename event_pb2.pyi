from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventRequest(_message.Message):
    __slots__ = ["eventName"]
    EVENTNAME_FIELD_NUMBER: _ClassVar[int]
    eventName: str
    def __init__(self, eventName: _Optional[str] = ...) -> None: ...

class EventReply(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...
