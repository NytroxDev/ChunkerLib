# DataChunker

[![PyPI version](https://img.shields.io/pypi/v/chunkerlib.svg)](https://pypi.org/project/chunkerlib/)
[![Python versions](https://img.shields.io/pypi/pyversions/chunkerlib.svg)](https://pypi.org/project/chunkerlib/)
[![License](https://img.shields.io/github/license/NytroxDev/DataChunker.svg)](https://github.com/NytroxDev/DataChunker)
[![CI](https://img.shields.io/github/actions/workflow/status/NytroxDev/DataChunker/ci.yml)](https://github.com/NytroxDev/DataChunker/actions)

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
- Static typed, compatible with Python 3.9+

## Documentation

See [DOCUMENTATION.md](DOCUMENTATION.md) for the full API reference.

## License

[MIT](LICENSE)
