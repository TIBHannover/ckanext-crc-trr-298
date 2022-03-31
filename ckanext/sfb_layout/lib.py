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
        plugins_with_stages = ['resource_custom_metadata', 'organization_group', 'semantic_media_wiki']
        enabled_plugins = toolkit.config.get("ckan.plugins")
        count = 0
        for pl in plugins_with_stages:
            if pl in enabled_plugins:
                count += 1
        
        return count
    


    @staticmethod
    def get_stages_class(current_stages):
        stages = [''] * (Helper.stages_count() + 2)
        for i in range(len(stages)):
            try:
                stages[i] = current_stages[i]
            except:
                if i == 0:
                    stages[i] = 'active'
                else:
                    stages[i] = 'uncomplete'
        
        return stages

    
    