# ckanext-crc-trr-298

The CKAN extension for the CRC TRR-298 project Data Repository. 

## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
|  2.9 | Yes    |
| earlier | Not Tested |           |


## Installation

To install ckanext-sfb-layout:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

        git clone https://github.com/TIBHannover/ckanext-crc-trr-298.git
        cd ckanext-crc-trr-298
        pip install -e .
        pip install -r requirements.txt

3. Add `trr_298` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Nginx on Ubuntu:

        sudo service supervisor reload
        sudo service nginx reload





