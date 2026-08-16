# DataChunker documentation

## DataChunker

Split binary data into fixed-size chunks.

```python
DataChunker(file_data: Union[bytes, memoryview], chunk_size: int)
```

### Arguments

| Argument    | Type                        | Description                                     |
| ----------- | --------------------------- | ----------------------------------------------- |
| `file_data` | `bytes` or `memoryview`     | The data to split into chunks.                  |
| `chunk_size`| `int`                       | Size of each chunk in bytes, must be > 0.       |

Raises `ValueError` if `chunk_size` is less than or equal to 0.

The data is wrapped in a `memoryview`, so no copy is made. Mutating the chunks
also mutates the original data.

### Methods

#### `split()`

```python
def split(self) -> Generator[tuple[int, memoryview[int]], None, None]
```

Yield every chunk of the data along with its chunk ID.

```python
for chunk_id, chunk in chunker.split():
    ...
```

#### `get_chunk(chunk_id)`

```python
def get_chunk(self, chunk_id: int) -> memoryview[int]
```

Return the chunk at the given ID. Raises `ValueError` if the ID is out of range.

#### `get_chunk_range(start_chunk_id, end_chunk_id)`

```python
def get_chunk_range(
    self,
    start_chunk_id: int,
    end_chunk_id: int,
) -> Generator[tuple[int, memoryview[int]], None, None]
```

Yield each chunk in the range, both bounds included. Raises `ValueError` if a
chunk ID is out of range, or if `end_chunk_id` is lower than `start_chunk_id`.

### Properties

#### `number_of_chunks`

Return the total number of chunks. This is `ceil(len(data) / chunk_size)`.

## Example

```python
from datachunker import DataChunker

data = bytes(range(10))
chunker = DataChunker(data, chunk_size=3)

assert chunker.number_of_chunks == 4

# Random access
first = bytes(chunker.get_chunk(0))       # b"\x00\x01\x02"
last = bytes(chunker.get_chunk(3))        # b"\t"

# Range access
middle = [bytes(c) for _, c in chunker.get_chunk_range(1, 2)]
# [b"\x03\x04\x05", b"\x06\x07\x08"]

# The last chunk is always shorter than chunk_size when
# the data length is not a multiple of chunk_size
```

## Notes

- Chunk IDs are zero-based.
- The last chunk may be shorter than `chunk_size`.
- Chunks are `memoryview` objects; use `bytes(chunk)` to copy the data.
