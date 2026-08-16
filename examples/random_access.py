"""Random access: fetch single chunks or a range without splitting everything."""

from chunkerlib import DataChunker


def main() -> None:
    data = b"abcdefghijklmnopqrstuvwxyz"
    chunker = DataChunker(data, chunk_size=5)

    print(f"total chunks: {chunker.number_of_chunks}")

    third = chunker.get_chunk(2)
    print(f"chunk 2: {bytes(third)}")

    first_two = [bytes(c) for _, c in chunker.get_chunk_range(0, 1)]
    print(f"chunks 0-1: {first_two}")


if __name__ == "__main__":
    main()
