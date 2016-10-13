#!/usr/bin/env python

from datetime import datetime
import requests

class TurtleFile(object):
  __DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

  def __init__(self, payload):
    self.payload = payload

  def getId(self):              return self.payload['fileID']
  def getKey(self):             return self.payload['key']
  def getName(self):            return self.payload['fileName']
  def hasDraft(self):           if( self.payload['hasDraft'] == 0 ): return False else return True
  def getSize(self):            return self.payload['fileSize']
  def getDateCreated(self):     return datetime.strptime(self.payload['fileCreatedDate'], self.__DATE_FORMAT)
  def getDateUpdated(self):     return datetime.strptime(self.payload['fileUpdatedDate'], self.__DATE_FORMAT)
  def getContent(self):         if( 'fileData' in self.payload ): return self.payload['fileData'] else return None
  def getProjectId(self):       return self.payload['fileProjectID']


class Project(object):
  __DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

  def __init__(self, payload):
    self.payload = payload

  # Project specific
  def getId(self):              return self.payload['postID']
  def getKey(self):             return self.payload['key']
  def getName(self):            return self.payload['postName']
  def getUrlTitle(self):        return self.payload['url_title']
  def getDescription(self):     return self.payload['postDescription']
  def getStatus(self):          return self.payload['postStatus']
  def getInstructions(self):    return self.payload['postInstructions']
  def getDateCreated(self):     return datetime.strptime(self.payload['postCreatedDate'], self.__DATE_FORMAT)
  def getDateUpdated(self):     return datetime.strptime(self.payload['postUpdatedDate'], self.__DATE_FORMAT)
  def getIsPublished(self):     if( self.payload['postPublished'] == '1' ) return True else return False
  def getRequirements(self):    return self.payload['requires']
  def getRequires(self):        return self.payload['postRequirements']

  # User specific
  def getUser(self):            return self.payload['userUsername']
  def getUserId(self):          return self.payload['userID']
  def getUserDateCreated(self): return datetime.strptime(self.payload['userCreated'], self.__DATE_FORMAT)
  def getUserIGN(self):         return self.payload['userIGN']

  # File specific
  def getFileCount(self):       return self.payload['fileCount']
  def getFileTotalSize(self):   return self.payload['totalFileSize']
  def getFileKeys(self):        return [ {f['key']: f['fileName']} for f in self.payload['files'] ]

  # Comment/Vote specific
  def getCommentCount(self):    return self.payload['commentCount']
  def getVoteCount(self):       return self.payload['voteCount']
  def getVoteAverage(self):     return self.payload['voteAvg']

  # YouTube specific
  def getYouTubeId(self):       return self.payload['youtube_id']
  def getYouTubeUrl(self):      return self.payload['postYouTubeURL']

  # Miscellaneous attributes
  def getExtras(self):          return self.payload['extras']
  def getExtra(self):           return self.payload['postExtra']
  def getBeta(self):            return self.payload['postBeta']

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

    return project_json['payload']

  def getProjectName(self, project_id):
    """ """
    return self.getProject(project_id)['postName']
