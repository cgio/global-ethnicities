"""Upon success, generate ipums.txt and exit via sys.exit(0)."""

import json
import re
import sys
from html.parser import HTMLParser
import requests
from requests.exceptions import HTTPError

FILE_OUTPUT = 'ipums.txt'

exclude = (
    'Mixture',
    'Uncodable',
    'Not Classified',
    'Other',
    'Not Reported',
    'American/United States'  # Unnecessary, as American is included
)


def finalize(ethnicities):
    """Final cleanup and then file output."""
    # Remove ", n.e.c."
    ethnicities = [e.replace(', n.e.c.', '') for e in ethnicities]
    # Example: splits "Bosnian  Herzegovinian" into two ethnicities
    for i, e in enumerate(ethnicities):
        if '  ' in e:
            del ethnicities[i]
            ethnicities.extend(e.split('  '))
    # Improve readability
    ethnicities = [e.replace(' ; ', '/') for e in ethnicities]
    ethnicities = [e.replace(', ', '/') for e in ethnicities]
    # Remove any trailing colons
    ethnicities = [e for e in ethnicities if e[-1:] != ':']
    # Remove duplicates
    ethnicities = list(set(ethnicities))
    # Remove exclusions
    ethnicities = list(set(ethnicities) - set(exclude))
    # Alphabetize
    ethnicities.sort()
    with open(FILE_OUTPUT, 'w') as f:
        for e in ethnicities:
            f.write(f'{e}\n')
    print(f'Success: wrote {FILE_OUTPUT}')


def main():
    """Get ethnicities and write them to disk."""
    ethnicities = []
    remote_url = 'https://usa.ipums.org/usa-action/variables/' \
                 'ANCESTR1#codes_section'
    remote_html = None

    try:
        remote_html = requests.get(remote_url)
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as err:
        print(f'Other error: {err}')

    parser = DataParser()
    parser.feed(remote_html.text)

    try:
        remote_json = json.loads('[' + parser.data + ']')
    except json.decoder.JSONDecodeError:
        sys.exit('Error: invalid JSON')

    del parser

    for e in remote_json:
        if not e.get('code'):
            continue
        if not e.get('label'):
            continue
        ethnicity = re.sub(r'\([^)]*\)', '', e.get('label'))
        ethnicities.append(ethnicity.strip())

    del remote_json

    if ethnicities:
        finalize(ethnicities)
        # Success
        sys.exit(0)


class DataParser(HTMLParser):
    """Parses chunks of remote_url's web page code."""
    data = None

    def handle_data(self, data):
        if 'jsonPath: "/usa-action/frequencies/ANCESTR1"' in data:
            data_start_str = 'categories: ['
            data_end_str = '}]'
            data_start = data.find(data_start_str)
            data_end = data.find(data_end_str, data_start + len(data_start_str))
            if data_start and data_end:
                self.data = data[data_start + len(data_start_str):data_end + 1]
            else:
                print('Error DataParser.handle_data: invalid data')

    def error(self, message):
        print('Error DataParser.error: unexpected')


if __name__ == '__main__':
    main()
