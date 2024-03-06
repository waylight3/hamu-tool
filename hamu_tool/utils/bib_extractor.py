class BIBExtractor:
    """Class to extract and parse BIB entries from a .bib file.
    """
    # Mapping of LaTeX special characters to their Unicode counterparts
    latex_unicode_mapping = {
        '\"a': 'ä', '\"o': 'ö', '\"u': 'ü', '\"A': 'Ä', '\"O': 'Ö', '\"U': 'Ü',
        '\'a': 'á', '\'e': 'é', '\'i': 'í', '\'o': 'ó', '\'u': 'ú', '\'A': 'Á', '\'E': 'É', '\'I': 'Í', '\'O': 'Ó', '\'U': 'Ú',
        '`a': 'à', '`e': 'è', '`i': 'ì', '`o': 'ò', '`u': 'ù', '`A': 'À', '`E': 'È', '`I': 'Ì', '`O': 'Ò', '`U': 'Ù',
        '^a': 'â', '^e': 'ê', '^i': 'î', '^o': 'ô', '^u': 'û', '^A': 'Â', '^E': 'Ê', '^I': 'Î', '^O': 'Ô', '^U': 'Û',
        '~n': 'ñ', '~N': 'Ñ', 'cC': 'Ç', 'cç': 'ç',
    }

    def __init__(self, path : str):
        """Constructor for BIBExtractor

        Args:
            path (str): Path to the .bib file to extract entries from.
        """
        # Initialize an empty list to store entries
        self.entries = []
        # Import entries from a .bib file specified by the path
        self.import_from_bib(path)

    def import_from_bib(self, path : str):
        """Import BIB entries from a .bib file

        Args:
            path (str): Path to the .bib file to import entries from.
        """
        # Flags for state within the file parsing
        is_inside = False  # Flag to check if currently inside a BIB entry
        current_entry_inside = []  # Buffer to store characters of the current entry
        inside_quote = False  # Flag to check if currently inside quotes
        inside_depth = 0  # Nested depth for braces

        with open(path, 'r', encoding='utf-8') as fp:  # Open the .bib file
            for line in fp:  # Iterate through each line
                line = line.lstrip()  # Strip leading whitespace
                if line.startswith('%') or not line:  # Ignore comment and blank lines
                    continue
                for ch in line:  # Iterate through each character
                    # Toggle the inside_quote flag when encountering a quote not preceded by a backslash
                    if ch == '"' and current_entry_inside[-1] != '\\':
                        inside_quote = not inside_quote
                    # Begin a new entry upon encountering '@' outside quotes
                    if ch == '@' and not inside_quote:
                        is_inside = True
                        continue
                    # Increase depth upon encountering '{' outside quotes
                    if ch == '{' and not inside_quote:
                        inside_depth += 1
                    # Decrease depth upon encountering '}' outside quotes
                    if ch == '}' and not inside_quote:
                        inside_depth -= 1
                        # If depth returns to 0, end of entry is reached
                        if inside_depth == 0:
                            is_inside = False
                            # Process and clean the entry, then add to the list
                            current_entry_raw = ' '.join(''.join(current_entry_inside).split())
                            etype, current_entry_raw = current_entry_raw.split('{', 1)
                            current_entry = self._parse_entry_from_raw(current_entry_raw)
                            current_entry['type'] = etype.strip()
                            current_entry = self._clean_entry(current_entry)
                            self.entries.append(current_entry)
                            current_entry_inside = []  # Reset buffer for next entry
                            continue
                    # If inside an entry, add character to buffer
                    if is_inside:
                        current_entry_inside.append(ch)

    def _parse_entry_from_raw(self, raw : str) -> dict[str, str]:
        """Parse a raw entry string into a dictionary

        Args:
            raw (str): Raw entry string to parse.

        Returns:
            dict[str, str]: Parsed entry as a dictionary.
        """
        lines = self._parse_entry_from_raw_line(raw)
        entry = {'id': lines[0]}  # The first line is the ID
        for line in lines[1:]:  # Process each line after the ID
            if not line:
                continue
            key, value = line.split('=', 1)
            entry[key.strip()] = value.strip()
        return entry

    def _parse_entry_from_raw_line(self, raw : str) -> list[str]:
        """Parse lines from a raw entry string, considering nested braces and quotes

        Args:
            raw (str): Raw entry string to parse.

        Returns:
            list[str]: List of parsed lines.
        """
        lines = []
        inside_quote = False
        pivot = 0
        depth = 0
        for i in range(len(raw)):
            if raw[i] == '"' and (i == 0 or raw[i-1] != '\\'):
                inside_quote = not inside_quote
            if inside_quote:
                continue
            elif raw[i] == '{':
                depth += 1
            elif raw[i] == '}':
                depth -= 1
            elif raw[i] == ',' and depth == 0:
                lines.append(raw[pivot:i].strip())
                pivot = i + 1
        lines.append(raw[pivot:].strip())  # Add the last segment
        return lines

    def _clean_entry(self, entry : dict[str, str]) -> dict[str, str]:
        """Clean and format an entry values, including converting LaTeX to Unicode

        Args:
            entry (dict[str, str]): Entry to clean and format.

        Returns:
            dict[str, str]: Cleaned and formatted entry.
        """
        for key in entry:
            entry[key] = entry[key].strip('"{}')
            for k, v in self.latex_unicode_mapping.items():
                # Replace LaTeX encoded characters with their Unicode counterparts
                entry[key] = entry[key].replace('{\\' + k + '}', v)
                entry[key] = entry[key].replace(k, v)
            if key in ['author', 'editor']:
                # Split authors/editors into a list, removing the surrounding braces
                entry[key] = entry[key][1:-1].split(' and ')
        return entry
