"""Gets the version, either installed or dynamically."""

# type: ignore


__all__ = ["__version__"]


try:
    from setuptools_scm import get_version

    __version__ = get_version(root="../..", relative_to=__file__)
except Exception:
    try:
        from importlib.metadata import PackageNotFoundError, version  # noqa  # type: ignore
    except ImportError:
        from importlib_metadata import PackageNotFoundError, version  # noqa  # type: ignore

    try:
        __version__ = version("pydantic_yaml")
    except PackageNotFoundError:  # type: ignore
        __version__ = "0.0.0"
