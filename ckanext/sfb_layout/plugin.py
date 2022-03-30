import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.sfb_layout.lib import Helper


class SfbLayoutPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/sfb_layout')
        toolkit.add_public_directory(config_, 'public/sfb_layout')
        toolkit.add_resource('public/sfb_layout/statics', 'ckanext-sfb-layout')
        
    

    def get_helpers(self):
        return {'which_sfb': Helper.which_sfb}