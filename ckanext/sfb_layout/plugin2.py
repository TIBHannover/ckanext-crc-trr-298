import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SfbSixtyEightStylePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/sfb1368_style')
        toolkit.add_public_directory(config_, 'public/sfb1368_style_statics')
        toolkit.add_resource('public/sfb1368_style_statics/statics', 'ckanext-sfb-layout-sfb1368')
        
    
