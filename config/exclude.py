"""Ethnicities or incorrect data to exclude.

Example:
    Your organization may not consider state names to be ethnicities though
    they are included as such in the U.S. Census data. Alternatively, some
    ethnicities share multiple names and we can further consolidate the list
    using exclusions.

"""

exclude = (
    'Reserved Codes',  # Invalid
    'Nonwhite'  # Nondescript
    'Not Hispanic or Latino',  # Nondescript
    'Part Hawaiian',  # Nondescript
    'Part Samoan',  # Nondescript
    'Some other race in combination with one or more other races',  # Nondescript
    'Negro',  # Consesus
    'Other Arab',  # Arab/Arabic exists
    'Other Asian',  # Asian exists
    'Other Pacific',  # Pacific Islander exists
    'Other Spanish/Hispanic',  # Spanish and Hispanic exist
    'Other Subsaharan Africa',  # Subsaharan African exists
    'Other West Indian',  # West Indian exists
    'Acadian',  # Acadian/Cajun exists
    'Bosnian',  # Bosnian/Herzegovinian exists
    'Afghan',  # Afghan/Afghanistani exists
    'Alaskan Athabascan',  # Alaska Athabascan exists
    'American',  # American/United States exists
    'Antigua',  # Antiguan/Barbudan exists
    'Antiguan and Barbudan',  # Antiguan/Barbudan exists
    'Arab',  # Arab/Arabic exists
    'Arabic', # Arab/Arabic exists
    'Argentinean',  # Argentinean/Argentine is included
    'Argentine/Argentinean',  # Argentinean/Argentine is included
    'Asian Indian',  # Asian Indian/Indian (Asia) exists
    'Assyrian',  # Assyrian/Chaldean/Syriac exists
    'Belarusian',  # Belarusian/Belorussian exists
    'Bosnian',  # Bosnian/Herzegovinian exists
    'British Isles/British Isles origin',  # British Isles exists
    'British West Indian',  # British West Indian/Indies exists
    'Cameroonian',  # Cameroonian/Cameroon exists
    'Chaldean',  # Assyrian/Chaldean/Syriac exists
    'Congolese',  # Congolese/Congo exists
    'Croatian',  # Croatian/Croat is included
    'Croat/Croatian',  # Croatian/Croat is included
    'Danish',  # Danish/Dane is included
    'Dane/Danish',  # Danish/Dane is included
    'Dutch West Indies',  # Dutch West Indian/Indies exists
    'Emirati/United Arab Emirates',  # United Arab Emirates/Emirati is included
    'Filipino',  # Filipino/Philippine exists
    'Finnish',  # Finnish/Finn is included
    'Finn/Finnish',  # Finnish/Finn is included
    'Flemish',  # Fleming/Flemish exists
    'Fulani',  # Fulani/Hausa exists
    'Georgian',  # Georgian/Georgia CIS exists
    'German from Russia/German Russian',  # German Russian exists
    'Ghanian',  # Ghanaian/Ghanian exists
    'Ghanaian',  # Ghanaian/Ghanian exists
    'Guamanian or Chamorro',  # Guamanian and Chamorro Islander exist separately
    'Guamanian/Chamorro',  # Guamanian and Chamorro Islander exist separately
    'Herzegovinian',  # Bosnian/Herzegovinian exists
    'Hispanic or Latino',  # Hispanic and Latino exist
    'Ibo',  # Ibo/Igbo exists
    'Ivory Coast',  # Ivoirian/Ivory Coast exists
    'Java',  # Javanese/Java/Jawa exists
    'Kurdish',  # Kurdish/Kurd is included
    'Kurd/Kurdish',  # Kurdish/Kurd
    'Laotian',  # Lao/Laotian is included
    'Lao/Laotian',  # Laotian/Lao is included
    'Moldavian',  # Moldovan/Moldavian exists
    'Nepalese',  # Nepalese/Nepali exists
    'Nepali',  # Nepalese/Nepali exists
    'New Zealander/New Zealand',  # New Zealander exists
    'Osage Tribe',  # Osage exists
    'Pathan',  # Pashtun/Pathan exists
    'Polish',  # Polish/Pole is included
    'Pole/Polish',  # Polish/Pole is included
    'Saudi Arabian',  # Saudi Arabian/Saudi is included
    'Saudi/Saudi Arabian',  # Saudi Arabian/Saudi is included
    'Scandinavian',  # Scandinavian/Nordic exists
    'Scotch Irish',  # Scotch-Irish exists
    'Serb/Serbian',  # Serbian/Serb is included
    'Serbian',  # Serbian/Serb is included
    'Singaporean/Singapore',  # Singaporean exists
    'Singhalese',  # Singhalese/Sinhalese is included
    'Sinhalese/Singhalese',  # Singhalese/Sinhalese is included
    'Slav',  # Slavic/Slav is included
    'Slavic',  # Slavic/Slav is included
    'Slovene',  # Slovenian/Slovene is included
    'Slovene/Slovenian',  # Slovenian/Slovene is included
    'Somali',  # Somalian/Somali is included
    'Somali/Somalian',  # Somalian/Somali is included
    'Somalian',  # Somalian/Somali is included
    'Soviet Union',  # Soviet/Soviet exists
    'Spaniard/Spanish',  # Spaniard and Spanish exist separately
    'St. Vincent and Grenadine Islander'  # St. Vincent Islander/Vincent-Grenadine Islander exists
    'Suisse',  # Non-English version of Swiss
    'Suisse Romane',  # Non-English version of Swiss
    'Surinam/Dutch Guiana',  # Surinamese and Surinamese/Dutch Guiana are incl.
    'Swede/Swedish',  # Swedish/Swede is included
    'Swedish',  # Swedish/Swede is included
    'Syriac',  # Assyrian/Chaldean/Syriac exists
    'Togo',  # Togolese/Togo exists
    'Togolese',  # Togolese/Togo exists
    'Trinidadian',  # Trinidadian/Tobagonian exists
    'Trinidadian and Tobagonian',  # Trinidadian/Tobagonian exists
    'Turk/Turkish',  # Turkish/Turk is included
    'Turkish',  # Turkish/Turk is included
    'Turtle Mountain Band/Turtle Mountain',  # Turtle Mountain is included
    'United Arab Emirates',  # United Arab Emirates/Emirati is included
    'United States',  # American is included
    'Uzbek',  # Uzbek/Uzbeg is included
    'White',  # White/Caucasian is included
    'Yup\'ik',  # 'Yupik/Yupik Eskimo' is included
    'Yup\'ik/Yupik Eskimo',  # 'Yupik/Yupik Eskimo' is included
    # 'Alabama',
    # 'Alaska',
    # 'Arizona',
    # 'Arkansas',
    # 'California',
    # 'Colorado',
    # 'Connecticut',
    # 'Delaware',
    # 'District of Columbia'
    # 'Florida',
    # 'Georgia',
    # 'Hawaii',
    # 'Idaho',
    # 'Illinois',
    # 'Indiana',
    # 'Iowa',
    # 'Kansas',
    # 'Kentucky',
    # 'Louisiana',
    # 'Maine',
    # 'Maryland',
    # 'Massachusetts',
    # 'Michigan',
    # 'Minnesota',
    # 'Mississippi',
    # 'Missouri',
    # 'Montana',
    # 'Nebraska',
    # 'Nevada',
    # 'New Hampshire',
    # 'New Jersey',
    # 'New Mexico',
    # 'New York',
    # 'North Carolina',
    # 'North Dakota',
    # 'Ohio',
    # 'Oklahoma',
    # 'Oregon',
    # 'Pennsylvania',
    # 'Rhode Island',
    # 'South Carolina',
    # 'South Dakota',
    # 'Tennessee',
    # 'Texas',
    # 'Utah',
    # 'Vermont',
    # 'Virginia',
    # 'Washington',
    # 'West Virginia',
    # 'Wisconsin',
    # 'Wyoming',
)
