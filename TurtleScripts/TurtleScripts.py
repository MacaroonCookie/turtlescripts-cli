#!/usr/bin/env python

from datetime import datetime
import requests

class TurtleFile(object):
  __DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

  def __init__(self, payload):
    self.payload = payload

  def getId(self):              return int(self.payload['fileID'])
  def getKey(self):             return self.payload['key']
  def getName(self):            return self.payload['fileName']
  def getProjectId(self):       return int(self.payload['fileProjectID'])
  def hasDraft(self):           return False if( 'hasDraft' not in self.payload or self.payload['hasDraft'] == 0 ) else True
  def getSize(self):            return 0 if( self.payload['fileSize'] is None ) else int(self.payload['fileSize'])
  def getDateCreated(self):     return datetime.strptime(self.payload['fileCreatedDate'], self.__DATE_FORMAT)
  def getDateUpdated(self):     return datetime.strptime(self.payload['fileUpdatedDate'], self.__DATE_FORMAT)
  def getContent(self):         return self.payload['fileData'] if( 'fileData' in self.payload ) else None

class TurtleProject(object):
  __DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

  def __init__(self, payload):
    self.payload = payload
  def getProjectId(self):       return int(self.payload['fileProjectID'])

  # Project specific
  def getId(self):              return int(self.payload['postID'])
  def getKey(self):             return self.payload['key']
  def getName(self):            return self.payload['postName']
  def getUrlTitle(self):        return self.payload['url_title']
  def getDescription(self):     return self.payload['postDescription']
  def getStatus(self):          return int(self.payload['postStatus'])
  def getInstructions(self):    return self.payload['postInstructions']
  def getDateCreated(self):     return datetime.strptime(self.payload['postCreatedDate'], self.__DATE_FORMAT)
  def getDateUpdated(self):     return datetime.strptime(self.payload['postUpdatedDate'], self.__DATE_FORMAT)
  def getIsPublished(self):     return True if( self.payload['postPublished'] == '1' ) else False
  def getRequirements(self):    return self.payload['postRequirements']
  def getRequires(self):        return self.payload['requires']

  # User specific
  def getUser(self):            return self.payload['userUsername']
  def getUserId(self):          return int(self.payload['userID'])
  def getUserDateCreated(self): return datetime.strptime(self.payload['userCreated'], self.__DATE_FORMAT)
  def getUserIGN(self):         return self.payload['userIGN']

  # File specific
  def getFileCount(self):       return 0 if( self.payload['fileCount'] is None ) else int(self.payload['fileCount'])
  def getFileTotalSize(self):   return 0 if( self.payload['totalFileSize'] is None ) else int(self.payload['totalFileSize'])
  def getFileKeys(self):        return [ {f['key']: f['fileName']} for f in self.payload['files'] ]

  # Comment/Vote specific
  def getCommentCount(self):    return 0 if( self.payload['commentCount'] is None ) else self.payload['commentCount']
  def getVoteCount(self):       return 0 if( self.payload['voteCount'] is None ) else self.payload['voteCount']
  def getVoteAverage(self):     return 0.0 if( self.payload['voteAvg'] is None ) else self.payload['voteAvg']

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

  def __get__(self, url):
    """ """
    response = requests.get(url)
    if( response.status_code != requests.codes.ok ):
      raise Exception('Failed to contact TurtleScrtips.com')

    response_json = response.json()

    if( 'success' not in response_json or
        'payload' not in response_json or
        'errors' not in response_json or
        'result_time' not in response_json ):
      raise Exception('Received malformed response from TurtleScripts.com')

    if( response_json['success'] == False ):
      raise Exception("Failed to retreive object from TurtleScripts.com" \
                      ": {0}".format(response_json['errors']['id']))

    return response_json['payload']

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

    return TurtleProject(project_json['payload'])

  def getFileObject(self, file_key, read_pin=None):
    """ """
    url = self.__geturl__('getFile/{0}'.format(file_key))
    file_payload = self.__get__(url)
    return TurtleFile(file_payload)

  def saveFile(self, file_key, read_pin=None, overwrite=False, file_name=None, directory=None):
    file_object = self.getFileObject(file_key, read_pin)

    if( directory is None ):
      directory = os.getcwdu()

    if( not os.path.exists(directory) ):
      raise Exception("Directory '{0}' does not exist".format(directory))

    if( file_name is None ):
      file_name = file_object.getName()

    file_name = os.path.join(directory, file_name)

    if( os.path.exists(file_name) and not overwrite ):
      raise Exception("File '{0}' already exists.".format(file_name))

    file_handle = open(file_name, 'w')

    file_handle.write(file_object.getContent())
    file_handle.close()

  def uploadFile(self, file_key, write_pin, file_name):
    if( not os.path.exists(file_name) ):
      raise Exception("File '{0}' does not exist.".format(file_name))

    file_handle = open(file_name, 'r')
    data_content = file_handle.readall()
    file_handle.close()

    url = self.__geturl__("putFileRaw/{0}".format(file_key))
    data = "pin={0}&data={1}".format(write_pin, data_content)

    response = requests.post(url, data=data)

    if( response.status_code != requests.codes.ok ):
      raise Exception('Failed to contact TurtleScrtips.com, submit file, or file content is equal to what is placed.')

    return True
