"""Basic usage: split data into chunks and reassemble it."""

from chunkerlib import DataChunker


def main() -> None:
    data = bytes(range(256)) * 4
    chunk_size = 7

    chunker = DataChunker(data, chunk_size)

    chunks = []
    for chunk_id, chunk in chunker.split():
        print(f"chunk {chunk_id}: {len(chunk)} bytes")
        chunks.append(chunk)

    reassembled = b"".join(bytes(chunk) for chunk in chunks)

    assert reassembled == data
    print(f"reassembled {len(reassembled)} bytes in {chunker.number_of_chunks} chunks")


if __name__ == "__main__":
    main()
