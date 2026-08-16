# v0.1.0 : Initial public release

First public release of ChunkerLib, a zero-dependency library for splitting binary
data into fixed-size chunks.

## Added

- `DataChunker`: splits `bytes` and `memoryview` data into fixed-size chunks with
  no data copy, safe for arbitrarily large files.
- `DataChunker.split()`: iterate over every chunk with its zero-based chunk ID.
- `DataChunker.get_chunk(chunk_id)`: direct random access to a single chunk.
- `DataChunker.get_chunk_range(start_chunk_id, end_chunk_id)`: iterate over a
  slice of chunks without materializing them.
- `DataChunker.number_of_chunks`: total chunk count.
- Full type hints with `py.typed`, Python 3.9+ support, zero runtime dependencies.

## Docs

- README with quick start, DOCUMENTATION.md with the complete API reference, and
  three runnable examples in `examples/`.

## Tests

- 22 unit tests passing across Python 3.9, 3.12 and 3.14: splitting, random access,
  bounds validation and round-trip reassembly.
- CI running ruff, mypy, build check and the test matrix on every push.

See CHANGELOG.md for the full list of changes.
