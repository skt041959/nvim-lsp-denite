from typing import Any, Dict, List, Optional

LspResponseEntry = Dict[str, Any]


class LspResponse:
    def __init__(self, response: List[LspResponseEntry]) -> None:
        self._response = response

    @property
    def result(self) -> List[LspResponseEntry]:
        return self._response.get("result", [])

    @property
    def is_error(self):
        return "error" in self._response

    @property
    def error_message(self) -> Optional[str]:
        if self.is_error:
            error = self._response.get("error", {})
            return error.get("message", None)
        else:
            return None
