"""File chunking: split a file on disk into chunks and write them back."""

from pathlib import Path

from chunkerlib import DataChunker


def main() -> None:
    source = Path(__file__).parent / "basic_usage.py"
    out_dir = Path("chunked_output")

    data = source.read_bytes()
    chunker = DataChunker(data, chunk_size=512)

    out_dir.mkdir(exist_ok=True)
    for chunk_id, chunk in chunker.split():
        (out_dir / f"part_{chunk_id:04d}").write_bytes(chunk)

    reassembled = b"".join(
        (out_dir / f"part_{chunk_id:04d}").read_bytes()
        for chunk_id in range(chunker.number_of_chunks)
    )

    assert reassembled == data
    print(f"split {source.name} into {chunker.number_of_chunks} chunks")


if __name__ == "__main__":
    main()
