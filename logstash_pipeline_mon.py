#!/usr/bin/env python3.8

"""
Script to monitor Logstash pipelines
"""
__author__ = "Developed by: Wolfgang Azevedo"
__email__ = "wolgang@ildt.io"
__license__ = "GPL"
__version__ = "1.0"

import json
from datetime import datetime
import time
import yaml
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


class PipelineMon:

    def __init__(self, **kwargs):
        '''
        Constructor Method of PipelineMon class
        '''
        try:
            with open(f'{kwargs.get("config")}', 'r') as config_file:
                config = yaml.safe_load(config_file)

            self.servers = config['servers']

        except (TypeError, FileNotFoundError) as error:
            print(f'[LOGSTASH_MON] - Configuration file not found! Please check --> {error}....')


    def timestamp(self):
        timestamp =  datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        return timestamp


    def get_logstash_data(self, **kwargs):
        for logstash_server in self.servers:
                for pipelines in self.servers[logstash_server]['pipelines']:
                    try:
                        url = f'http://{self.servers[logstash_server]["ip"]}:{self.servers[logstash_server]["port"]}/_node/stats/pipelines/{pipelines}'

                        response = requests.get(url)
                        response.encoding = 'utf-8'
                        json_response = json.loads(response.text)

                        for in_values in json_response['pipelines'][pipelines]['plugins']['inputs']:
                            print(f'{self.timestamp()} - {logstash_server} - {in_values["name"]} - out: {str(in_values["events"]["out"])}') 
                    
                        for out_values in json_response['pipelines'][pipelines]['plugins']['outputs']:
                            print(f'{self.timestamp()} - {logstash_server} - {out_values["name"]} - in: {str(out_values["events"]["in"])}')
                            print(f'{self.timestamp()} - {logstash_server} - {out_values["name"]} - out: {str(out_values["events"]["out"])}')

                    except Exception as error:
                        print(f'[LOGSTASH_MON] No valid pipeline {self.servers[logstash_server]["pipelines"]} found on list: {error}'
                              f' of server {logstash_server}..., check YAML config file!')


if __name__ == '__main__':

    connect = PipelineMon(config='config.yml')
    connect.get_logstash_data()