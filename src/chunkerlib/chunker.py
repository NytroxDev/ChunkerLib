from collections.abc import Generator
from typing import Union


class DataChunker:
    """Splits binary data into fixed-size chunks."""

    def __init__(self, file_data: Union[bytes, memoryview], chunk_size: int):
        """Initialize a DataChunker.

        Args:
            file_data: File data to split into chunks.
            chunk_size: Size of each chunk in bytes.

        Raises:
            ValueError: If chunk_size is less than or equal to 0.
        """
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

        self.chunk_size = chunk_size
        self.data: memoryview[int] = (
            memoryview(file_data) if not isinstance(file_data, memoryview) else file_data
        )

    def split(self) -> Generator[tuple[int, memoryview[int]], None, None]:
        """Split the file data into chunks.

        Yields:
            Each chunk from the data, along with its chunk ID.
        """
        offset = 0
        chunk_id = 0
        while offset < len(self.data):
            yield chunk_id, self.data[offset : offset + self.chunk_size]
            offset += self.chunk_size
            chunk_id += 1

    def _validate_chunk_id(self, chunk_id: int) -> None:
        if not 0 <= chunk_id < self.number_of_chunks:
            raise ValueError(f"Invalid chunk ID: {chunk_id}")

    def get_chunk(self, chunk_id: int) -> memoryview[int]:
        """Get a specific chunk from the file data.

        Args:
            chunk_id: ID of the chunk to extract.

        Returns:
            The content of the requested chunk.

        Raises:
            ValueError: If a chunk ID is invalid.
        """
        self._validate_chunk_id(chunk_id)

        return self.data[chunk_id * self.chunk_size : (chunk_id + 1) * self.chunk_size]

    def get_chunk_range(
        self,
        start_chunk_id: int,
        end_chunk_id: int,
    ) -> Generator[tuple[int, memoryview[int]], None, None]:
        """Get a range of chunks from the file data.

        Args:
            start_chunk_id: ID of the first chunk to get.
            end_chunk_id: ID of the last chunk to get (inclusive).

        Yields:
            Each chunk in the specified range, along with its ID.

        Raises:
            ValueError: If a chunk ID is invalid.
        """
        self._validate_chunk_id(start_chunk_id)
        self._validate_chunk_id(end_chunk_id)

        if end_chunk_id < start_chunk_id:
            raise ValueError("end_chunk_id must be greater than or equal to start_chunk_id")

        for chunk_id in range(start_chunk_id, end_chunk_id + 1):
            yield chunk_id, self.get_chunk(chunk_id)

    @property
    def number_of_chunks(self) -> int:
        """Return the number of chunks in the file data."""
        length = len(self.data) // self.chunk_size
        if len(self.data) % self.chunk_size:
            return length + 1
        return length
