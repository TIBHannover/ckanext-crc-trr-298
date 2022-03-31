# ckanext-sfb-layout

| Plugin    | Description   |
| --------------- | ------------- |
|  **sfb_layout** | This plugin modifies the ckan general style for the site content, headers. and footer    |


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

        git clone https://github.com//ckanext-sfb-layout.git
        cd ckanext-sfb-layout
        pip install -e .
        pip install -r requirements.txt

3. Add `sfb_layout` to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Nginx on Ubuntu:

        sudo service supervisor reload
        sudo service nginx reload





