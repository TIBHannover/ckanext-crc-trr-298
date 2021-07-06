# ckanext-sfb-layout

| Plugin    | Description   |
| --------------- | ------------- |
|  **sfb1368_style** | This plugin modifies the ckan general style for the site headers and footer    |
| **user_manual** | The plugin adds a "Help" option on the site main navigation menu. The Help page contains information about CKAN functionalities that aims to answer users questions and guiding them to use CKAN.           |
| **feature_image** | The plugin ables system admins to upload a featured image and caption for the CKAN homepage.|


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

3. Add `sfb1368_style`, `user_manual`, and `feature_image`  to the `ckan.plugins` setting in your CKAN config file (by default the config file is located at `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Nginx on Ubuntu:

        sudo service nginx reload


## Customization

| Plugin    | Description   |
| --------------- | ------------- |
|  **sfb1368_style** | Modify `public/sfb1368_style_statics/statics/ckan_style.css`  |
| **user_manual** |      The page contents are in: `templates/user_manual/snippets/sections`. You may also need to change `templates/user_manual/snippets/ckanext_user_manual_help.html`     |


