#!/usr/bin/env python

import requests

class TurtleScripts(object):
  """  """

  TURTLESCRIPTS_API_URL = 'api.turtlescripts.com'
  TURTLESCRIPTS_PROTOCOL = 'http'

  def __init__(self):
    pass

  def __geturl__(self, uri):
    """ """
    return "{0}://{1}/{2}".format(self.TURTLESCRIPTS_PROTOCOL, self.TURTLESCRIPTS_API_URL, uri)

  def getProject(self, project_id):
    """ """
    url = self.__geturl__('getProject/{0}'.format(project_id))
    project_response = requests.get(url)
    if( project_response.status_code != requests.codes.ok ):
      raise Exception('Failed to contact TurtleScripts.com')

    project_json = project_response.json()

    if( project_json['success'] == False ):
      raise Exception("Failed to retrieve project '{0}' from TurtleScripts.com" \
                      ": {1}".format(project_id, project_json['errors']['id']))

    return project_json

