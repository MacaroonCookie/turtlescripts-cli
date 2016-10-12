#!/usr/bin/env python

from turtlescripts import TurtleScripts

import unittest

TEST_PROJECT_ID = 'gjdi6h'

class TestTurtleScripts(unittest.TestCase):

  def setUp(self):
    self.ts = TurtleScripts()

  def test_get_project(self):
    print(self.ts.getProject(TEST_PROJECT_ID))
    self.assertTrue(True)

if( __name__ == '__main__' ):
  unittest.main()
