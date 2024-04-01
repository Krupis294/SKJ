import xmlrpc.client
import random
import visualizer
import xml.etree.ElementTree as ET

class Agent:

    def __init__(self, filename):

        self.tree = ET.parse(filename)

        self.login = self.tree.find("login").text
        self.url = self.tree.find("url").text

        self.data = []
        self.visualizer = visualizer.Visualizer()

        self.gameserver = xmlrpc.client.ServerProxy(self.url)
        
        self.gameserver.add_player(self.login)
        
        # TODO 1     - load data from the XML configuration file (filename is in the parameter)
        # TODO 2     - create instance variables (login, data, visualizer, gameserver)
        # login      - load from XML file (tag 'login')
        # data       - an empty list, where data from server will be stored
        # visualizer - instance of the visualizer.Visualizer class
        # gameserver - connect to the remote XML-RPC server (url is provided in the XML file, tag 'url')
        # TODO 3     - call method 'add_player' on the server with login as the parameter (use instance variable 'self.login')




        pass

    def action(self):
        # TODO 4 - Call 'make_action' method on the XML-RPC server.
        # The method has 3 parameters (login, action_name, parameters).
        # All three parameters are strings. Call the 'look' method on the server,
        # to take a look around the player, without NY parameter (empty string).
        # Every action returns a list of strings, where each row represents one
        # row from the surrounding area of the player.
        # Each string is 11-characters in length and there are 22 rows.
        # First 11 elements of the list represent the agent's environment
        # and other 11 elements of his surroundings
        # (so far, only "p" character is present to represent other agents).
        # The player is in this surrounding at the position [5][5] (5th row, 5th character).
        # Objects on the same position can be sought at the coordinates [5 + 11] [5].
        # "~" water
        # " " grass
        # "*" road
        # "t" tree
        # "o" rock (wall)
        # "f" tiled floor
        # "p" player

        # self.gameserver.make_action(self.login, action_name, parameters)
        # self.gameserver.look()
        result = self.gameserver.make_action(self.login, "look", "")
        self.visualizer.visualize(result)
        pass
    
    def __repr__(self):
        # TODO 5 - Returns human readable representation of stored data form 'self.data' variable.
        separator = ", "
        return separator.join(self.data)
        pass

    def save_data(self):
     # TODO 6 - Store data into the 'data.txt' filename.
        try:
            f = open("data.txt", "w")
            
            for item in self.data:
                #f.close()
                # f = open("data.txt", "at")
                f.write(item + "\n")

        except IOError:
            pass
            #f = open("data.txt", "w")
            #f.close()
        finally:
            f.close()
        pass

class AgentRandom(Agent):
    # TODO 7 - This agent will extend from the previous agent and
    # reimplement (override) the 'action' method so that the action will be 'move' and
    # the passed parameter will be one the directions: 'north', 'west', 'south', 'east'.
    # These directions will be randomly selected
    # (find the appropriate method from the random package).
    # Call the 'make_action' method from the parent class.
    # The 'action' method returns the result of the 'make_action' method.
    # The result will be visualized by the visualizer object.
    # The agent will be moving in random directions until the visualizer is running (True).
    def action(self):
        directions = ['north', 'west', 'south', 'east']
        random_direction = random.choice(directions)
        result = self.gameserver.make_action(self.login, "move", random_direction)
        self.visualizer.visualize(result)
    pass

class AgentLeftRight(Agent):
    # TODO 8 - This agent will be moving just to the left until it hits a barrier.
    # Then it run to the right and moves until it hits the barrier again.
    # It repeats such behavior.

    def __init__(self, filename):
        super().__init__(filename)
        self.direction = "west"

    def action(self):
        result = self.gameserver.make_action(self.login, "move", self.direction)
        self.visualizer.visualize(result)
        print(result)
        print("vlevo" + result[5][4])
        print("vpravo" + result[5][6])
        print("nahore" + result[4][5])
        print("dole" + result[6][5])
        # Check if the agent hits a barrier
        if "o" in result[5][4] or "t" in result[5][4] or "~" in result[5][4] and self.direction == "west":
                self.direction = "east"
        elif "o" in result[5][6] or "t" in result[5][6] or "~" in result[5][6] and self.direction == "east":
                self.direction = "west"

def main():
    agent = None
    try:
        #agent = AgentLeftRight('config.xml')
        agent = AgentRandom('config.xml')
        #agent = Agent('config.xml')
        while agent.visualizer.running:
            agent.action()
            print(agent)
        else:
            agent.gameserver.make_action(agent.login, 'exit', '')
        agent.save_data()
    except KeyboardInterrupt:
        agent.gameserver.make_action(agent.login, 'exit', '')

if __name__ == '__main__':
    main()
