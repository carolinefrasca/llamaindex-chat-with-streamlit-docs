from typing import Any, Dict, List, Optional

from llama_index.callbacks.base import BaseCallbackHandler
from llama_index.callbacks.schema import CBEventType
import streamlit as st

class StreamlitRetrievalHandler(BaseCallbackHandler):
    """Callback handler for writing retrieval results to Streamlit."""

    def __init__(
        self,
        container = None,
        event_starts_to_ignore: Optional[List[CBEventType]] = None,
        event_ends_to_ignore: Optional[List[CBEventType]] = None,
        verbose: bool = False,
    ) -> None:
        self._container = container

        super().__init__(
            event_starts_to_ignore=event_starts_to_ignore or [],
            event_ends_to_ignore=event_ends_to_ignore or [],
        )

    def set_container(self, container):
        self._container = container

    def start_trace(self, trace_id: Optional[str] = None) -> None:
        return

    def end_trace(
        self,
        trace_id: Optional[str] = None,
        trace_map: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        return

    def on_event_start(
        self,
        event_type: CBEventType,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        **kwargs: Any,
    ) -> str:
        if (
            event_type in (CBEventType.QUERY)
            and event_type not in self.event_starts_to_ignore
            and payload is not None
        ):
            self._results = st.status("Gathering context")
        return event_id

    def on_event_end(
        self,
        event_type: CBEventType,
        payload: Optional[Dict[str, Any]] = None,
        event_id: str = "",
        **kwargs: Any,
    ) -> None:
        if (
            event_type in (CBEventType.RETRIEVE)
            and event_type not in self.event_ends_to_ignore
            and payload is not None
        ):
            for idx, node in enumerate(payload["nodes"]):
                self._results.write(f"**Node {idx}: Score: {node.score}**")
                self._results.write(node.node.text)
            self._results.update(state="complete")
