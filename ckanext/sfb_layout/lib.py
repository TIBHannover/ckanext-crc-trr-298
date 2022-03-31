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
    
    