import re

with open('data/01_regex.txt') as input_file:
    text = input_file.read()
    # (?>\+2)?\d{11}
    result = re.finditer(r'(\+2)?(\d{11})',text,re.MULTILINE)
    for match_idx, match in enumerate(result, start=1):
        groups = match.groups()
        if len(match.groups()) == 2 and None not in groups:
            print(f"Match #{match_idx} has code")
        print(f"Match #{match_idx} {str(groups[1])}")
        