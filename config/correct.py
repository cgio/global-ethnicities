"""Ethnicities to correct.


Example:
    The IPUMS database erroneously contains "Zanzibar Islande" rather than
    "Zanzibar Islander". FYI IPUMS was notified of this error on May 3, 2019.

"""

correct = {
    'African-American': 'African American',
    'Asian Indian/Indian (Asia)': 'Asian Indian',
    'St Lucia Islander': 'St. Lucia Islander',
    'U.S. Trust Terr of the Pacific': 'Trust Territory of the Pacific '
                                              'Islands',
    'Udmert': 'Udmurt',
    'Zanzibar Islande': 'Zanzibar Islander',
}
