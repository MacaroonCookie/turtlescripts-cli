#!/usr/bin/env python

from datetime import datetime
from TurtleScripts import TurtleScripts, TurtleProject, TurtleFile

import unittest

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
TEST_PROJECT_ID = 'gjdi6h'

class TestTurtleScripts(unittest.TestCase):

  def setUp(self):
    self.ts = TurtleScripts()

  def test_get_project(self):
    test_project = self.ts.getProject(TEST_PROJECT_ID)

    self.assertIsInstance(test_project, TurtleProject)
    self.assertEqual(test_project.getName(), "Test Project")
    self.assertEqual(test_project.getId(), 1609)
    self.assertEqual(test_project.getKey(), TEST_PROJECT_ID)
    self.assertEqual(test_project.getUrlTitle(), "Test-Project")
    self.assertEqual(test_project.getDescription(), "Just a test project for testing the HTTP API.")
    self.assertEqual(test_project.getStatus(), 0)
    self.assertEqual(test_project.getInstructions(), "")
    self.assertTrue(test_project.getIsPublished())
    self.assertEqual(test_project.getRequirements(), "Advanced Computer,Computer,Turtle,Mining Turtle")
    self.assertEqual(test_project.getExtra(), "Advanced Monitor,Monitor")
    self.assertIn("Advanced Computer", test_project.getRequires())
    self.assertIn("Computer", test_project.getRequires())
    self.assertIn("Turtle", test_project.getRequires())
    self.assertIn("Mining Turtle", test_project.getRequires())
    self.assertIn("Advanced Monitor", test_project.getExtras())
    self.assertIn("Monitor", test_project.getExtras())
    self.assertIs(type(test_project.getFileTotalSize()), type(1))
    self.assertEqual(test_project.getDateCreated(), datetime.strptime("2016-10-07 15:54:00", DATE_FORMAT))
    self.assertIsInstance(test_project.getDateUpdated(), datetime)
    self.assertEqual(test_project.getUser(), "MacaroonCookie")
    self.assertEqual(test_project.getUserId(), 3942)
    self.assertEqual(test_project.getUserDateCreated(), datetime.strptime("2015-10-28 22:35:30", DATE_FORMAT))
    self.assertEqual(test_project.getUserIGN(), "")
    self.assertEqual(test_project.getFileCount(), 0)
    self.assertIs(type(test_project.getFileTotalSize()), type(1))
    self.assertEqual(test_project.getFileKeys(), [])
    self.assertIs(type(test_project.getCommentCount()), type(1))
    self.assertIs(type(test_project.getVoteCount()), type(1))
    self.assertIs(type(test_project.getVoteAverage()), type(1.1))
    self.assertEqual(test_project.getYouTubeId(), "")
    self.assertEqual(test_project.getYouTubeUrl(), "")
    self.assertEqual(test_project.getBeta(), "")

if( __name__ == '__main__' ):
  unittest.main()
