# all location classes for game
# dictionary at bottom 

import things

class Location(object):
    """
    Parent class for all locations in the game. Location 00. Lots of 
    functions here because they are available in all locations.
    - action() is the crucial function
    - response (variable) stores the interaction from the player
    """

    def __init__(self):
        self.items = []
        self.first_visit = True

    def enter(self):
    # announce the current location when you enter it
        print self.name
        if self.first_visit:
            print self.descrip
            self.first_visit = False
        self.list_items()

    def action(self):
    # runs in all location classes - Engine() makes it so 
        t = []
        while True:
            response = raw_input("> ")
            if self.items or things.inventory:
                t = self.check_for_things(response)
            if len(t) > 0:
                self.use_item(response, t)
            elif "look" in response:
                print self.descrip
                self.list_items()
            elif "inventory" in response or response == "i":
                self.take_inventory()
            elif "drop" in response:
                self.drop_all(response)
            elif "take" in response:
                print "What do you want to take?"
            else:
                return self.travel(response)
                # this is particular to each location

    def check_for_things(self, r):
    # find out which and how many things you named in your response
        t = []
        for item in self.items:
            if item.nickname in r:
                t.append(item)
        for item in things.inventory:
            if item.nickname in r:
                t.append(item)
        return t

    def list_items(self):
    # announce all items available in your current location
        if self.items:
            for item in self.items:
                print "    There is a %s here" % item.name
            print

    def take_inventory(self):
    # lists all things that you are carrying
        if things.inventory:
            print "You are carrying:"
            for item in things.inventory:
                print item.name
        else:
            print "You are not carrying anything."

    def drop_all(self, r):
    # runs when "drop" appears in response but no items were named 
        if r == "drop":
            print "Drop what? Give us a hint!"
        elif "all" in r or "everything" in r:
            if things.inventory:
                for i in things.inventory:
                    print "%s dropped" % i.name
                    self.items.append(i)
                    if i.name == "raft":
                        things.carrying_raft = False
                things.inventory = []
                print
            else:
                print "You are not carrying anything."
        else:
            print "What do you want to drop?"

    def use_item(self, r, t):
        """
        This function runs if you have typed the name of ANY item in
        your response. It handles all generic manipulations of the items: 
        put, look, drop, take
        
        It will NOT run if you did not include an item name in your response.
        
        Things to do: 
        Ability to put things into the raft. 
        DONE Make raft special: Can pick up only if you are not 
        carrying anything else.
        DONE Cannot pick up raft if anything is in it. 
        """
        if "put" in r:
            self.put_items(r, t)
        elif len(t) > 1:
            print "You can only deal with one item at a time."
        elif "look" in r:
            print t[0].descrip, "\n"
        elif "drop" in r:
            self.drop_items(t)
        elif "take" in r:
            self.take_items(t)
        else:
            print "What do you want to do with the %s?" % t[0].name

    def put_items(self, r, t):
    # how to put items in the raft
        print "Put is not working yet."

    def drop_items(self, t):
    # if item is in inventory, can drop
        if t[0] in things.inventory:
            things.inventory.remove(t[0])
            self.items.append(t[0])
            print "You drop the %s." % t[0].name
            # check for raft
            if t[0].name == "raft":
                things.carrying_raft = False
        else:
            print "You are not carrying any %s." % t[0].name

    def take_items(self, t):
    # how to pick up things (the raft can only be carried alone)
        if t[0] in things.inventory:
            print "You are already carrying the %s." % t[0].name
        elif not t[0] in self.items:
            print "There is no %s here." % t[0].name
        elif things.carrying_raft:
            print "You can't carry anything else when you are carrying",
            print "the raft."      
        elif t[0].name == "raft" and not things.inventory:
            self.move_item(t)
            things.carrying_raft = True
        elif len(things.inventory) < 4:
            self.move_item(t)
        else:
            print "You cannot take the %s." % t[0].name
            print "You are carrying too many things already."
            print 'Type "inventory" or "i" to see what you\'ve got.\n'

    def move_item(self, t):
        things.inventory.append(t[0])
        self.items.remove(t[0])
        print "You are now carrying the %s." % t[0].name


class Bongo_Glade(Location):
    """
    Location 01.
    """

    name = "\nGlade of the Bongo Fruit Tree"
    descrip = """    Sunlight streams down from a wide opening in the
    forest canopy. Directly below that opening stands a 
    magnificent stout tree, its branches bending with the 
    weight of large, round, shining purple fruits. There 
    is a break in the dense forest to the south.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "south" in response or response == 's':
                return '07'
            else:
                print "I don't understand that."


class Path2(Location):
    """
    Location 02.
    """

    name = "\nPath"
    descrip = """    The remains of a cleared path run east and south. To 
    the east is a kind of bridge.\n"""   

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '03'
            elif "south" in response or response == 's':
                return '08'
            else:
                print "I don't understand that."


class North_Bridge(Location):
    """
    Location 03.
    """

    name = "\nBridge"
    descrip = """    A rickety structure made only of bamboo strips and 
    woven rattan spans the river. Standing on this bridge is
    surely a great risk!\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '04'
            elif "west" in response or response == 'w':
                return '02'
            else:
                print "I don't understand that."


class Path4(Location):
    """
    Location 04.
    """

    name = "\nPath"
    descrip = """    Here a barely perceptible old path leads to the 
    south and east. A kind of bridge can be seen to the west.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '05'
            elif "west" in response or response == 'w':
                return '03'
            elif "south" in response or response == 's':
                return '09'
            else:
                print "I don't understand that."


class Path5(Location):
    """
    Location 05.
    """

    def __init__(self):
        self.basket = things.Basket()
        self.items = [self.basket.name]

    name = "\nPath"
    descrip = """    The path ends here, choked off by dense foliage
    and thick, twisted vines. An ancient basket, woven from 
    grasses or reeds, lies on the ground.\n"""
    descrip2 = """    The path ends here, choked off by dense foliage
    and thick, twisted vines.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "west" in response or response == 'w':
                return '04'
            else:
                print "I don't understand that."


class Dense_Forest6(Location):
    """
    Location 06.
    """

    name = "\nDense Forest"
    descrip = """    The forest growth is impossibly thick here. You can
    only return the way you came.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '07'
            else:
                print "I don't understand that."


class Dense_Forest7(Location):
    """
    Location 07.
    """

    name = "\nDense Forest"
    descrip = """    The tangled undergrowth here might yield to a sharp
    blade. At present, you can't go anywhere but east.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "east" in response or response == 'e':
                return '08'
            elif "north" in response or response == 'n':
                return '01'
            elif "west" in response or response == 'w':
                return '06'
            elif "southwest" in response or response == 'sw':
                return '11'
            else:
                print "I don't understand that."


class Slope(Location):
    """
    Location 08.
    """

    name = "\nSmall Slope"
    descrip = """    The ground here makes a hump, going up toward the west.
    You could move sideways on the slope toward the north.\n"""

    def action(self):
        while True:
            response = raw_input("> ")
            if "look" in response:
                print self.descrip
            elif "west" in response or response == 'w':
                return '07'
            elif "north" in response or response == 'n':
                return '02'
            else:
                print "I don't understand that."


class Dense_Forest9(Location):
    """
    Location 09.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Falls(Location):
    """
    Location 10.
    """

    name = "Falls"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Panther_Forest(Location):
    """
    Location 11.
    """

    name = "Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest12(Location):
    """
    Location 12.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class North_River(Location):
    """
    Location 13.
    """

    name = "River"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing14(Location):
    """
    Location 14.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest15(Location):
    """
    Location 15.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Path16(Location):
    """
    Location 16.
    """

    name = "Path"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest17(Location):
    """
    Location 17.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Path18(Location):
    """
    Location 18.
    """

    name = "Path"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Log_Forest(Location):
    """
    Location 19.
    """

    name = "Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing20(Location):
    """
    Location 20.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Viper_Forest(Location):
    """
    Location 21.
    """

    name = "Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Swamp(Location):
    """
    Location 22.
    """

    name = "Swamp"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Path23(Location):
    """
    Location 23.
    """

    name = "Path"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Clearing24(Location):
    """
    Location 24.
    """

    name = "Clearing"
    descrip = """    The   
    There is """

    def action(self):
        pass


class Dense_Forest25(Location):
    """
    Location 25.
    """

    name = "Dense Forest"
    descrip = """    The   
    There is """

    def action(self):
        pass


class South_River(Location):
    """
    Location 26.
    """

    name = "\nRiver"
    descrip = """    This wide, unnamed river is deep and hazardous. The 
    far bank lies to the west of where you stand. This is one 
    of the relatively few rivers in the world that flow north.
    You are on the east bank.\n"""

    def travel(self, r):
        if "river" in r or ("north" in r or r == 'n'):
            return "You can only go downriver if you use the raft."
        elif "east" in r or r == 'e':
            return '27'
        elif "south" in r or r == 's':
            return "You cannot go upriver. The current is too swift."
        elif "west" in r or r == 'w':
            return "It is impossible to cross to the west bank of the river here."
        else:
            return None


class Vehicle_Clearing(Location):
    """
    Location 27. This is where the game always begins.
    """

    def __init__(self):
        self.first_visit = True
        
        self.raft = things.Raft()
        self.machete = things.Machete()
        self.jar = things.Sample_Jar()
        self.jerky = things.Beef_Jerky()
        self.flash = things.Flashlight()
        self.rope = things.Rope()
        self.whistle = things.Whistle()
        self.compass = things.Compass()
        
        self.items = [self.raft, self.machete, self.jar, self.jerky, 
                self.flash, self.rope, self.whistle, self.compass]

    name = "\nClearing"
    descrip = """    Your vehicle, a powerful but compact 4WD, is parked in
    a broad clearing at the end of a dirt track, which 
    disappears into the jungle to the north. A wide river 
    lies in front of you. The clearing extends to the south.\n"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '28'
        elif "east" in r or r == 'e':
            return "You can't go that way."
        elif "south" in r or r == 's':
            return '31'
        elif "river" in r or ("west" in r or r == 'w'):
            return '26'
        else:
            return None


class Dirt_Road(Location):
    """
    Location 28.
    """

    name = "\nDirt Road"
    descrip = """    This narrow, partly overgrown track extends straight 
    ahead into the jungle. This is the road that brought you
    to this lonely place, where you hope to find the greatest
    scientific discovery of your career.\n"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "You came from that direction in your 4WD."
        elif "east" in r or r == 'e':
            return "A deep ravine blocks your way."
        elif "south" in r or r == 's':
            return '27'
        elif "west" in r or r == 'w':
            return ("You can hear the river, but the forest growth is too thick. \nIt's impossible to break through in that direction.")
        else:
            return None


class Dense_Forest29(Location):
    """
    Location 29.
    """

    name = ""
    descrip = """    The   
    There is """

    def action(self):
        pass


class South_Bridge(Location):
    """
    Location 30.
    """

    name = "\nLog Bridge"
    descrip = """    This bridge (if you can call it a bridge) consists of   
    one very long log and a kind of rope made from twisted plant 
    fibers or thin vines. Moss covers the log, which is rather 
    narrow. The rope is strung between two upright trees so 
    you can hold on to it while crossing.\n"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return "If you went that way, you would be in the river."
        elif "east" in r or r == 'e':
            return '31'
        elif "south" in r or r == 's':
            return "If you went that way, you would be in the river."
        elif "west" in r or r == 'w':
            return "You can't go that way yet."
        else:
            return None


class Clearing31(Location):
    """
    Location 31.
    """

    name = "\nClearing"
    descrip = """    A small open space is hemmed in by jungle on all sides. 
    You can see your 4WD vehicle to the north. A bridge 
    lies to the west.\n"""

    def travel(self, r):
        if "north" in r or r == 'n':
            return '27'
        elif "east" in r or r == 'e':
            return "A deep ravine blocks your way."
        elif "south" in r or r == 's':
            return "The jungle is much too dense in that direction."
        elif "west" in r or r == 'w':
            return '30'
        else:
            return None


# dictionary for all locations 
loc_code_map = {
       '01' : Bongo_Glade(),
       '14' : Clearing14(),
       '20' : Clearing20(),
       '24' : Clearing24(),
       '31' : Clearing31(),
       '12' : Dense_Forest12(),
       '15' : Dense_Forest15(),
       '17' : Dense_Forest17(),
       '25' : Dense_Forest25(),
       '29' : Dense_Forest29(),
       '06' : Dense_Forest6(),
       '07' : Dense_Forest7(),
       '09' : Dense_Forest9(),
       '28' : Dirt_Road(),
       '10' : Falls(),
       '00' : Location(),
       '19' : Log_Forest(),
       '03' : North_Bridge(),
       '13' : North_River(),
       '11' : Panther_Forest(),
       '16' : Path16(),
       '18' : Path18(),
       '02' : Path2(),
       '23' : Path23(),
       '04' : Path4(),
       '05' : Path5(),
       '08' : Slope(),
       '30' : South_Bridge(),
       '26' : South_River(),
       '22' : Swamp(),
       '27' : Vehicle_Clearing(),
       '21' : Viper_Forest()
       }
