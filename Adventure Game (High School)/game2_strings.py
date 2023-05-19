### General Strings ###
from convert_image import *

main_menu_string = """                           
*************************************************************************
*               _____    ______   _____    _____   _   _                *
*              |  __ \  |  ____| |_   _|  / ____| | \ | |               *
*              | |__) | | |__      | |   | |  __  |  \| |               *
*              |  _  /  |  __|     | |   | | |_ | |   ` |               *
*              | | \ \  | |____   _| |_  | |__| | | |\  |               *
*              |_|  \_\ |______| |_____|  \_____| |_| \_|               *
*                                                                       *                
*                 (2022 Game - By Flynn Costello)                       *
*         o                                                             *
*      o^/|\^o             - Enter 'p' to play                          *
*   o_^|\/*\/|^_o          - Enter 'q' to quit                          *
*  o\*`'.\|/.'`*/o         - Enter 'l' for the games leaderboard        *
*   \/\/\/|\/\/\/          - Enter 'i' for game instructions            *
*    {><><@><><}                                                        *
*     ---------                                                         *
*                                                                       *
*                                                                       *   
*************************************************************************
"""

instructions_string = """

How to Play:
- The game involves you making a multitude of decisions based of a given scenario/event
- Once you have made a decision on a certain event the impacts of your decision will be revealed
- These impacts may be nothing or as severe as an instant death, so choose wisely
- After each event has occured a random amount of time will pass (in years) before the next begins
- Your aim is to survive and rule over the kingdom for as long as you can with the maximum length possible being 100 years
- There also may or may not be a secret ending somewhere in the game. Good Luck!

"""

loss = """
################        
## Game Over! ##
################
"""

win = """
################        
##  You Win!  ##
################        
"""




### Event String ###

# 1
event1_image = image1

event1_intro = """A stranger wanders into town on a horse and carrage. He travels through the town until he reaches the castle steps. Could he be an intruder? An assassin? Or maybe a shapeshifting sprite? Would you like to let him in?"""

event1_yes = """Luckily it is just a travelling merchant who would like to donate to your castle. He gives you 100 gold coins to add to your storage."""

event1_no = """Pity. It seems he was just trying to help you. Alas, he will just have to take his wealth elsewhere now. :("""

event1_yes_impacted_fields = ["w"]

event1_yes_impact_numbers = [10]

event1_no_impacted_fields = []

event1_no_impact_numbers = []


# 2
event2_image = image2

event2_intro = """A troll has been spotted under the local bridge and is scaring lots of the townsfolk. They are pleading for you to kill the beast. Would you like to send a squad of soldiers to deal with this issue?"""

event2_yes = """The troll proved to be a strong adversary taking out almost half the squad but was eventually dealt with and the townsfolk are much appreciative."""

event2_no = """Not your issue anyway is it? Well, apparently it was. Following your decision to not kill the troll, it went on to murder and eat another ten villagers. The villages are angry and hate you now."""

event2_yes_impacted_fields = ["d", "h"]

event2_yes_impact_numbers = [-10, 25]

event2_no_impacted_fields = ["h"]

event2_no_impact_numbers = [-40]

# 3
event3_image = image3

event3_intro = """The Priests of the castle wish to extend the Church by adding another floor to it. They believe it will 'allow them to be closer with God'. Do you wish to give them the gold necessary?"""

event3_yes = """The Priests are much appreciative and ensure that it will help the Kingdom."""

event3_no = """The Priests are angry that you did not wish to support them in their endeavours. As such, they begin to spread rumours of your lack of attendance at Church lately, much to the suprise of you citizens."""

event3_yes_impacted_fields = ["r", "w"]

event3_yes_impact_numbers = [30, -15]

event3_no_impacted_fields = ["r", "h"]

event3_no_impact_numbers = [-5, -5]

# 4
event4_image = image4

event4_intro = """News has come that a dragon has recently attacked a neighbouring Kingdom and destroyed all its army and defences. You feel that this could be your chance to strike and take the Kingdom as your own. Do you send troops?"""

event4_yes = """As the troops approached the presumed 'destroyed' castle they quickly realised it was a trap but sadly it was too late. In a matter of moments your troops were killed and supplies taken by the castle."""

event4_no = """Honestly who cares about the other Kingdoms. My Kingdoms the best anyway."""

event4_yes_impacted_fields = ["w", "d"]

event4_yes_impact_numbers = [-10, -30]

event4_no_impacted_fields = []

event4_no_impact_numbers = []

# 5
event5_image = image5

event5_intro = """An earthquake suddenly shakes the Kingdom leaving many injured and the castle free for pillaging. Would you like to save the injured but risk pillaging?"""

event5_yes = """The guards quickly help the injured citizens and bring them to safety. However, whilst they were being saved, the castle was pillaged and the gold storage was almost emptied. You are now broke."""

event5_no = """Leaving your citizens to die was a bad decision. While your castle remained secure from pillagers, the families of your guards and servents were dying. They are all furious and will likely rebel. Better watch your back from now on..."""

event5_yes_impacted_fields = ["h", "w"]

event5_yes_impact_numbers = [30, -70]

event5_no_impacted_fields = ["h", "r"]

event5_no_impact_numbers = [-20, -40]

# 6
event6_image = image6

event6_intro = """In the dead of night you are suddenly attacked by a masked assassin. He says he will spare your life for a thousand gold but your not sure if you can trust him. Do you give him the gold and hope he stays true to his word?"""

event6_yes = """After grabbing the gold he quickly mutters something under his breath before plunging a dagger into you. What can you expect from a masked assissin I guess."""

event6_no = """In a split second decision you smash the masked assassin across the head with the bag of gold and run away. Luckily you escape and the man is captured."""

event6_yes_impacted_fields = [False]

event6_yes_impact_numbers = [False]

event6_no_impacted_fields = []

event6_no_impact_numbers = []

# 7
event7_image = image7

event7_intro = """Following Summer your lands have suddenly become full of plague and disease. Luckily a strange witch shows up on your doorstep and offers to help you with this problem. The Church forbids you from accepting her offer but she guarantees she will fix the problem. Do you let her help?"""

event7_yes = """The Church are ashamed of your decision and leave the castle entirely. However, the witches magic works and your people are healthy again!"""

event7_no = """Plague and disease continues to overcome your Kingdom. It takes almost three years for the impacts of such illness to stop but by then the damage has been done. Half your army and a third of your entire Kingdom is dead."""

event7_yes_impacted_fields = ["d", "h", "r"]

event7_yes_impact_numbers = [10, 25, -40]

event7_no_impacted_fields = ["d", "h"]

event7_no_impact_numbers = [-15, -30]

# 8
event8_image = image8

event8_intro = """Looking out at your Kingdom from the castle's watchtower you are suddenly greated by a devlish looking creature. Maybe the priests were right after all? Anyway, the creature quickly reveals that he has captured your daughter and in order to save her you must slaughter half of your army! Your people will hate you and surly overthrow you! Do you follow through with what the creature has requested and save your daughter?"""

event8_yes = """After doing what was needed you learn that the creature was only lying. Your daughter was asleep in her room right next to you the whole time. Oh no. Banging of the throne room doors is only momentary before you feel the sharp edge of a blade pierce your skin as the Kingdom's peasants storm the castles gates in rebellion for the blood you have taken from their families! You Died!"""

event8_no = """Luckily the creature was just bluffing. Your daughter was fine after all. Phew!"""

event8_yes_impacted_fields = [False]

event8_yes_impact_numbers = [False]

event8_no_impacted_fields = []

event8_no_impact_numbers = []

# 9
event9_image = image9

event9_intro = """King Edmund from the Empire of Lais has offered you a trade. 1000 of your men for all the wealth you could ever ask for. Do you accept?"""

event9_yes = """Luckily King Edmund stuck to his word and delivered as promised. 10,000 golden coin in return for the troops. Your citizens aren't sure if they're happy or sad for this trade. They just seem to accept it I guess."""

event9_no = """Edmund understands your decision. He hopes you can reconsider at a later time though."""

event9_yes_impacted_fields = ["w", "d"]

event9_yes_impact_numbers = [60, -50]

event9_no_impacted_fields = []

event9_no_impact_numbers = []

# 10
event10_image = image10

event10_intro = """The widely hated King of Luceras has offered you a proposal. He offers you the hand of his daughter Luna, in return for a merging of your two great Kingdoms. He also promises ten thousand gold and a thousand more troops to be sent as a wedding gift. Do you accept his proposal?"""

event10_yes = """Congratulations! You and Lunar are now married. Your gold and extra soldiers have also arrived bringing further wealth and security to your lands. However your people depise Luna due to her father and hate that you've married her and made an deal with such a horrible man."""

event10_no = """Unfortunately the King of Luceras doesn't take kindly to your rejection. He wages war on your Kingdom! His forces are too strong and overwhelm the castle! Your Kingdom is destroyed and your rotting head is left on a spike outside the castle's gates. You Died!"""

event10_yes_impacted_fields = ["w", "d", "h"]

event10_yes_impact_numbers = [20, 20, -20]

event10_no_impacted_fields = [False]

event10_no_impact_numbers = [False]

# 11
event11_image = image11

event11_intro = """On a hunting trip in the Evergail Forest you have suffered a horrible injury. All doctors in the Kingdom say they cannot help you, but a witchdoctor says you will have a chance if she helps. The church are not happy that you have even considered her. Do you accept her offer?"""

event11_yes = """You are healed! The church hates you though."""

event11_no = """Unsurprisingly prayer was not enough to heal your fatal wounds. You Died!"""

event11_yes_impacted_fields = ["r"]

event11_yes_impact_numbers = [-30]

event11_no_impacted_fields = [False]

event11_no_impact_numbers = [False]

# 12
event12_image = image12

event12_intro = """A hoard of zombies has been spotted eating animals in Forest Black, east of the castle. Would you like to send a party of soldiers to deal with the hoard?"""

event12_yes = """Unfortunately sending only 10 men wasn't enough! They are all turned into zombies and are now attacking the castle. After much loss, the hoard are finally silenced but your kingdom is in ruin!"""

event12_no = """Thankfully the hoard have kept to the forest however the church and your people are still angry you didn't deal with them. Hopefully this decision doesn't bite you in the back later..."""

event12_yes_impacted_fields = ["w", "d", "h"]

event12_yes_impact_numbers = [-30, -40, -30]

event12_no_impacted_fields = []

event12_no_impact_numbers = []

# 13
event13_image = image13

event13_intro = """Overcrowding in the Kingdom has led to unsanitary conditions and an increase in disease. Would you like to force some of your citizens outside the castle walls to reduce this level of disease?"""

event13_yes = """After much anger and frustration your citizens agree, however request you pay them. You do so to ensure rioting does not occur."""

event13_no = """Disease continues to spread and populations dwindle. The disease also spreads to the Church making the Priests furious at you."""

event13_yes_impacted_fields = ["w", "h"]

event13_yes_impact_numbers = [-20, -10]

event13_no_impacted_fields = ["h", "r"]

event13_no_impact_numbers = [-20, -20]

# 14
event14_image = image14

event14_intro = """The Church wishes to be given more power in the Kingdom and offer a co-leadership scheme where they control the wealth and you control the Kingdom's decisions. Do you accept?"""

event14_yes = """The Church are much pleased and ensure the wealth will be used well. However, only days later they reveal they've spent most of the vault's supplies on a golden statue for the church. Oh no."""

event14_no = """The Church are furious that you would deny their offer. They say that you are not only denying them, but God too in the process."""

event14_yes_impacted_fields = ["r", "w"]

event14_yes_impact_numbers = [30, -40]

event14_no_impacted_fields = ["r"]

event14_no_impact_numbers = [-50]

# 15
event15_image = image15

event15_intro = """A group of people have become enraged at the news that a little boy was killed by a witch. They begin hunting and burning women they percieve to be witches. Do you allow them to proceed with their actions?"""

event15_yes = """The group continue their mission. In total they kill 23 women before they realise what actually killed the little boy was poisonous berries, not a witch! The families of those killed are furious. They want the heads of all the people in the group!"""

event15_no = """The group rebel against your decision and began an all out riot with the castle's guards. In the end, your troops finish of the group, however experience significant casualities too."""

event15_yes_impacted_fields = ["h"]

event15_yes_impact_numbers = [-30]

event15_no_impacted_fields = ["d", "h"]

event15_no_impact_numbers = [-10, 10]

# 16
event16_image = image16

event16_intro = """Rumours of a vampire have surfaced in the outskirts of your Kingdom. People are scared and want you to investiage. Do you send a group of troops to investigate?"""

event16_yes = """The troops not only find a single vampire but a whole nest. Being quickly overwhelmed they only have time to send a single messanger pigeon to warn the capital. Gaining news of this nest of vampires you send a thousand men to deal with them. Only 20 return but the vampires have been killed."""

event16_no = """Seems it was just a false rumour as you never hear of any vampire problems again."""

event16_yes_impacted_fields = ["d", "h"]

event16_yes_impact_numbers = [-60, 30]

event16_no_impacted_fields = []

event16_no_impact_numbers = []

# 17

event17_image = image17

event17_intro = """A witch has been identified in the castle and the church wish for you to make an exmaple of her. Do you follow through with this execution?"""

event17_yes = """The Church are pleased at your commitment to God. However, some of your citizens feel you are abusing your power."""

event17_no = """The Church are furious you would let such a person remain freely in the capitol. They warn you of the consequences if you continue to disobey them."""

event17_yes_impacted_fields = ["r", "h"]

event17_yes_impact_numbers = [30, -10]

event17_no_impacted_fields = ["r"]

event17_no_impact_numbers = [-40]

# 18
event18_image = image18

event18_intro = """Lately you have heard rumours of mythical place that some say could 'beat death'. The Fountain of Youth! The church tells you it is foolish to follow such a path as doing so would go against God. Do you follow the rumours and begin your search for the fountain?"""

event18_yes = """Leaving to find the fountain of youth the church condems your name and banishes you. Guess all you have now is the fountain. After travelling for almost a year you reach the mountain it is said to be within and before long you find it. Taking a sip from it you feel refreshed and amazing! You are now immoratal! Years pass. You return to your Kingdom only to see it in ruins. You wait... New kingdoms are formed and old ones are destroyed. You do not age or change. Hundred of years pass, the landscapre changes, evolves. You do not change. You realise what this means. You will be but a ghost in humanity... in the universe. Forever."""

event18_no = """The Church are happy. Surely it's not real anyway. Right?"""

event18_yes_impacted_fields = [False]

event18_yes_impact_numbers = [False]

event18_no_impacted_fields = ["r"]

event18_no_impact_numbers = [30]

# 19
event19_image = image19

event19_intro = """A spirit appears to you one day and offers you a choice. For all the power in the world all the spirit needs is your soul. It tells you of all the great things you could do with such power. Conquer Kingdoms, rule Continents and even become a God! Do you accept such an offer?"""

event19_yes = """Your newfound power gives you the ability to conquer lands, conquer Kingdoms, and conquer the ENTIRE WORLD! But after it all, you still feel empty, alone. Maybe the power wasn't worth it. Years later you die of lonliness in your castle walls."""

event19_no = """Your peoeple think you are a fool for not accpeting the offer but you know it was the right decision."""

event19_yes_impacted_fields = [False]

event19_yes_impact_numbers = [False]

event19_no_impacted_fields = ["h"]

event19_no_impact_numbers = [-10]

# 20
event20_image = image20

event20_intro = """Your old enemy King Ezekiel sends a message warning of his armies might. He says that if you don't give him your head he will invade and conquer your lands, murdering all your citizens and burning your castle to the ground. Do you sacrifice yourself to save your lands?"""

event20_yes = """I'd love to say your sacrifice was worth it but only a few days later Ezekiel's army arrives and burns your Kingdom to the ground. You Died!"""

event20_no = """After rejecting his proposal your people label you a coward and rebel against you. After taking control of the castle they kill you and send your head anyway. You Died!"""

event20_yes_impacted_fields = [False]

event20_yes_impact_numbers = [False]

event20_no_impacted_fields = [False]

event20_no_impact_numbers = [False]




