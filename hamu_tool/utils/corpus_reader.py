"""This module defines a CorpusReader class for efficient access to documents in a corpus using an index.
The CorpusReader uses memory-mapped file support for random access to large files or streams.
This module is compatible with Python 3.8 and above due to the use of the '|' (pipe) operator for type hinting.
The CorpusReader class provides methods to:
- Initialize the corpus reader using a pre-built index file.
- Fetch a document by its ID or index in dict format or raw string format.
- Return the number of documents in the corpus.
- Check if a given index or ID is in the corpus.
- Return a string representation of the corpus reader.
- Return an iterator for the corpus reader.
- Convert given data into string representation.
- Build an index file for a given data file.
"""

import datetime
import json
import mmap
import os
import unidecode

class CorpusReader:
    """A reader for efficiently accessing documents in a corpus using an index.
    """
    def __init__(self, index_path : str):
        """Initialize the corpus reader using an pre-built index file.

        Args:
            index_path (str): Path of the pre-built index file.
        """
        self.index = {}
        self.idx_list = []
        self.idx_set = set()
        self.data_offset = 0
        self.index_path = index_path
        if not os.path.exists(self.index_path):
            raise FileNotFoundError(f'Index file not found: [{self.index_path}]')
        self.index_file_size = os.path.getsize(self.index_path)
        with open(f'{self.index_path}', 'r', encoding='utf-8') as fp:
            for line in fp:
                self.data_offset += len(line)
                idx, start_idx, end_idx = line.strip().split('\t')
                if (idx, start_idx, end_idx) == ('0', '0', '0'):
                    break
                self.index[idx] = {'start': int(start_idx), 'end': int(end_idx)}
                self.idx_list.append(idx)
                self.idx_set.add(idx)
        self.fp = open(f'{self.index_path}', 'r+b')
        self.mm = mmap.mmap(self.fp.fileno(), 0)

    def __del__(self):
        """Clean up resources.
        """
        self.mm.close()
        self.fp.close()

    def __getitem__(self, index : int | str) -> dict:
        """Fetch a document by its ID (str) or index (int) in dict format.

        Args:
            index (int | str): The ID (str) or index (int) of the document.

        Returns:
            dict: The fetched document in dict format.
        """
        idx = self.idx_list[index] if isinstance(index, int) else index
        if not self.__contain__(idx):
            raise KeyError(f'Index or ID not found: [{idx}]')
        start_idx = self.data_offset+self.index[idx]['start']
        end_idx = self.data_offset+self.index[idx]['end']
        doc = self.mm[start_idx:end_idx]
        doc = doc.decode()
        doc = json.loads(doc)
        return doc

    def raw(self, index : int | str) -> str:
        """Fetch a document by its ID (str) or index (int) in raw string format.

        Args:
            index (int | str): The ID (str) or index (int) of the document.

        Returns:
            str: The fetched document in raw string format.
        """
        idx = self.idx_list[index] if isinstance(index, int) else index
        if not self.__contain__(idx):
            raise KeyError(f'Index or ID not found: [{idx}]')
        start_idx = self.data_offset+self.index[idx]['start']
        end_idx = self.data_offset+self.index[idx]['end']
        doc = self.mm[start_idx:end_idx]
        doc = doc.decode()
        return doc

    def __len__(self) -> int:
        """Return the number of documents in the corpus.

        Returns:
            int: Number of documents in the corpus.
        """
        return len(self.idx_list)

    def __contain__(self, index : int | str) -> bool:
        """Check if the given index (int) or ID (str) is in the corpus.

        Args:
            index (int | str): The ID (str) or index (int) of the document.

        Returns:
            bool: Whether the given index or ID is in the corpus or not.
        """
        return index in self.idx_set

    def __str__(self):
        """Return the string representation of the corpus reader.

        Returns:
            str: String representation of the corpus reader.
        """
        index_file_size = os.path.getsize(self.index_path)
        unit = 'B'
        for current_unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if index_file_size < 1024:
                break
            index_file_size /= 1024
            unit = current_unit
        return f"CorpusReader(index_path='{self.index_path}')\n- number of documents: {len(self)}\n- index file size: {index_file_size:.1f} {unit}"

    def __repr__(self):
        """Return the string representation of the corpus reader.

        Returns:
            str: String representation of the corpus reader.
        """
        return f"CorpusReader('{self.index_path}')"

    def __iter__(self):
        """Return an iterator for the corpus reader.

        Returns:
            iter: An iterator for the corpus reader.
        """
        for idx in self.idx_list:
            yield self[idx]

    @staticmethod
    def to_str(data : any) -> str:
        """Convert the given data into string representation.

        Args:
            data (any): Data to convert.

        Returns:
            str: String converted version of the given data.
        """
        if isinstance(data, str):
            return data
        data = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
        return data

    @staticmethod
    def build_index(data_path : str, index_path : str, idx_field : str = 'id', verbose : bool = False):
        """Build an index file for the given data file.

        Args:
            data_path (str): Path of the data file (jsonl type).
            index_path (str): Path of the index file to be created.
            idx_field (str): Field of the data file to be used as the ID (str) of the documents. Defaults to 'id'.
            verbose (bool, optional): Wheather to print the progress status or not. Defaults to False.
        """
        # Create index and data files
        with open(f'{index_path}', 'w', encoding='utf-8', newline='\n') as fp_idx, \
            open(f'{index_path}.data', 'w', encoding='utf-8', newline='\n') as fp_data, \
            open(data_path, 'r', encoding='utf-8') as fp:
            file_name = data_path.split('/')[-1]
            cnt = 0
            cnt_doc = 0
            for line in fp:
                data_pre = json.loads(line)
                data = {}
                for key_pre in data_pre:
                    key = unidecode.unidecode(key_pre)
                    value = unidecode.unidecode(data_pre[key_pre])
                    data[key] = value
                idx_field = unidecode.unidecode(idx_field)
                idx = data[idx_field]
                content = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
                fp_data.write(content)
                fp_idx.write(f'{idx}\t{cnt}\t{cnt + len(content)}\n')
                cnt += len(content)
                cnt_doc += 1
                if verbose and cnt_doc % 1000 == 0:
                    now = datetime.datetime.now().strftime('%H:%M:%S')
                    print(f'[ {now} ] Corpus Reader | file: {file_name} | reading documents | doc: {cnt_doc:,} |', end='\r', flush=True)
            if verbose:
                now = datetime.datetime.now().strftime('%H:%M:%S')
                print(f'[ {now} ] Corpus Reader | file: {file_name} | reading documents | doc: {cnt_doc:,} |', flush=True)
            fp_idx.write('0\t0\t0\n')

        # Merge index and data files into one
        with open(f'{index_path}', 'a', encoding='utf-8') as fp_idx, open(f'{index_path}.data', 'r', encoding='utf-8') as fp_data:
            for line in fp_data:
                fp_idx.write(line)
                if verbose and cnt_doc % 1000 == 0:
                    now = datetime.datetime.now().strftime('%H:%M:%S')
                    print(f'[ {now} ] Corpus Reader | file: {file_name} | merging index |', end='\r', flush=True)
            if verbose:
                now = datetime.datetime.now().strftime('%H:%M:%S')
                print(f'[ {now} ] Corpus Reader | file: {file_name} | merging index |', flush=True)
        os.remove(f'{index_path}.data')
