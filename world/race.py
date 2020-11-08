"""
Holds information regarding races of the scrolls
"""

from typeclasses.scripts import Script


class RaceInfo(Script):
    def at_object_creation(self):
        self.reset()

    def reset(self):
        self.db.races = {
            'altmer': {
                'desc':
                """
                The Altmer (or High Elves, as they are also known) are a race of Mer that make their home on Summerset Isle, an island off the south western coast of Tamriel. Many races of Tamriel consider the Altmer to be quite beautiful due to their fair, golden skinned complexion and the dazzling gem like colors of their eyes; as such, the Altmer are welcome guests in most parts of Tamriel, save for the Black Marsh and Vvardenfell.  However, the combination of their fair appearance, long lives, propensity for magic and resemblance to the Old Elves of Tamriel tends to give Altmer an elevated sense of their own importance. This can sometimes impact diplomatic relations with the other races.The use of magic is heavily emphasized in Altmer society,  given the latent magical gifts of the Altmer race. Those Altmer that rarely or never leave Summerset Isle are used to a culture in which Magic permeates every level of society. Unfortunately, the natural affinity of the Altmer race also leaves them vulnerable to magical attack; however, most choose to pay little heed to this drawback. Aside from their dependence on magic, Altmer also tend to place a high cultural value on living for as long as possible, often using magic to extend their longevity. Altmer born and raised on Summerset Isle tend to be haughty and more out of touch than those raised in other areas of Tamriel.
                """.strip(),
                "sdesc":
                "high elves",
                'stats': {
                    'str': 20,
                    'end': 23,
                    'agi': 23,
                    'int': 30,
                    'wp': 28,
                    'prc': 25,
                    'prs': 25
                },
                'traits': {},
                'powers': {}
            },
            'argonian': {
                'desc':
                """
                Argonians are a race of reptilian humanoids native to the land of Black Marsh in south-eastern Tamriel. In Jel, their native tongue, Argonians refer to themselves as Saxhleel (meaning “People of the Root”) to show their absolute reverence towards and dependence on a the Hist, a species of sentient trees that share a singular and extremely intelligent mind. The Argonian people owe the entirety of their life, culture and shape to the Hist, as the sap of the trees is a necessary catalyst for the metamorphosis of young Argonians into their humanoid form. Traditionally minded Argonians also believe the Hist is a repository for their souls, reincarnating them after death.Argonians are naturally suited to the dangerous environment of Black Marsh and are resistant to most diseases and poison. Additionally, Argonians have the ability to breathe indefinitely while underwater, as well as formidable resistance to many kinds of damage courtesy of the Hist. In their homeland, Argonians tend to live in either desolate, scattered villages or within the ruins of great cities of stone, remnants of the Elves and other extinct denizens of the Black Marsh. Given the necessity of the Hist to their lifestyle, most Argonians rarely leave Black Marsh by choice; however, some have been known to aban-don Argonian society and venture out into the wider world as adventurers and hired workers. Unfortunately, others are sometimes forcibly removed from Black Marsh by slavers and sold as chattel across Tamriel
                """.strip(),
                "sdesc":
                "reptilian humanoids",
                'stats': {
                    'str': 25,
                    'end': 24,
                    'agi': 28,
                    'int': 27,
                    'wp': 24,
                    'prc': 25,
                    'prs': 22
                },
                'traits': {},
                'powers': {}
            },
            'bosmer': {
                'desc':
                """
                The Bosmer (or Wood Elves, as they are also known) are a race of forest-dwelling Mer native to the province of Valenwood.  In their own tongue, the Bosmer refer to themselves as the Boiche, or “Tree-Sap People”, a reference to their pact with the Aedra Y’ffre. Like other elves, the Bosmer were originally from the Summerset Isles; however, the Wood Elves scorned strict and formal lifestyle of their Aldmeri ancestors, choosing to travel to mainland Tamriel and live more carefree and simple lives. Chronologically, the First Era is officially marked as starting when the Bosmer united under the rule of the King Eplear, the first of the Camoran Dynasty. Bosmer are known across Tamriel as competent and deadly bow users; some rumors even claim that the Wood Elves were the first to have invented and used the bow as a weapon.Despite the high status granted to Auri-El by most of the Merish pantheons, the Bosmer hold Y’ffre in the highest regard. As the first of the Aedra to help stabilize Nirn by becoming an earthbone, Y’ffre helped the Wood Elves maintain their shape during the Dawn Era. The grateful Bosmer accepted his patronage, making an oath known as the Green Pact and vowing to never eat nor harm any vegetation that grew within Valenwood (though other plants outside the province have no such protection). Because of their oath, those Bosmer native to Valenwood (and even some who leave) are carnivorous, even engaging in cannibalism on occasion
                """.strip(),
                "sdesc":
                "wood elves",
                'stats': {
                    'str': 21,
                    'end': 21,
                    'agi': 31,
                    'int': 25,
                    'wp': 23,
                    'prc': 26,
                    'prs': 24
                },
                'traits': {},
                'powers': {}
            },
            'breton': {
                'desc':
                """
                The Bretons are a race of men native to the north western prov-ince of High Rock. Bretons as a whole are generally dark-haired, tall and gifted with a rare amount of intelligence and willpower compared to the other races of men across Tamriel. Despite their height, Bretons tend to have a slighter build, being less muscular than Redguards or Nords. Bretons are descended from both Aldmeri and Nedic bloodlines, giving them a unique combination of abilities that both enhances their innate Aldmeri talent for magic and suppresses their vulnerability to magic, thanks to their Nedic heritage.  Culturally, Bretons possess a great love of art and philosophy, as well as an innate connection with magic; this leads many to scholarly pursuits, becoming great wizards and sorcerers. Bretons are also prone to engaging in knightly pursuits, driven on by a “quest-obsession” to do good deeds prevalent throught Breton society.Also worthy of mention are the Reachmen, a splinter group of Bretons inhabiting the western reach that joins High Rock and Skyrim. Violently opposed to the Breton kingdoms and infighting of High Rock, the Reachmen have formed a tribal society based on hedge magic learned from Orcs and bird-witches known as Hagravens. Though far more ferocious than their cultured cousins, the Reachmen live far more primitive lives, trading the steel blades of High Rock for stone and bone, the castles and towers for natural caverns.
                """.strip(),
                "sdesc":
                "hybrid of man and mer",
                'stats': {
                    'str': 23,
                    'end': 21,
                    'agi': 22,
                    'int': 28,
                    'wp': 30,
                    'prc': 25,
                    'prs': 25
                },
                'traits': {},
                'powers': {}
            },
            'dunmer': {
                'desc':
                """
                The Dunmer (or Dark Elves, as they are also known) are a race of xenophobic Mer native to the province of Morrowind,  a land dominated by a wasteland of dust and fire. Like other elves, the Dunmer were originally from the Summerset Isles; however, they are descended from the Chimer, a tribe of Aldmeri exiles who fled Summerset to worship the Daedra, who they title “Our Stronger, Better Ancestors”. An agile and graceful people, the Dunmer use their natural magical and physical abilities to their advantage in combat. Physically their swordsmanship rivals that of the Redguards of Hammerfell, while their natural affinity for Destruction magic is rivaled only by their distant cousins in the Summerset Isles.Dunmer society is divided into two distinct areas: the more civilized Great Houses and the nomadic Ashlanders. The Great Houses of Morrowind behave more like nations than states, divided as they are by both culture and politics. The only things which unite the Great Houses are the temple and an almost universal distaste for outlanders. By contrast to the more civilized and political Great Houses, Ashlander society is more tribal-oriented and nomadic. The Ashlanders split from the society of the Great Houses over the validity of the Temple’s doctrine, a conflict which has divided the two sectors of Dunmer society ever since. Those who have met the Ashlanders describe them as ferocious, chitin-armored savages who are wary of strangers; however, beneath the xeno-phobic surface of Ashlander society lies a deeply spiritual and disciplined lifestyle, a vital key to the survival of the nomads in the harsh land of Morrowind.
                """.strip(),
                "sdesc":
                "dark elves",
                'stats': {
                    'str': 25,
                    'end': 24,
                    'agi': 29,
                    'int': 25,
                    'wp': 24,
                    'prc': 25,
                    'prs': 23
                },
                'traits': {},
                'powers': {}
            },
            'colovian': {
                'desc':
                """
                Imperials (also known as Cyrods) are a race of men descended from Nedics who settled in the province of Cyrodiil, most notably Nibenese and Colovians. From the time of the Merethic Era the Imperials were held in slavery by the Ayleids (also known as the Heartland High Elves) until a Nedic woman by the name of Alessia organized a successful slave revolt with the help of her champion Pelinal Whitestrake and demigod Morihaus.Following the revolt, the Cyrods set up three different empires under three different factions: Alessia and her followers, the Reman Dynasty and the Septim Dynasty. Though the empires had internal differences, more stark differences arose between the more mercantile Nibenese and the rougher Colovians. Where the Nibenese Imperials were skilled at trading the creation of wealth, the Colovian Imperials were influenced by their northern Nordic neighbors, turning to more physical pursuits such as farming and war. In fact, such differences kept the Imperials from becoming a unified people until the arrival of Reman Cyrodiil in the First Era and the warrior King Cuhlecain at the end of the Second Era. Due to the central position of Cyrodiil in Tamriel, Cyrods have learned to become shrewd traders and diplomats. The more Nordic Imperials, Colovians are rougher and more physical than their Nibenese counterparts. The Nibenese are more cosmopolitan than their Colovian bretheren, and have excelled in trade and other such pursuits
                """.strip(),
                "sdesc":
                "countryside human",
                'stats': {
                    'str': 26,
                    'end': 27,
                    'agi': 24,
                    'int': 24,
                    'wp': 24,
                    'prc': 25,
                    'prs': 25
                },
                'traits': {},
                'powers': {}
            },
            'nibenese': {
                'desc':
                """
                Imperials (also known as Cyrods) are a race of men descended from Nedics who settled in the province of Cyrodiil, most notably Nibenese and Colovians. From the time of the Merethic Era the Imperials were held in slavery by the Ayleids (also known as the Heartland High Elves) until a Nedic woman by the name of Alessia organized a successful slave revolt with the help of her champion Pelinal Whitestrake and demigod Morihaus.Following the revolt, the Cyrods set up three different empires under three different factions: Alessia and her followers, the Reman Dynasty and the Septim Dynasty. Though the empires had internal differences, more stark differences arose between the more mercantile Nibenese and the rougher Colovians. Where the Nibenese Imperials were skilled at trading the creation of wealth, the Colovian Imperials were influenced by their northern Nordic neighbors, turning to more physical pursuits such as farming and war. In fact, such differences kept the Imperials from becoming a unified people until the arrival of Reman Cyrodiil in the First Era and the warrior King Cuhlecain at the end of the Second Era. Due to the central position of Cyrodiil in Tamriel, Cyrods have learned to become shrewd traders and diplomats. The more Nordic Imperials, Colovians are rougher and more physical than their Nibenese counterparts. The Nibenese are more cosmopolitan than their Colovian bretheren, and have excelled in trade and other such pursuits
                """.strip(),
                "sdesc":
                "cosmopolitan human",
                'stats': {
                    'str': 24,
                    'end': 23,
                    'agi': 23,
                    'int': 27,
                    'wp': 23,
                    'prc': 25,
                    'prs': 30
                },
                'traits': {},
                'powers': {}
            },
            'khajiit': {
                'desc':
                """
                Khajiit are a race of feline humanoids native to the province of Elsweyr in southern Tamriel. In their native tongue of Ta’agra, the word Khajiit means “desert walkers”, a fitting epithet for the nomadic race. Unlike the other races of Tamriel, there are variety of different “breeds” of Khajiit, ranging from bipedal to quadrupedal, the size of tigers to the size of house cats, and many in between. Some are even unable to speak, while others are hard to distinguish from elves. All of these things and more are determined by the moons, cementing their place at the center of Khajiit society. Aside from determining a given Khajiit’s form and abilities, the moons also form the basis of the Khajiit’s governmental system.Most Khajiit value agility and cunning above brute force, as these traits are valuable assets for survival in the harsh deserts and tropical jungles the Khajiit call home. Their natural acrobatic ability, intelligence and unmatched agility make the Khajiit excellent guerrilla fighters, adventurers and thieves.
                """.strip(),
                "sdesc":
                "feline humanoids",
                'stats': {
                    'str': 22,
                    'end': 22,
                    'agi': 29,
                    'int': 25,
                    'wp': 21,
                    'prc': 28,
                    'prs': 24
                },
                'traits': {},
                'powers': {}
            },
            'nord': {
                'desc':
                """
                The Nords are a race of tall, fair haired men hailing from Skyrim but found all along the coasts of Tamriel. Originating from the continent of Atmora, the Nords are a fierce and proud people, known for their natural aptitude as both warriors and seafar-ers. Possessing great physical strength and endurance, Nords also enjoy impressive resistance to magical frost and lightning. Natural conquerors, the warlike and enterprising spirit of the Nords has greatly influenced the history of Tamriel since their arrival from Atmora in the late Merethic Era, with their armies driving the Snow Elves into ruin and providing the strength and impetus to forge the first empires of man. The Nords consider themselves the sons and daughters of Kyne, formed when the great Northern Winds broke upon the ground at the Throat of the World. As such, they consider their breath their very essence, and are able to channel their strength and power into their voices in magical shouts known as the Thu’um. Though all Nords possess the potential to use the Thu’um, it has become increasingly rare since the fall of the first Empire of the Nords when it was deemed it should only be used in times of great need.Honor and heroism are important virtues to a Nord, for they believe that an honorable life or a valiant death will grant them access to Sovngarde, Shor’s Hall. This belief makes Nords all but fearless in battle, making war with an energy and enthusiasm that terrifies their enemies. This leads many down the path of the warrior; consequently, most Nords encountered outside Skyrim pursue some martial enterprise, be it sellsword, brigand, or wandering adventurer.
                """.strip(),
                "sdesc":
                "sons and daughters of skyrim",
                'stats': {
                    'str': 30,
                    'end': 28,
                    'agi': 23,
                    'int': 21,
                    'wp': 24,
                    'prc': 25,
                    'prs': 23
                },
                'traits': {},
                'powers': {}
            },
            'orsimer': {
                'desc':
                """
                The Orcs, sometimes known as Orsimer, consist of barbaric tribes found in the north of Tamriel, concentrated in High Rock’s Wrothgarian mountain range and with settlements in High Rock, Skyrim, and Hammerfell. Known for their ugly appearance (including but not limited to green or red skin, prominent tusks, and unusual facial bone structure), propensity for violence, and skill in metalcraft, the Orcs are commonly held to be the least of the races. Although officially accepted as citizens by the Cyrodiilic Empire after the events of the Warp in the West, Tamriel’s populace still holds them in low regard, especially in the northwest. With the few exceptions of those living in cities or camps, most Orcs hail from Orsinium or a Stronghold, where they are raised from birth to defend their clan and family.Orcs have been bred for centuries to survive harsh conditions and constant assault, and as such have a natural proficiency in hand-to-hand combat. Their sheer physical strength makes them formidable opponents when wearing heavy armor and wielding two-handed weapons, especially when using products of their own design. Most Orcs learn to work metal from a young age, and even those who do not choose the smithing profession have better skill to maintain their equipment. Orcs hailing from wilderness Strongholds are generally more ferocious than their Orsinium cousins, who tend to have more skill as craftsmen
                """.strip(),
                "sdesc":
                "Orcs",
                'stats': {
                    'str': 28,
                    'end': 30,
                    'agi': 22,
                    'int': 23,
                    'wp': 26,
                    'prc': 24,
                    'prs': 22
                },
                'traits': {},
                'powers': {}
            },
            'redguard': {
                'desc':
                """
                The Redguards originated from the continent of Yokuda, far to Tamriel’s west. They are renowned sword masters and forged an empire on Yokuda to rival Tamriel’s own. Following a disaster which destroyed most of their homeland, the emigrated east to Tamriel, where they landed on Hammerfell. In Hammerfell, Redguard society split into two main camps; Forebears, those who had come in the Warrior Wave to purge Hammerfell of inhabitants, and Crowns, the upper-class who had followed.The Redguards maintain a strong tradition of sword-mastery and honor to this day, though the significant Redguard piracy presence suggests interesting definitions of honor. Redguard warriors are at their best when using their famed scimitars, typically singly with a shield (though there are those who fight with two scimitars, known as “dervishes”). They prefer lighter armors and cloth to heavy metal, allowing for freedom and rapidity of movement. Redguards make for strong individual warriors, though only rarely does one find a Redguard who is not part of a society or band. They are known for their strict code of battlefield ethics, preferring to fight honorably even against creatures they see as below them.
                """.strip(),
                "sdesc":
                "sword masters",
                'stats': {
                    'str': 27,
                    'end': 28,
                    'agi': 26,
                    'int': 22,
                    'wp': 23,
                    'prc': 25,
                    'prs': 24
                },
                'traits': {},
                'powers': {}
            }
        }