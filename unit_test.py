import unittest
from unittest import result
import playerName
import server
from flask import redirect, Flask, request, render_template

class UnitTest(unittest.TestCase):
    def testSearchPlayerByName(self):
     searchData = list()
     result = list()
     playerList = playerName.getPlayerTable()    
     result = playerName.searchPlayerByName(playerList,"Travis Knight")
     for player in playerList:
      if player['player_name'] == "Travis Knight":
       searchData.append(player)
     self.assertEqual(result,searchData)
     self.assertNotEqual(playerList,searchData)
     self.assertListEqual(searchData,result)
     

    def testSearchPlayerByDraftYear(self):
     searchData = list()
     result = list()
     playerList = playerName.getPlayerTable()    
     result = playerName.searchPlayerByDraftYear(playerList,"2000")
     for player in playerList:
       if player['draft_year'] == "2000":
        searchData.append(player)
     self.assertEqual(result,searchData)
    
    def testSearchPlayerBySeason(self):
     searchData = list()
     result = list()
     playerList = playerName.getPlayerTable()    
     result = playerName.searchPlayerBySeason(playerList,"2016-17")
     for player in playerList:
       if player['season'] == "2016-17":
        searchData.append(player)
     self.assertEqual(result,searchData)
 

if __name__ == '__main__':
    unittest.main()