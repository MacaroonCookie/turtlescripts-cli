#!/usr/bin/env python

from .TurtleScripts import TurtleScripts, TurtleProject, TurtleFile

def getProject(project_id):
  ts = TurtleScripts()
  ts.getProject(project_id)
