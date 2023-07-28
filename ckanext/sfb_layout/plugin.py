import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.sfb_layout.lib import Helper


class SfbLayoutPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public/sfb_layout')
        toolkit.add_resource('public/sfb_layout/statics', 'ckanext-crc-trr-298')
    
        
    

    def get_helpers(self):
        return {
            'is_enabled': Helper.check_plugin_enabled           
        }