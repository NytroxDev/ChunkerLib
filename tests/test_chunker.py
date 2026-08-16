"""Tests for datachunker.chunker."""

import pytest

from datachunker import DataChunker


class TestInit:
    def test_accepts_bytes(self):
        chunker = DataChunker(b"abc", chunk_size=2)
        assert chunker.number_of_chunks == 2

    def test_accepts_memoryview(self):
        data = memoryview(b"abcd")
        chunker = DataChunker(data, chunk_size=2)
        assert chunker.number_of_chunks == 2

    def test_rejects_zero_chunk_size(self):
        with pytest.raises(ValueError):
            DataChunker(b"abc", chunk_size=0)

    def test_rejects_negative_chunk_size(self):
        with pytest.raises(ValueError):
            DataChunker(b"abc", chunk_size=-1)


class TestSplit:
    def test_splits_into_fixed_chunks(self):
        chunker = DataChunker(b"abcdef", chunk_size=2)
        chunks = [bytes(chunk) for _, chunk in chunker.split()]
        assert chunks == [b"ab", b"cd", b"ef"]

    def test_last_chunk_can_be_short(self):
        chunker = DataChunker(b"abcde", chunk_size=2)
        chunks = [bytes(chunk) for _, chunk in chunker.split()]
        assert chunks == [b"ab", b"cd", b"e"]

    def test_chunk_ids_are_zero_based(self):
        chunker = DataChunker(b"abcd", chunk_size=2)
        ids = [chunk_id for chunk_id, _ in chunker.split()]
        assert ids == [0, 1]

    def test_empty_data_yields_nothing(self):
        chunker = DataChunker(b"", chunk_size=2)
        assert list(chunker.split()) == []

    def test_chunk_size_bigger_than_data(self):
        chunker = DataChunker(b"abc", chunk_size=16)
        chunks = [bytes(chunk) for _, chunk in chunker.split()]
        assert chunks == [b"abc"]


class TestNumberOfChunks:
    def test_exact_multiple(self):
        assert DataChunker(b"abcd", chunk_size=2).number_of_chunks == 2

    def test_remainder_rounds_up(self):
        assert DataChunker(b"abcde", chunk_size=2).number_of_chunks == 3

    def test_single_chunk(self):
        assert DataChunker(b"abc", chunk_size=100).number_of_chunks == 1

    def test_empty_data(self):
        assert DataChunker(b"", chunk_size=2).number_of_chunks == 0

    def test_chunk_size_one(self):
        assert DataChunker(b"abc", chunk_size=1).number_of_chunks == 3


class TestGetChunk:
    def test_returns_expected_chunk(self):
        chunker = DataChunker(b"abcdef", chunk_size=2)
        assert bytes(chunker.get_chunk(0)) == b"ab"
        assert bytes(chunker.get_chunk(2)) == b"ef"

    def test_invalid_id_raises(self):
        chunker = DataChunker(b"abcd", chunk_size=2)
        with pytest.raises(ValueError):
            chunker.get_chunk(2)
        with pytest.raises(ValueError):
            chunker.get_chunk(-1)


class TestGetChunkRange:
    def test_returns_expected_range(self):
        chunker = DataChunker(b"abcdef", chunk_size=2)
        chunks = [bytes(chunk) for _, chunk in chunker.get_chunk_range(1, 2)]
        assert chunks == [b"cd", b"ef"]

    def test_single_element_range(self):
        chunker = DataChunker(b"abcdef", chunk_size=2)
        chunks = [bytes(chunk) for _, chunk in chunker.get_chunk_range(1, 1)]
        assert chunks == [b"cd"]

    def test_reversed_bounds_raise(self):
        chunker = DataChunker(b"abcdef", chunk_size=2)
        with pytest.raises(ValueError):
            list(chunker.get_chunk_range(2, 1))

    def test_out_of_range_bounds_raise(self):
        chunker = DataChunker(b"abcd", chunk_size=2)
        with pytest.raises(ValueError):
            list(chunker.get_chunk_range(0, 2))
        with pytest.raises(ValueError):
            list(chunker.get_chunk_range(2, 2))


class TestRoundTrip:
    def test_split_then_reassemble(self):
        data = bytes(range(256)) * 4
        chunker = DataChunker(data, chunk_size=7)
        reassembled = b"".join(bytes(chunk) for _, chunk in chunker.split())
        assert reassembled == data

    def test_memoryview_no_copy(self):
        data = b"abcdef"
        chunker = DataChunker(data, chunk_size=2)
        assert chunker.get_chunk(0).nbytes == 2
        assert bytes(chunker.get_chunk(1)) == b"cd"
