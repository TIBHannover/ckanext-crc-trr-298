import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class UserManualPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates/user_manual')
        toolkit.add_public_directory(config_, 'public/user_manual_statics')
        toolkit.add_resource('public/user_manual_statics/statics', 'ckanext-sfb-layout')
        
    
