#!/usr/bin/env python3.5
# -*- conding: utf-8 -*-

'''
    Description:
        AWS Codepipeline create

    Sample Usage:
        file   = 'pipeline.json'
        object = Codepipeline(file)
        if object.is_exists():
            print('CodePipeline: ' + object.pipeline_name + ' found.')
        else:
            print('CodePipeline: ' + object.pipeline_name + ' not found.')
        
            try:
                object.create()
            except ClientError as err:
                print('CodePipeline: ' + object.pipeline_name + ' create failed.')
            else:
                print('CodePipeline: ' + object.pipeline_name + ' created.')
            finally:
                pass

'''

from botocore.exceptions import ClientError
import boto3
import json

class AwsFamiliar:

    # initialize
    def __init__(self):
        '''plase override subclass'''

class Codepipeline(AwsFamiliar):

    # initialize
    def __init__(self):
        '''plase override subclass'''

class CustomAction(Codepipeline):

    # initialize
    def __init__(self,custom_action_define_file):
        self.codepipeline  = boto3.client('codepipeline')
        self.action_file = custom_action_define_file

        with open(self.action_file, 'r') as json_f:
            self.custom_action_json = json.load(json_f)
            self.category  = self.custom_action_json['category']
            self.provider  = self.custom_action_json['provider']
            self.version   = self.custom_action_json['version']
            self.settings  = self.custom_action_json['settings']
            self.configurationProperties  = self.custom_action_json['configurationProperties']
            self.inputArtifactDetails     = self.custom_action_json['inputArtifactDetails']
            self.outputArtifactDetails    = self.custom_action_json['outputArtifactDetails']

    # check custom action exists
    # return: True/False
    def is_exists(self):
        try:
            response = self.codepipeline.list_action_types(
                actionOwnerFilter = 'Custom'
            )

            for action in response['actionTypes']:
                if action['id']['category'] == self.category and \
                   action['id']['provider'] == self.provider and \
                   action['id']['version']  == self.version:
                    return True
                else:
                    continue

        except ClientError as err:
            return False
        
        else:
            return False

        finally:
            pass

    # create custom action
    def create(self):
        response = self.codepipeline.create_custom_action_type(
            category = self.category,
            provider = self.provider,
            version  = self.version,
            settings = self.settings,
            configurationProperties = self.configurationProperties,
            inputArtifactDetails    = self.inputArtifactDetails,
            outputArtifactDetails   = self.outputArtifactDetails
        )

class Pipeline(Codepipeline):

    # initialize
    def __init__(self,pipeline_file):
        self.codepipeline  = boto3.client('codepipeline')
        self.pipeline_file = pipeline_file

        with open(self.pipeline_file, 'r') as json_f:
            self.codepipeline_json = json.load(json_f)
            self.pipeline_name = self.codepipeline_json['pipeline']['name']

    # check pipeline exists
    # return: True/False
    def is_exists(self):
        try:
            response = self.codepipeline.get_pipeline(
                name = self.pipeline_name
            )
        
        except ClientError as err:
            return False
        
        else:
            return True

        finally:
            pass

    # create json file of specific pipeline.
    # file name as specific pipeline name.
    def get_pipeline(self):
        try:
            response = self.codepipeline.get_pipeline(
                name = self.pipeline_name
            )

            f = open(self.pipeline_name + ".json", "w")
            pipeline_json = { "pipeline" : response['pipeline'] }
            json.dump(pipeline_json, f, indent=4, sort_keys=False)

        except ClientError as err:
            return False
        
        else:
            return True

        finally:
            pass

    # create pipeline
    def create(self):
        response = self.codepipeline.create_pipeline(
            pipeline={
                'name'          : self.pipeline_name,
                'roleArn'       : self.codepipeline_json['pipeline']['roleArn'],
                'artifactStore' : self.codepipeline_json['pipeline']['artifactStore'],
                'stages'        : self.codepipeline_json['pipeline']['stages'],
                'version'       : self.codepipeline_json['pipeline']['version']
            }
        )

    # update pipeline
    def update(self):
        response = self.codepipeline.update_pipeline(
            pipeline={
                'name'          : self.pipeline_name,
                'roleArn'       : self.codepipeline_json['pipeline']['roleArn'],
                'artifactStore' : self.codepipeline_json['pipeline']['artifactStore'],
                'stages'        : self.codepipeline_json['pipeline']['stages'],
                'version'       : self.codepipeline_json['pipeline']['version']
            }
        )



