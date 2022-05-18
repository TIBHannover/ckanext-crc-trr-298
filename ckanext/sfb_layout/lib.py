# encoding: utf-8
from flask import render_template, request, redirect, app
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h
import ckan.model as model
import ckan.logic as logic



class Helper():
    
    @staticmethod
    def which_sfb():
        '''
            Check which sfb server the plugin is runnung in. 
        '''

        ckan_root_path = toolkit.config.get('ckan.root_path')
        if  ckan_root_path and 'sfb1368/ckan' in ckan_root_path:
            return '1368'
        elif ckan_root_path and 'sfb1153/ckan' in ckan_root_path:
            return '1153'
        else:
            # localhost
            return '1368'
    

    @staticmethod
    def check_plugin_enabled(plugin_name):
        plugins = toolkit.config.get("ckan.plugins")
        if plugin_name in plugins:
            return True
        return False
    

    @staticmethod
    def stages_count():
        plugins_with_stages = ['resource_custom_metadata', 'organization_group', 'semantic_media_wiki', 'sample_link']
        enabled_plugins = toolkit.config.get("ckan.plugins")
        count = 0
        for pl in plugins_with_stages:
            if pl in enabled_plugins:
                count += 1
        
        return count


    @staticmethod
    def set_stages():
        stages= []
        if Helper.which_sfb() == '1368':
            if  'dataset/new' in  h.full_current_url():
                stages = ['active', 'uncomplete','uncomplete', 'uncomplete', 'uncomplete']
            
            elif 'resource/new' in h.full_current_url():
                stages = ['complete', 'active','uncomplete', 'uncomplete', 'uncomplete']
            
            elif 'resource_custom_metadata/index' in h.full_current_url():
                stages = ['complete', 'complete','active', 'uncomplete', 'uncomplete']
            
            elif 'upgrade_dataset/add_ownership_view' in h.full_current_url():
                stages = ['complete', 'complete','complete', 'active', 'uncomplete']
            
            elif 'smw/machines_view' in h.full_current_url():
                stages = ['complete', 'complete','complete', 'complete', 'active']
        
        else:
            # 1153
            if  'dataset/new' in  h.full_current_url():
                stages = ['active', 'uncomplete','uncomplete', 'uncomplete', 'uncomplete']
            
            elif 'resource/new' in h.full_current_url():
                stages = ['complete', 'active','uncomplete', 'uncomplete', 'uncomplete']
                        
            elif 'upgrade_dataset/add_ownership_view' in h.full_current_url():
                stages = ['complete', 'complete','active', 'uncomplete', 'uncomplete']
            
            elif 'smw/machines_view' in h.full_current_url():
                stages = ['complete', 'complete','complete', 'active', 'uncomplete']
            
            elif '/smw/add_samples_view' in h.full_current_url():
                stages = ['complete', 'complete','complete', 'complete', 'active']
        
        return stages


    @staticmethod
    def set_orders():
        if Helper.which_sfb() == '1368':
            return ['second', 'third', 'forth']
        else:
            return ['second', 'third', 'forth']
    


    @staticmethod
    def set_titles():
        if Helper.which_sfb() == '1368':
            return ['Add data', 'Metadata', 'Ownership', 'Equipment(s)'] 
        else:
            return ['Add data', 'Ownership', 'Equipment(s)', 'Sample(s)'] 



    @staticmethod
    def search_query_prepration(query):
        if "sample:" in query:
            return query.split(":")[1]
        elif "column:" in query:
            return query.split(":")[1]
        else:
            return query
    


    @staticmethod
    def is_selection_needed(form_id):
        if form_id in ["organization-search-form", "group-search-form"]:
            return False
        return True
    
    