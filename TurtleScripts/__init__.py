#!/usr/bin/env python

from TurtleScripts import TurtleScripts

__all__ = ['TurtleScripts']

def getProject(project_id):
  ts = TurtleScripts()
  ts.getProject(project_id)
