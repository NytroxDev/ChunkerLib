# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-08-16

### Added

- **`DataChunker`**: splits `bytes` and `memoryview` data into fixed-size chunks
  without copying the data.
- **`DataChunker.split()`**: iterate over every chunk of the data along with its
  zero-based chunk ID.
- **`DataChunker.get_chunk(chunk_id)`**: random access to a single chunk.
- **`DataChunker.get_chunk_range(start, end)`**: iterate over a slice of chunks.
- **`DataChunker.number_of_chunks`**: total chunk count, `ceil(len(data) / chunk_size)`.
- **Zero runtime dependencies**, fully typed with `py.typed`.
- **Packaging**: src layout with hatchling, Python 3.9+ support.
- **Tests**: 22 unit tests covering splitting, random access, bounds validation
  and round-trip reassembly.
- **CI**: lint, type checking, version check, build check and test matrix across
  Python 3.9, 3.12 and 3.14.
- **Publishing**: GitHub Actions workflow with trusted publishing to PyPI and
  test.pypi.org.
- **Documentation**: README, full API reference in DOCUMENTATION.md and three
  runnable examples in `examples/`.
