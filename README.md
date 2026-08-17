# ChunkerLib

[![PyPI version](https://img.shields.io/pypi/v/chunkerlib.svg?cache=0)](https://pypi.org/project/chunkerlib/)
[![Python versions](https://img.shields.io/pypi/pyversions/chunkerlib.svg?cache=0)](https://pypi.org/project/chunkerlib/)
[![License](https://img.shields.io/github/license/NytroxDev/ChunkerLib.svg?cache=0)](https://github.com/NytroxDev/ChunkerLib)
[![CI](https://img.shields.io/github/actions/workflow/status/NytroxDev/ChunkerLib/ci.yml?cache=0)](https://github.com/NytroxDev/ChunkerLib/actions)

Split binary data into fixed-size chunks. Zero dependencies, fully typed, works with any file size thanks to memory views.

## Installation

```bash
pip install chunkerlib
```

## Quick start

```python
from chunkerlib import DataChunker

data = b"some binary file content"

chunker = DataChunker(data, chunk_size=4)

for chunk_id, chunk in chunker.split():
    print(chunk_id, bytes(chunk))

print(f"{chunker.number_of_chunks} chunks")
```

## Features

- Zero runtime dependencies
- Splits `bytes` and `memoryview` without copying the data
- Random access to chunks (`get_chunk`, `get_chunk_range`)
- Static typed, compatible with Python 3.8+

## Examples

- `examples/basic_usage.py`: split data and reassemble it
- `examples/random_access.py`: fetch a single chunk or a range
- `examples/file_chunking.py`: split a file on disk into parts

## Documentation

See [DOCUMENTATION.md](DOCUMENTATION.md) for the full API reference.

## License

[MIT](LICENSE)
