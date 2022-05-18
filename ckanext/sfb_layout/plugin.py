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
        toolkit.add_resource('public/sfb_layout/statics', 'ckanext-sfb-layout')
        
    

    def get_helpers(self):
        return {'which_sfb': Helper.which_sfb, 
            'is_enabled': Helper.check_plugin_enabled,
            'stages_count': Helper.stages_count, 
            'set_stages': Helper.set_stages,
            'set_orders': Helper.set_orders,
            'set_titles': Helper.set_titles,
            'query_prepration': Helper.search_query_prepration
        }