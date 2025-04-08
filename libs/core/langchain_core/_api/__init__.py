"""Helper functions for managing the LangChain API.

This module is only relevant for LangChain developers, not for users.

.. warning::

    This module and its submodules are for internal use only.  Do not use them
    in your own code.  We may change the API at any time with no warning.

"""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .beta_decorator import (
        LangChainBetaWarning,
        beta,
        suppress_langchain_beta_warning,
        surface_langchain_beta_warnings,
    )
    from .deprecation import (
        LangChainDeprecationWarning,
        deprecated,
        suppress_langchain_deprecation_warning,
        surface_langchain_deprecation_warnings,
        warn_deprecated,
    )
    from .path import as_import_path, get_relative_path

__all__ = [
    "as_import_path",
    "beta",
    "deprecated",
    "get_relative_path",
    "LangChainBetaWarning",
    "LangChainDeprecationWarning",
    "suppress_langchain_beta_warning",
    "surface_langchain_beta_warnings",
    "suppress_langchain_deprecation_warning",
    "surface_langchain_deprecation_warnings",
    "warn_deprecated",
]


_dynamic_imports: dict[str, str] = {
    "as_import_path": "path",
    "get_relative_path": "path",
    "beta": "beta_decorator",
    "LangChainBetaWarning": "beta_decorator",
    "suppress_langchain_beta_warning": "beta_decorator",
    "surface_langchain_beta_warnings": "beta_decorator",
    "deprecated": "deprecation",
    "LangChainDeprecationWarning": "deprecation",
    "suppress_langchain_deprecation_warning": "deprecation",
    "surface_langchain_deprecation_warnings": "deprecation",
    "warn_deprecated": "deprecation",
}


def __getattr__(attr_name: str) -> object:
    # Fetch the dynamic import details from the mapping
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise ImportError(
            f"cannot import name '{attr_name}' from 'langchain_core._api'"
        )

    module = import_module(f".{module_name}", package="langchain_core._api")
    result = getattr(module, attr_name)
    globals()[attr_name] = result
    return result


def __dir__() -> list[str]:
    return list(__all__)
