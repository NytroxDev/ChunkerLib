# DataChunker

[![PyPI version](https://img.shields.io/pypi/v/datachunker.svg)](https://pypi.org/project/datachunker/)
[![Python versions](https://img.shields.io/pypi/pyversions/datachunker.svg)](https://pypi.org/project/datachunker/)
[![License](https://img.shields.io/github/license/NytroxDev/datachunker.svg)](https://github.com/NytroxDev/datachunker)
[![CI](https://img.shields.io/github/actions/workflow/status/NytroxDev/datachunker/ci.yml)](https://github.com/NytroxDev/datachunker/actions)

Split binary data into fixed-size chunks. Zero dependencies, fully typed, works with any file size thanks to memory views.

## Installation

```bash
pip install datachunker
```

## Quick start

```python
from datachunker import DataChunker

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
