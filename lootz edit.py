import subprocess
import sys
import os
import tempfile
import tkinter as tk
from tkinter import scrolledtext

# Embedded original loot generator script
CLI_SCRIPT = '''
#Loot Roller
#system - windows
#interface - cmd
#req - roll loot for one encounter based on level

#get user input
varEL=input('Encounter level? (1-30) ')
varEL=int(varEL)

#call random module
import random   

#create loop for multiple rolls
while True:

                
        
        #print separator
        print("")
        
        #ROLL FOR common coins
        varCommonCoins=(random.randint(1,20)) + (varEL)
        if varCommonCoins <= 7:
                print("You recieve no common coins.")
        if varCommonCoins >= 8 and varCommonCoins <= 14:
                print("You recieve", (varEL * (random.randint(1,6))) * (random.randint(1,6)), "bits and", (random.randint(1,6)), "pence.")
        if varCommonCoins >= 15 and varCommonCoins <= 19:
                print("You recieve", (varEL * (random.randint(1,6))) * (random.randint(1,6)), "pence and", (random.randint(1,6)), "bits.")
        if varCommonCoins >= 20:
                print("You recieve", (varEL * (random.randint(1,6))) * (random.randint(1,6)), "copper and", (random.randint(1,6)), "pence.")

        #ROLL FOR rare coins
        varRareCoins=(random.randint(1,20)) + (varEL)
        if varRareCoins <=13:
                print("You receive no rare coins.")
        if varRareCoins >= 14 and varRareCoins <= 20:
                print("You recieve", (varEL * (random.randint(1,6))) * ((random.randint(1,6))+(random.randint(1,6))), "copper and", (random.randint(1,8)), "pence.")
        if varRareCoins >= 21 and varRareCoins <= 29:
                print("You recieve", (varEL * (random.randint(1,6))) * (random.randint(1,6)), "silver and", (random.randint(1,6)), "copper.")
        if varRareCoins >= 30 and varRareCoins <= 35:
                print("You recieve", (varEL * (random.randint (1,6))) * (random.randint(1,4)), "gold and", (random.randint(1,8)), "silver.")
        if varRareCoins >= 36:
                print("You receive", (varEL * (random.randint(1,6))) * (random.randint(1,3)), "platinum and", (random.randint(1,10)), "gold.")
        
        #print a space to break up the coins and gems/art
        print("-----------------------------------")    

        #list of gems
        varOrnamentalGemsList = ['turqoise', 'banded agate', 'moss agate', 'eye agate', 'azurite', 'bloodstone', 
                        'carnelian', 'jasper', 'chalcedony', 'chrysoprase', 'citrine', 'hematite', 'iolite', 
                        'lapis lazuli', 'malachite', 'moonstone', 'obsidian', 'onyx', 'freshwater pearl', 
                        'blue quartz', 'rose quartz', 'star quartz', 'rhodochrosite', 'sard', 'tiger eye']
        varSemipreciousGemsList = ['alexandrite', 'amber', 'amethyst', 'aquamarine', 'chrysoberyl', 'red coral', 
                        'white coral', 'violet garnet', 'red garnet', 'brown-green garnet', 'jade', 'jet', 
                        'white pearl', 'black pearl', 'gold pearl', 'pink pearl', 'silver pearl', 'red spinel', 
                        'red-brown spinel', 'deep blue spinel', 'deep green spinel', 'golden topaz', 'tourmaline']
        varPreciousGemsList = ['blue amber', 'star ruby', 'emerald opal', 'white opal', 'black opal', 'fire opal',
                        'blue sapphire', 'blue star sapphire', 'black star sapphire', 'bright emerald', 'thunder opal', 
                        'blue-white diamond', 'pink diamond', 'blue diamond', 'chocolate diamond', 'jacinth',
                        'flawless black pearl', 'flawless golden pearl', 'green pearl', 'purple pearl', 'blue pearl']
        
        #get gem multipliers
        OrnNum=(random.randint(1,3)) + (random.randint(-2,1)) 
        SemPrecNum=(random.randint(1,3)) + (random.randint(-2,1))
        PrecNum=(random.randint(1,3)) + (random.randint(-2,1))
                
        #ROLL FOR gems and art
        varGemsArt=(random.randint(1,20)) + varEL

        #no gems, get rekt scrub
        if varGemsArt <= 16:
                print("You recieve no gems or art objects.")
        
        #get for ornamental gems
        if varGemsArt >= 17 and varGemsArt <= 21:
                print("You recieve a", random.choice(varOrnamentalGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "pence.")
                if OrnNum >= 2:
                        print("You recieve a", random.choice(varOrnamentalGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "pence.")
                if OrnNum >= 3:
                        print("You recieve a", random.choice(varOrnamentalGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "pence.")
                if OrnNum >= 4:
                        print("You recieve a", random.choice(varOrnamentalGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "pence.")        
                if OrnNum >= 5:
                        print("You recieve a", random.choice(varOrnamentalGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "pence.")
                if OrnNum >= 6:
                        print("You recieve a", random.choice(varOrnamentalGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "pence.")        
        
        #get semi precious gem
        if varGemsArt >= 22 and varGemsArt <= 26:
                print("You recieve", random.choice(varSemipreciousGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "copper.")
                if SemPrecNum >= 2:
                        print("You recieve a", random.choice(varSemipreciousGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "copper.")
                if SemPrecNum >= 3:
                        print("You recieve a", random.choice(varSemipreciousGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "copper.")
                if SemPrecNum >= 4:
                        print("You recieve a", random.choice(varSemipreciousGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "copper.")
                if SemPrecNum >= 5:
                        print("You recieve a", random.choice(varSemipreciousGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "copper.")
                if SemPrecNum >= 6:
                        print("You recieve a", random.choice(varSemipreciousGemsList), "worth", (varEL * ((random.randint(1,6)) + random.randint(1,6))), "copper.")
                        
        #get decorative art     
        if varGemsArt >= 27 and varGemsArt <= 31:
                print("You recieve", (random.randint(1,3)), "piece(s) of decorative art worth", (random.randint(1,20)) * (varEL), "silver in total.")
                
        #get precious gems
        if varGemsArt >= 32 and varGemsArt <= 36:
                print("You recieve", random.choice(varPreciousGemsList), "worth", (varEL * ((random.randint(1,4)) + random.randint(1,4))), "gold.")
                if SemPrecNum >= 2:
                        print("You recieve a", random.choice(varPreciousGemsList), "worth", (varEL * ((random.randint(1,4)) + random.randint(1,4))), "gold.")
                if SemPrecNum >= 3:
                        print("You recieve a", random.choice(varPreciousGemsList), "worth", (varEL * ((random.randint(1,4)) + random.randint(1,4))), "gold.")
        
        #get fine art
        if varGemsArt >= 37:
                print("You recieve an object of fine art worth", (random.randint(1,20) * (varEL)), "gold.")

        print("-----------------------------------")    

        #START MAGIC ITEM SECTION
        varMagicQuality=""
        
        #spell lists (can be called from other sections)
        varFirstLevelSpells = ['Alarm', 'Animal Friendship', 'Bless', 'Burning Hands', 'Cause Fear', 'Charm Person', 
                        'Color Spray', 'Command', 'Comprehend Languages', 'Create or Destroy Water', 'False Life', 'Cure Wounds I', 
                        'Protection from Evil', 'Detect Good & Evil', 'Detect Magic', 'Detect Poison & Disease', 'Disguise Self', 
                        'Divine Favor', 'Entangle', 'Faerie Fire', 'False Life', 'Feather Fall', 'Fog Cloud', 'Cure Wounds I', 
                        'Goodberry', 'Grease', 'Gust of Wind', 'Healing Word I', 'Identify', 'Inflict Wounds I', 'Longstrider', 
                        'Magic Missile I', 'Protection from Aether', 'Proteciton from Evil', 'Protection from Good', 'Cure Wounds I',
                        'Purify Food & Drink', 'Renew Aether I', 'Sanctuary', 'Sheild', 'Shield of Faith', 'Sleep', 'Soul Shroud', 
                        'Speak With Animals', 'Summon Monster I', 'Summon Undead I', 'Thunderwave', 'Cure Wounds I']
        varSecondLevelSpells = ['Aid', 'Animal Messenger', 'Animate Dead', 'Arcane Lock', 'Augury', 'Barkskin', 'Blur', 
                        'Bone Armor', 'Darkness', 'Summon Undead II', 'Renew Aether II', 'Cure Wounds II', 'Darkvision', 
                        'Flame Blade', 'Flaming Sphere', 'Gentle Repose', 'Heat Metal', 'Hold Person', 'Summon Monster II',
                        'Invisibility', 'Knock', 'Lesser Restoration', 'Levitate', 'Cure Wounds II', 'Inflict Wounds II', 
                        'Locate Plants or Animals', 'Magic Weapon', "Melph's Acid Arrow", 'Mirror Image', 'Moonbeam', 'Pass Without Trace', 
                        'Phantasmal Force', 'Lesser Restoration', 'Prayer of Healing', 'Protection from Poison', 'Healing Word II', 'Ray of Enfeeblement', 
                        'Cure Wounds II', 'Rope Trick', 'Scorching Ray', 'Silence', 'Spider Climb', 'Sound Burst', 'Spike Growth', 
                        'Spiritual Weapon', 'Suggestion', 'Web', 'Zone of Truth', 'Cure Wounds II', 'Summon Monster II', 'Summon Undead II']
        varThirdLevelSpells = ['Animate Dead', 'Beacon of Hope', 'Blink', 'Call Lightning', 'Create Food & Water', 
                        'Cure Wounds III', 'Daylight', 'Dispel Magic', 'Elemental Mantle', 'Fireball', 'Remove Curse', 'Protection from Energy', 
                        'Fly', 'Haste', 'Holy Vigor', 'Lightning Bolt', 'Mass Healing Word', 'Meld Into Stone', 'Plant Growth',
                        'Prayer', 'Protection from Energy', 'Remove Curse', 'Cure Wounds III', 'Water Breathing', 'Cure Wounds III', 
                        'Remove Curse', 'Renew Aether III', 'Inflict Wounds III', 'Sleet Storm', 'Slow', 'Speak With Dead', 'Stinking Cloud', 
                        'Summoner Monster III', 'Summon Undead III', 'Unholy Vigor', 'Water Breathing', 'Water Walk']
        varFourthLevelSpells = ['Cure Wounds IV', 'Cure Wounds IV', 'Cure Wounds IV', 'Summon Monster IV', 'Summon Undead IV', 'Renew Aether IV', 
                        'Arcane Eye', 'Confusion', 'Dimension Door', 'Divination', 'Freedom of Movement', 'Polymorph',
                        'Blight', 'Confusion', 'Death Ward', "Evard's Black Tentacles", 'Ice Storm', 'Stoneskin', 
                        'Air Walk', 'Dominate Beast', 'Wall of Fire', 'Stoneskin', 'Conviction', 'Death Ward', 'Guardian of Faith']
        varFifthLevelSpells = ['Cure Wounds V', 'Cure Wounds V', 'Cure Wounds V', 'Summon Monster V', 'Summon Undead V', 'Renew Aether V',
                        'Dominate Person', 'Feeblemind', 'Hold Monster', 'Mass Cure Wounds', 'Passwall', 'Scrying', 'Seeming', 'True Seeing', 
                        'Cloudkill', 'Cone of Cold', 'Insect Plague', 'Scrying', 'Awaken', 'Commune', 'Plant Door', 'Wall of Stone', 
                        'Flame Strike', 'Mass Cure Wounds', 'Raise Dead', 'Contact Other Plane', 'Telekinesis', 'Teleportation Circle']
        varSixthLevelSpells = ['Cure Wounds VI', 'Cure Wounds VI', 'Cure Wounds VI', 'Summon Monster VI', 'Summon Undead VI', 'Renew Aether VI', 
                        'Banishment', 'Greater Dispel Magic', 'Heal', 'Mass Suggestion', 'Wind Walk', 'Circle of Death', 'Harm', 'Ossify', 
                        'Heal', 'Move Earth', 'Sunbeam', 'Wall of Thorns', 'Blade Barrier', 'Planar Ally', 'Arcane Gate', 'Chain Lightning', 
                        'Disintegrate', 'Flesh to Stone', 'Stone to Flesh', 'Move Earth', 'Sunbeam']
        varSeventhLevelSpells = ['Cure Wounds VII', 'Cure Wounds VII', 'Cure Wounds VII', 'Summon Monster VII', 'Summon Undead VII', 'Renew Aether VII', 
                        'Etherealness', 'Greater Restoration', 'Mass Invisibility', 'Prismatic Spray', 'Regenerate', 'Creeping Doom', 
                        'Finger of Death', 'Fire Storm', 'Plane Shift', 'Regenerate', 'Destruction', 'Holy Word', 'Plane Shift', 'Resurrection', 
                        'Mass Invisibility', "Mordenkainen's Sword", 'Teleport']
        varEighthLevelSpells = ['Cure Wounds VIII', 'Cure Wounds VIII', 'Cure Wounds VIII', 'Summon Monster VIII', 'Summon Undead VIII', 'Renew Aether VIII', 
                        'Antimagic Field', 'Dominate Monster', 'Maze', 'Power Word Stun', 'Breath of Crypt Lord', 'Clone', 'Trap the Soul', 
                        'Earthquake', 'Sunburst', 'Holy Aura', 'Dominate Monster', 'Maze', "Otto's Irresistible Dance"]
        varNinthLevelSpells = ['Cure Wounds IX', 'Cure Wounds IX', 'Cure Wounds IX', 'Summon Monster IX', 'Summon Undead IX', 'Renew Aether IX', 
                        'Astral Projection', 'Foresight', 'Mass Heal', 'Mass Hold Monster', 'Power Word Kill', 'Mass Harm', 'Storm of Vengeance', 
                        'Gate', 'Mass Heal', 'True Resurrection', 'Meteor Swarm', 'Time Stop', 'Wish', 'Miracle']
        
        # Potions
        varFirstLevelPotions = ['Animal Friendship', 'Bless', 'Cause Fear', 'Charm Person', 
                        'Command', 'Comprehend Languages', 'False Life', 'Cure Wounds I', 
                        'Protection from Evil', 'Detect Good & Evil', 'Detect Magic', 'Detect Poison & Disease', 'Disguise Self', 
                        'Divine Favor', 'False Life', 'Feather Fall', 'Cure Wounds I', 
                        'Goodberry', 'Identify', 'Inflict Wounds I', 'Longstrider', 
                        'Protection from Aether', 'Protection from Evil', 'Protection from Good', 'Cure Wounds I',
                        'Purify Food & Drink', 'Renew Aether I', 'Sanctuary', 'Sheild', 'Shield of Faith', 'Sleep', 'Soul Shroud', 
                        'Speak With Animals']
        varSecondLevelPotions = ['Aid', 'Animate Dead', 'Augury', 'Barkskin', 'Blur', 
                        'Bone Armor', 'Renew Aether II', 'Cure Wounds II', 'Darkvision', 
                        'Gentle Repose', 'Hold Person', 'Invisibility', 'Lesser Restoration', 'Levitate', 'Cure Wounds II', 'Inflict Wounds II', 
                        'Locate Plants or Animals', 'Magic Weapon', 'Mirror Image', 'Pass Without Trace', 
                        'Protection from Poison', 'Healing Word II', 'Cure Wounds II', 'Silence', 'Spider Climb', 
                        'Spiritual Weapon', 'Suggestion']
        varThirdLevelPotions = ['Animate Dead', 'Beacon of Hope', 'Cure Wounds III', 'Dispel Magic', 'Elemental Mantle', 
                        'Remove Curse', 'Protection from Energy', 'Fly', 'Haste', 'Holy Vigor', 'Meld Into Stone', 
                        'Prayer', 'Protection from Energy', 'Remove Curse', 'Cure Wounds III', 'Water Breathing', 'Cure Wounds III', 
                        'Remove Curse', 'Renew Aether III', 'Inflict Wounds III', 'Slow', 'Speak With Dead',  
                        'Unholy Vigor', 'Water Breathing', 'Water Walk']
        
        #colors list
        varMagicColors = ['snow-white', 'ivory', 'smokey', 'ashen', 'ebon', 'platinum', 'silver', 'onyx', 'magenta', 'crimson', 
                        'violet', 'lavender', 'rose', 'ruby', 'amaranth', 'oxblood', 'rusty', 'amber', 'umber', 'citrine', 'golden', 
                        'tawny', 'orange', 'emerald', 'harlequin green', 'sickly green', 'balefire green', 'cyan', 'turquoise', 
                        'azure', 'cerulean', 'indigo', 'midnight', 'cobalt', 'sapphire', 'amethyst']
        
        
        varDragonColor = ['Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Black', 'Green', 'White', 'Red', 'Blue', 'Gold', 'Silver', 'Copper', 'Brass', 'Bronze', 
                        'Fang (poison)', 'Shadow (necrotic)', 'Astral (radiant/fire)', 'Brown (bludgeoning)', 'Gem (psychic)']
        
        #armor type list
        varMagicArmorType = ['Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 
                        'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Mithral Shirt', 'Mithral Shirt', 
                        'Mithral Shirt', 'Mithral Shirt', 'Mithral Shirt', 'Adamantine Shirt', 
                        "Black Iron Shirt", "Black Iron Shirt", "Black Iron Shirt", "Deep Crystal Shirt", "Glassteel Shirt", "Ironwood Shirt",
                        "Glassteel Shirt", "Ironwood Shirt", "Glassteel Shirt", "Ironwood Shirt", 'Orichalcon Shirt', 'Orichalcon Shirt', 
                        'Orichalcon Shirt', 'Warpstone Shirt', "Unique Ancient's Shirt", "Unique Ancient's Shirt", "Sky Iron Shirt", 
                        "Unique Ancient's Shirt", 'Dragon Leather', 'Dragon Leather', 'Dragon Leather', "Sky Iron Shirt",
                        'Dragon Leather', 'Dragon Leather', 'Dragon Leather', 'Spiderweave', 'Sylvanweave', 'Wyldskin Hide', 
                        'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Mithral Scale', 'Adamantine Scale', 
                        'Studded Dragon Leather', "Black Iron Scale", 'Studded Dragon Leather', "Black Iron Scale", 'Deep Crystal Scale', 
                        'Glassteel Scale', 'Ironwood Scale', 'Glassteel Scale', 'Ironwood Scale', "Sky Iron Scale", "Sky Iron Scale",
                        'Dragon Scale', 'Studded Dragon Leather', "Orichalcon Scale", 'Dragon Scale', 'Studded Dragon Leather', "Orichalcon Scale", 
                        'Dragon Scale', 'Studded Dragon Leather', 'Warpstone Scale', "Unique Ancient's Scale", "Unique Ancient's Scale", 
                        'Dragon Scale', 'Mithril Chain', 'Mithril Chain', 'Mithril Banded', 'Black Iron Banded', 'Deep Crystal Banded', 'Sky Iron Banded',
                        'Black Iron Banded', 'Glassteel Banded', 'Ironwood Banded', 'Orichalcon Banded', 'Warpstone Banded', "Unique Ancient's Banded", 
                        'Black Iron Banded', 'Glassteel Banded', 'Ironwood Banded', 'Orichalcon Banded', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 
                        'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Mithral Shirt', 'Mithral Shirt', 
                        'Mithral Shirt', 'Mithral Shirt', 'Mithral Shirt', 'Adamantine Shirt', 'Sky Iron Shirt', 'Sky Iron Scale', 'Sky Iron Banded',
                        "Black Iron Shirt", "Black Iron Shirt", "Black Iron Shirt", "Deep Crystal Shirt", "Glassteel Shirt", "Ironwood Shirt",
                        "Glassteel Shirt", "Ironwood Shirt", "Glassteel Shirt", "Ironwood Shirt", 'Orichalcon Shirt', 'Orichalcon Shirt', 
                        'Orichalcon Shirt', 'Warpstone Shirt', "Unique Ancient's Shirt", "Unique Ancient's Shirt", 
                        "Unique Ancient's Shirt", 'Dragon Leather', 'Dragon Leather', 'Dragon Leather', 
                        'Dragon Leather', 'Dragon Leather', 'Dragon Leather', 'Spiderweave', 'Sylvanweave', 'Wyldskin Hide', 
                        'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Mithral Scale', 'Adamantine Scale', 
                        'Studded Dragon Leather', "Black Iron Scale", 'Studded Dragon Leather', "Black Iron Scale", 'Deep Crystal Scale', 
                        'Glassteel Scale', 'Ironwood Scale', 'Glassteel Scale', 'Ironwood Scale', 'Sky Iron Plate', 'Sky Iron Plate',
                        'Dragon Scale', 'Studded Dragon Leather', "Orichalcon Scale", 'Dragon Scale', 'Studded Dragon Leather', "Orichalcon Scale", 
                        'Dragon Scale', 'Studded Dragon Leather', 'Warpstone Scale', "Unique Ancient's Scale", "Unique Ancient's Scale", 
                        'Dragon Scale', 'Mithril Chain', 'Mithril Chain', 'Mithril Banded', 'Black Iron Banded', 'Deep Crystal Banded', 
                        'Black Iron Banded', 'Glassteel Banded', 'Ironwood Banded', 'Orichalcon Banded', 'Warpstone Banded', "Unique Ancient's Banded", 
                        'Black Iron Banded', 'Glassteel Banded', 'Ironwood Banded', 'Orichalcon Banded', 'Black Iron Plate', 'Ironwood Plate', 
                        'Black Iron Plate', 'Deep Crystal Plate', 'Glassteel Plate', 'Ironwood Plate', 'Orichalcon Plate', 'Warpstone Plate', 
                        'Orichalcon Plate', "Unique Ancient's Plate", "Unique Ancient's Plate", "Unique Ancient's Plate", 
                        'Mithril Plate', 'Adamantine Banded', 'Adamantine Plate', 'Dragonsteel Plate''Mithril Plate', 'Adamantine Banded', 'Adamantine Plate', 
                        'Dragonsteel Plate', 'Dragonsteel Plate', 'Dragonsteel Plate']
        
        # normal armor list
        varRandomArmor = ['Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Leather Armor', 'Leather Armor', 'Leather Armor', 
                        'Leather Armor', 'Leather Armor', 'Chain Shirt', 'Chain Shirt', 'Chain Shirt', 'Hide Armor', 'Hide Armor', 'Hide Armor', 'Hide Armor', 
                        'Hide Armor', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Scale Mail', 
                        'Scale Mail', 'Scale Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 
                        'Chain Mail', 'Chain Mail', 'Chain Mail', 'Splint Mail', 'Splint Mail', 'Splint Mail', 'Banded Mail', 'Plate Mail', 
                        'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Leather Armor', 'Leather Armor', 'Leather Armor', 
                        'Leather Armor', 'Leather Armor', 'Chain Shirt', 'Chain Shirt', 'Chain Shirt', 'Hide Armor', 'Hide Armor', 'Hide Armor', 'Hide Armor', 
                        'Hide Armor', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Scale Mail', 
                        'Scale Mail', 'Scale Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 
                        'Chain Mail', 'Chain Mail', 'Chain Mail', 'Splint Mail', 'Splint Mail', 'Splint Mail', 'Banded Mail', 'Plate Mail', 
                        'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Leather Armor', 'Leather Armor', 'Leather Armor', 
                        'Leather Armor', 'Leather Armor', 'Chain Shirt', 'Chain Shirt', 'Chain Shirt', 'Hide Armor', 'Hide Armor', 'Hide Armor', 'Hide Armor', 
                        'Hide Armor', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Scale Mail', 
                        'Scale Mail', 'Scale Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 
                        'Chain Mail', 'Chain Mail', 'Chain Mail', 'Splint Mail', 'Splint Mail', 'Splint Mail', 'Banded Mail', 'Plate Mail', 
                        'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Leather Armor', 'Leather Armor', 'Leather Armor', 
                        'Leather Armor', 'Leather Armor', 'Chain Shirt', 'Chain Shirt', 'Chain Shirt', 'Hide Armor', 'Hide Armor', 'Hide Armor', 'Hide Armor', 
                        'Hide Armor', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Scale Mail', 
                        'Scale Mail', 'Scale Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 
                        'Chain Mail', 'Chain Mail', 'Chain Mail', 'Splint Mail', 'Splint Mail', 'Splint Mail', 'Banded Mail', 'Plate Mail', 
                        'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Padded Armor', 'Leather Armor', 'Leather Armor', 'Leather Armor', 
                        'Leather Armor', 'Leather Armor', 'Chain Shirt', 'Chain Shirt', 'Chain Shirt', 'Hide Armor', 'Hide Armor', 'Hide Armor', 'Hide Armor', 
                        'Hide Armor', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Studded Leather', 'Scale Mail', 
                        'Scale Mail', 'Scale Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Ring Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 'Chain Mail', 
                        'Chain Mail', 'Chain Mail', 'Chain Mail', 'Splint Mail', 'Splint Mail', 'Splint Mail', 'Banded Mail', 'Plate Mail', 
                        'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Wyldskin Leather', 'Mithral Shirt', 'Mithral Shirt', 
                        'Mithral Shirt', 'Adamantine Shirt', 'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Wyldskin Hide', 'Mithral Scale', 
                        'Adamantine Scale', 'Mithral Chain', 'Mithral Chain', 'Mithral Chain', 'Mithral Banded', 'Mithral Plate', 'Adamantine Plate', 
                        'Mithral Shield', 'Adamantine Shield']
        
        #weapon type list
        varRandomWeapon = ['Cestus', 'Club', 'Light Crossbow', 'Light Crossbow', 'Light Crossbow', 'Dagger', 'Dagger', 'Dagger', 
                        'Dagger', 'Dagger', 'Dagger', 'Dart', 'Dart', 'Greatclub', 'Javelin', 'Javelin', 'Mace', 'Mace', 'Mace', 'Mace', 'Mace', 
                        'Quarterstaff', 'Quarterstaff', 'Quarterstaff', 'Shortbow', 'Shortbow', 'Shortbow', 'Sling', 'Spear', 'Spear', 
                        'Spear', 'Spear', 'Armor Spikes', 'Battleaxe', 'Battleaxe', 'Battleaxe', 'Battleaxe', 'Battleaxe', 
                        'Blowgun', 'Blowgun', 'Bolas', 'Hand Crossbow', 'Hand Crossbow', 'Hand Crossbow', 'Heavy Crossbow', 'Heavy Crossbow', 
                        'Heavy Crossbow', 'Heavy Crossbow', 'Heavy Crossbow', 'Double Axe', 'Double Sword', 'Double Sword', 'Falchion', 
                        'Falchion', 'Falchion', 'Flail', 'Flail', 'Flail', 'Glaive', 'Glaive', 'Glaive', 'Greataxe', 'Greataxe', 'Greataxe', 
                        'Greataxe', 'Greataxe', 'Greatsword', 'Greatsword', 'Greatsword', 'Greatsword', 'Greatsword', 'Greatsword', 'Greatsword', 
                        'Halberd', 'Halberd', 'Halberd', 'Handaxe', 'Handaxe', 'Katana', 'Katana', 'Katana', 'Katana', 'Katana', 
                        'Lance', 'Lance', 'Lance', 'Light Hammer', 'Light Hammer', 'Longsword', 'Longsword', 'Longsword', 'Longsword', 
                        'Longsword', 'Longsword', 'Longsword', 'Longsword', 'Longsword', 'Longsword', 'Longbow', 'Longbow', 'Longbow', 
                        'Longbow', 'Longbow', 'Longbow', 'Longbow', 'Longbow', 'Longbow', 'Longbow', 'Maul', 'Maul', 'Maul', 'Morningstar', 
                        'Morningstar', 'Morningstar', 'Morningstar', 'Morningstar', 'Net', 'Pike', 'Pike', 'Rapier', 'Rapier', 'Rapier', 
                        'Rapier', 'Rapier', 'Scimitar', 'Scimitar', 'Scimitar', 'Scimitar', 'Scimitar', 'Shortsword', 'Shortsword', 'Shortsword', 
                        'Shortsword', 'Shortsword', 'Shortsword', 'Shortsword', 'Spiked Chain', 'Spiked Chain', 'Spiked Chain', 'Spiked Shield', 
                        'Spiked Shield', 'Trident', 'Trident', 'War Pick', 'War Pick', 'War Pick', 'Warhammer', 'Warhammer', 'Warhammer', 'Warhammer',
                        'Warhammer', 'Warhammer', 'Warhammer', 'Warhammer', 'Warhammer', 'Warhammer', 'Whip', 'Whip', 'Arbalest', 'Bearded Axe', 
                        'Blade Boot', 'Boarding Axe', 'Brightspark Holdout', 'Brightspark Pistol', 'Brightspark Revolver', 'Brightspark Rifle', 
                        'Brightspark Repeater', 'Brightspark Longrifle', 'Brightspark Scattergun', 'Chakram', 'Coiled Dagger', 'Dire Flail', 
                        'Dwarven Boulder Helm', 'Earthbreaker', 'Estoc', 'Garrote', 'Halfling Rope Shot', 'Harpoon', 'Greatbow', 'Greatbow', 
                        'Khopesh', 'Khopesh', 'Ogre Hook', 'Meteor Hammer', 'Nodachi', 'Nodachi', 'Parrying Dagger', 'Saber Claws', 
                        'Scorpion Whip', 'Telvari Viridian Rifle', 'Heavy Viridian Cannon', 'Urgrosh', 'Warscythe']
                        
        #magic material list for swords and shields
        varMagicMaterial = ['Common Material', 'Common Material', 'Common Material', 'Adamantine', 'Black Iron', 
                        'Common Material', 'Common Material', 'Common Material', 'Common Material', 'Common Material', 'Common Material', 
                        'Common Material', 'Common Material', 'Common Material', 'Common Material', 'Common Material', 'Common Material', 
                        'Common Material', 'Common Material', 'Common Material', 'Common Material', 'Common Material', 'Common Material', 
                        'Common Material', 'Adamantine', 'Black Iron', 'Black Iron', 'Deep Crystal', 'Dragonsteel', 'Dragonsteel', 
                        'Dragonsteel', 'Dragonsteel', 'Dragonsteel', 'Dragonsteel', 'Glassteel', 'Ironwood', 'Glassteel', 'Ironwood', 
                        'Glassteel', 'Ironwood', 'Mithral', 'Orichalcon', 'Mithral', 'Orichalcon', 'Sky Iron', 'Sky Iron', 'Spiderweave', 'Sylvanweave', 
                        'Warpstone', 'Wyldskin/Wyldfang', 'a Unique Material', 'Wyldskin/Wyldfang', 'a Unique Material', 'Wyldskin/Wyldfang', 'a Unique Material']      
                        
        varDivineList = ['Aiyr, the Hidden Rune', 'Castia, the Wild Hunt', 'Draugh, the Black Thorn', 'Ision, the Crimson Fane', 
                        'Nym, the Untamed Tempest', 'Roelyd, the White Ram', 'Ur, the Fallen', 'Ylle, the Crawling Chaos', 'The Kingsroad', 
                        'The Way of Flame', 'Aiyr, the Hidden Rune', 'Castia, the Wild Hunt', 'Draugh, the Black Thorn', 'Ision, the Crimson Fane', 
                        'Nym, the Untamed Tempest', 'Roelyd, the White Ram', 'Ur, the Fallen', 'Ylle, the Crawling Chaos', 'The Kingsroad', 
                        'The Way of Flame', 'Aiyr, the Hidden Rune', 'Castia, the Wild Hunt', 'Draugh, the Black Thorn', 'Ision, the Crimson Fane', 
                        'Nym, the Untamed Tempest', 'Roelyd, the White Ram', 'Ur, the Fallen', 'Ylle, the Crawling Chaos', 'The Kingsroad', 
                        'The Way of Flame', 'A Forgotten God or Cult', 'A Forgotten God or Cult', 'A Forgotten God or Cult', 'The Void']

        #alchemical concoctions list                    
        varMinorAlchemical = ['Oil of Iron Silence', 'Oil of Minor Banes', 'Oil of Minor Striking', 'Oil of Magestrike', 'Dose of Carrion Crawler Brain Juice',
                        'Catseye Elixir', 'Dose of Dissonance Taint', "Elixir of Bear's Endurance", "Elixir of Bull's Strength", "Elixir of Cat's Grace", 
                        "Elixir of Eagle's Splendor", "Elixir of Fox's Cunning", 'Elixir of Minor Health', 'Elixir of Minor Health', 'Elixir of Minor Health', 
                        "Elixir of Lion's Might", 'Elixir of Minor Defense', "Elixir of Owl's Wisdom", 'Dose of Giant Spider Venom', 'Dose of Hemorrhagic Venom', 
                        'Minor Healing Draught (2d6)', 'Minor Healing Draught (2d6)', 'Minor Healing Draught (2d6)', 'Minor Healing Draught (2d6)', 
                        'Minor Healing Draught (2d6)', 'Minor Mana Draught', 'Minor Mana Draught', 'Minor Mana Draught', 'Minor Rejuvenation Draught', 
                        'Minor Trollflesh Elixir', 'Minor Trollflesh Elixir', 'Minor Trollflesh Elixir', 'Dose of Venomous Grandeur']
        varLesserAlchemical = ['Oil of Lesser Banes', 'Oil of Lesser Defense', 'Oil of Fire', 'Blessed Elixir', 'Draught of Magic Resistance', 
                        'Draught of Shapelessness', 'Elixir of Anchored Steps', 'Elixir of Cognizance', 'Elixir of Fortitude', 'Elixir of Guidance', 
                        'Elixir of Lesser Awareness', 'Elixir of Lesser Health', 'Elixir of Oaken Flesh', 'Elixir of Ogre Strength', 'Elixir of Savage Power', 
                        "Elixir of Panther's Agility", 'Elixir of the Bloodhound', 'Elixir of the Inquisitor', 'Elixir of the Sea', 'Dose of Giant Wasp Venom', 
                        'Lesser Healing Draught (4d6)', 'Lesser Healing Draught (4d6)', 'Lesser Healing Draught (4d6)', 'Lesser Healing Draught (4d6)', 
                        'Lesser Healing Draught (4d6)', 'Lesser Mana Draught', 'Lesser Mana Draught', 'Lesser Mana Draught', 'Lesser Rejuvenation Draught', 
                        'Dose of Somnolent Venom']
        varModerateAlchemical = ['Oil of Frost', 'Oil of Moderate Banes', 'Oil of Moderate Defense', 'Oil of Necrosis', 'Oil of Wraithstrike', 
                        'Elixir of Cold Resistance', 'Elixir of Discernment', 'Elixir of Draconic Reservoir', 'Elixir of Elemental Endurance', 
                        'Elixir of Fire Resistance', 'Elixir of Flames', 'Elixir of Frost Power', 'Elixir of Invisibility', 'Elixir of Moderate Health', 
                        'Elixir of Monkeyflesh', 'Dose of Giant Scorpion Venom', 'Love Potion', 'Moderate Healing Draught (6d6)', 'Moderate Healing Draught (6d6)', 
                        'Moderate Healing Draught (6d6)', 'Moderate Healing Draught (6d6)', 'Moderate Mana Draught', 'Moderate Mana Draught', 
                        'Shadowsoul Elixir', 'Moderate Trollflesh Elixir']
        
        varHerbalism = ['acantha', 'adamantine dust', 'ash wood shavings', 'athril', 'ayana', 'black cohosh', 'black lotus', 'black tea', 
                        'blackwood sap', 'bloodcrown', 'bloodthistle', 'briarthorn', 'brimstone', 'cinnabar', 'cockatrice teeth', 'devil grass', 
                        'dragonleaf', 'dreamthorn', 'elderberry', 'fadewhisker', 'felbloom', 'feverfew', 'fire lichen', 'firevine', 'fjaleaf', 'fools cap', 
                        'foxglove', 'frostcap', 'ghost moss', 'glownettle', 'gravethorn', 'green tea', 'greymold', 'hemlock', 'holy water', 'honey', 
                        'iron filings', 'ironwood sap', 'jasmine', 'kave', 'kingsblood', 'kohl', 'lunas rose', 'magethistle', 'mana clover', 'mandrake', 
                        'nornsblood', 'phosphorus', 'rain poppy', 'riverbite', 'rosethorn', 'saltmoss', 'seraline', 'silkweed', 'silversage', 'sirens kiss', 
                        'slimescale', 'snow lily', 'snow poppy', 'steelbloom', 'suns bell', 'tiger lily', 'torchflower', 'valerian', 'vervain', 'whiteveil', 'wolvesbane']
        
        #alchemical bits
        varHerbalismGet = (random.randint(1,20))
        varHerbalismStuff = (random.randint(1,4))
        if varHerbalismGet >= 15:
                print("You find a pouch of herbal ingredients containing:")
                while varHerbalismStuff >= 0:
                        print("  ", random.choice(varHerbalism))
                        varHerbalismStuff = (varHerbalismStuff - 1)
                print("-----------------------------------")    
        
        
        #consumables
        varConsumables=(random.randint(1,20)) + (varEL)
        
        if varConsumables <= 17:
                print("You recieve no consumables.")
                
        if varConsumables >= 18 and varConsumables <= 29:
                varConsumablesGet=(random.randint(1,3))
                varConsumablesSoFar=0
                while varConsumablesGet >= varConsumablesSoFar:
                        varConsumablesType=(random.randint(1,20))
                        if varConsumablesType <= 7:
                                varAlchemicalQuality=(random.randint(1,20))
                                if varAlchemicalQuality <= 15:
                                        print("You recieve a(n)", random.choice(varMinorAlchemical))
                                if varAlchemicalQuality >= 16 and varAlchemicalQuality <= 19:
                                        print("You recieve a(n)", random.choice(varLesserAlchemical))
                                if varAlchemicalQuality == 20:
                                        print("You recieve a(n)", random.choice(varModerateAlchemical))
                        if varConsumablesType >=8 and varConsumablesType <= 13:
                                varPotionLevel=(random.randint(1,20))
                                if varPotionLevel <= 15:
                                        print("You recieve a Potion of", random.choice(varFirstLevelPotions))
                                if varPotionLevel >= 16 and varPotionLevel <= 19:
                                        print("You recieve a Potion of", random.choice(varSecondLevelPotions))
                                if varPotionLevel == 20:
                                        print("You have recieved a Potion of", random.choice(varThirdLevelPotions))
                        if varConsumablesType >= 14:
                                varScrollLevel=(random.randint(1,20)) + (varEL)
                                if varScrollLevel >= 1 and varScrollLevel <=10:
                                        print("You recieve a Scroll of", random.choice(varFirstLevelSpells))
                                if varScrollLevel >= 11 and varScrollLevel <=15:
                                        print("You recieve a Scroll of", random.choice(varSecondLevelSpells))                                   
                                if varScrollLevel >= 16 and varScrollLevel <=20:
                                        print("You recieve a Scroll of", random.choice(varThirdLevelSpells))
                                if varScrollLevel >= 21 and varScrollLevel <=25:
                                        print("You recieve a Scroll of", random.choice(varFourthLevelSpells))  
                                if varScrollLevel >= 26 and varScrollLevel <=30:
                                        print("You recieve a Scroll of", random.choice(varFifthLevelSpells))            
                                if varScrollLevel >= 31 and varScrollLevel <=32:
                                        print("You recieve a Scroll of", random.choice(varSixthLevelSpells))
                                if varScrollLevel >= 33 and varScrollLevel <=34:
                                        print("You recieve a Scroll of", random.choice(varSeventhLevelSpells))                                  
                                if varScrollLevel >= 35 and varScrollLevel <=36:
                                        print("You recieve a Scroll of", random.choice(varEighthLevelSpells))
                                if varScrollLevel >= 37 and varScrollLevel <=40:
                                        print("You recieve a Scroll of", random.choice(varNinthLevelSpells))
                        varConsumablesSoFar = varConsumablesSoFar +1
                        
        if varConsumables >= 30:
                varConsumablesGet=(random.randint(1,6))
                varConsumablesSoFar=0
                while varConsumablesGet >= varConsumablesSoFar:
                        varConsumablesType=(random.randint(1,20))
                        if varConsumablesType <= 7:
                                varAlchemicalQuality=(random.randint(1,20))
                                if varAlchemicalQuality <= 15:
                                        print("You recieve a(n)", random.choice(varMinorAlchemical))
                                if varAlchemicalQuality >= 16 and varAlchemicalQuality <= 19:
                                        print("You recieve a(n)", random.choice(varLesserAlchemical))
                                if varAlchemicalQuality == 20:
                                        print("You recieve a(n)", random.choice(varModerateAlchemical))
                        if varConsumablesType >=8 and varConsumablesType <= 13:
                                varPotionLevel=(random.randint(1,20))
                                if varPotionLevel <= 15:
                                        print("You recieve a Potion of", random.choice(varFirstLevelPotions))
                                if varPotionLevel >= 16 and varPotionLevel <= 19:
                                        print("You recieve a Potion of", random.choice(varSecondLevelPotions))
                                if varPotionLevel == 20:
                                        print("You recieve a Potion of", random.choice(varThirdLevelPotions))
                        if varConsumablesType >= 14:
                                varScrollLevel=(random.randint(1,20)) + (varEL)
                                if varScrollLevel >= 1 and varScrollLevel <=10:
                                        print("You recieve a Scroll of", random.choice(varFirstLevelSpells))
                                if varScrollLevel >= 11 and varScrollLevel <=15:
                                        print("You recieve a Scroll of", random.choice(varSecondLevelSpells))                                   
                                if varScrollLevel >= 16 and varScrollLevel <=20:
                                        print("You recieve a Scroll of", random.choice(varThirdLevelSpells))
                                if varScrollLevel >= 21 and varScrollLevel <=25:
                                        print("You recieve a Scroll of", random.choice(varFourthLevelSpells))  
                                if varScrollLevel >= 26 and varScrollLevel <=30:
                                        print("You recieve a Scroll of", random.choice(varFifthLevelSpells))            
                                if varScrollLevel >= 31 and varScrollLevel <=32:
                                        print("You recieve a Scroll of", random.choice(varSixthLevelSpells))
                                if varScrollLevel >= 33 and varScrollLevel <=34:
                                        print("You recieve a Scroll of", random.choice(varSeventhLevelSpells))                                  
                                if varScrollLevel >= 35 and varScrollLevel <=36:
                                        print("You recieve a Scroll of", random.choice(varEighthLevelSpells))
                                if varScrollLevel >= 37 and varScrollLevel <=40:
                                        print("You recieve a Scroll of", random.choice(varNinthLevelSpells))
                        varConsumablesSoFar = varConsumablesSoFar +1
        print("-----------------------------------")    
        
        #check for magic items
        varMagicItem=(random.randint(1,20)) + (varEL)
        if varMagicItem <= 19:
                print("You recieve no magic items.")
                
        if varMagicItem >= 20:
                varMagicQualityRoll=(random.randint(1,20))
                if varMagicQualityRoll <= 15:
                        varMagicQuality="Dross"
                if varMagicQualityRoll >= 16 and varMagicQualityRoll <= 19:
                        varMagicQuality="Relic"
                if varMagicQualityRoll == 20:
                        varMagicQuality="Artifact"
                
                #set Magic Item Origin
                varMagicItemOriginRoll=(random.randint(1,20))
                if varMagicItemOriginRoll == 1:
                        varMagicItemOrigin = "Far Realm"
                if varMagicItemOriginRoll == 2:
                        varMagicItemOrigin = "Underdark"
                if varMagicItemOriginRoll == 3:
                        varMagicItemOrigin = "Astral"
                if varMagicItemOriginRoll == 4:
                        varMagicItemOrigin = "Elven"
                if varMagicItemOriginRoll == 5:
                        varMagicItemOrigin = "Elven"
                if varMagicItemOriginRoll == 6:
                        varMagicItemOrigin = "Human"
                if varMagicItemOriginRoll == 7:
                        varMagicItemOrigin = "Human"
                if varMagicItemOriginRoll == 8:
                        varMagicItemOrigin = "Dwarven"
                if varMagicItemOriginRoll == 9:
                        varMagicItemOrigin = "Dwarven"
                if varMagicItemOriginRoll == 10:
                        varMagicItemOrigin = "Gnomish"
                if varMagicItemOriginRoll == 11:
                        varMagicItemOrigin = "Gnomish"
                if varMagicItemOriginRoll == 12:
                        varMagicItemOrigin = "Draconic"
                if varMagicItemOriginRoll == 13:
                        varMagicItemOrigin = "Necromantic"
                if varMagicItemOriginRoll == 14:
                        varMagicItemOrigin = "Tiefling"
                if varMagicItemOriginRoll == 15:
                        varMagicItemOrigin = "Halfling"
                if varMagicItemOriginRoll == 16:
                        varElementalList=['Elemental Air', 'Elemental Earth', 'Elemental Fire', 'Elemental Water']
                        varMagicItemOrigin=random.choice(varElementalList)
                if varMagicItemOriginRoll == 17:
                        varMagicItemOrigin = "Rare Humanoid"
                if varMagicItemOriginRoll == 18:
                        varMagicItemOrigin = "Warforged"
                if varMagicItemOriginRoll == 19:
                        varMagicItemOrigin = "Savage/Monstrous"
                if varMagicItemOriginRoll == 20:
                        varMagicItemOrigin = "Antiquity"
            
                #Set Magic Item Type
                varMagicItemTypeRoll=(random.randint(1,20))
                
                #eternal wands
                if varMagicItemTypeRoll == 1 or varMagicItemTypeRoll == 2:
                        varEternalWandLevel=(random.randint(1,20))
                        if varEternalWandLevel >= 1 and varEternalWandLevel <= 15:
                                print("You recieve a(n)", varMagicQuality, "rank Eternal Wand of", random.choice(varFirstLevelSpells))
                                print("of", varMagicItemOrigin, "make.")
                        if varEternalWandLevel >=16 and varEternalWandLevel <= 19:
                                print("You recieve a(n)", varMagicQuality, "rank Eternal Wand of", random.choice(varSecondLevelSpells))
                                print("of", varMagicItemOrigin, "make.")
                        if varEternalWandLevel ==20:
                                print("You recieve a(n)", varMagicQuality, "rank Eternal Wand of", random.choice(varThirdLevelSpells))
                                print("of", varMagicItemOrigin, "make.")
                
                #magic armor
                if varMagicItemTypeRoll == 3 or varMagicItemTypeRoll == 4:
                        varMagicItemType="Magic Armor"
                        varMagicArmorChoice=random.choice(varMagicArmorType)
                        print("You recieve a", varMagicQuality, "rank suit of", varMagicArmorChoice) 
                        print("of", varMagicItemOrigin, "make.")
                        if varMagicArmorChoice == "Dragon Leather" or varMagicArmorChoice == "Studded Dragon Leather" or varMagicArmorChoice == "Dragon Scale" or varMagicArmorChoice == "Dragonsteel Plate":
                                print("   This armor is forged of", random.choice(varDragonColor), "dragon hide.")
                
                #magic shield           
                if varMagicItemTypeRoll == 5:
                        varMagicItemType="Magic Shield"
                        varShieldMat=random.choice(varMagicMaterial)
                        print("You recieve a", varMagicQuality, "rank", varMagicItemType, ", of", varMagicItemOrigin, "make,")
                        print("crafted from", varShieldMat, ".")
                        if varShieldMat == "Dragonsteel": 
                                print("   This shield is forged of", random.choice(varDragonColor), "dragon hide.")

                #magic weapon           
                if varMagicItemTypeRoll >= 6 and varMagicItemTypeRoll <= 8:
                        varMagicItemType="Magic Weapon"
                        varWeaponMat=random.choice(varMagicMaterial)
                        varRandomWeaponChoice=random.choice(varRandomWeapon)
                        if varRandomWeaponChoice == "Telvari Viridian Rifle" or varRandomWeaponChoice == "Heavy Viridian Cannon":
                                varMagicItemOrigin="Telvari"
                        print("You recieve a", varMagicQuality, "rank magical weapon, a", varRandomWeaponChoice, "of")
                        print(varMagicItemOrigin, "make, forged from", varWeaponMat, ".")
                        if varWeaponMat == "Dragonsteel":
                                print("   This weapon is forged of", random.choice(varDragonColor), "dragonsteel.")
                
                #talisman
                if varMagicItemTypeRoll == 9 or varMagicItemTypeRoll == 10:
                        varTalismanType = ['Instrument', 'Component Pouch', 'Component Pouch', 'Component Pouch', 'Dagger', 'Dagger', 
                                        'Dagger', 'Dagger', 'Holy Symbol', 'Holy Symbol', 'Holy Symbol', 'Orb', 'Orb', 'Psi Crystal', 'Rod', 
                                        'Rod', 'Spellbook', 'Spellbook', 'Staff', 'Staff', 'Wand', 'Wand', 'Martial Focus']
                        varMagicItemType=random.choice(varTalismanType)
                        print("You recieve a", varMagicQuality, "rank magical talisman, a", varMagicItemType, "of")
                        print(varMagicItemOrigin, "make.")
                        if varMagicItemType == 'Holy Symbol':
                                print("   This Holy Symbol is dedicated to", random.choice(varDivineList), ".")
                                
                #magic ring
                if varMagicItemTypeRoll == 11 or varMagicItemTypeRoll == 12:
                        varMagicItemType="Magic Ring"
                        print("You recieve a", varMagicQuality, "rank Magic Ring of", varMagicItemOrigin, "make.")
                
                #dorje
                if varMagicItemTypeRoll == 13 or varMagicItemTypeRoll == 14:
                        varMagicItemType="Dorje"
                        varDorjeClass = ['Dragon Shaman', 'Runeblade', 'Soulweaver', 'Warlock', 'Witch', 'Psion']
                        print("You recieve a", varMagicQuality, "rank Dorje, of", varMagicItemOrigin, "make, which contains")
                        print("an invocation or aptitude from the", random.choice(varDorjeClass), "class, based on its rank.")

                #magic staff
                if varMagicItemTypeRoll == 15:
                        varMagicItemType="Magic Staff"
                        varPowers=0
                        varSpells=0
                        if varMagicQuality == "Dross":
                                varPowersCheck=random.randint(1,4)
                                if varPowersCheck == 4:
                                        varPowers = varPowers +1
                                if varPowersCheck != 4:
                                        varSpells = varSpells +1
                        if varMagicQuality == "Relic":
                                varPowersCheck=random.randint(1,4)
                                if varPowersCheck == 4:
                                        varPowers = +1
                                if varPowersCheck != 4:
                                        varSpells = varSpells +1
                                varPowersCheck2=random.randint(1,4)
                                if varPowersCheck2 == 4:
                                        varPowers = +1
                                if varPowersCheck != 4:
                                        varSpells =  +1
                        if varMagicQuality == "Artifact":
                                varPowersCheck=random.randint(1,4)
                                if varPowersCheck == 4:
                                        varPowers = +1
                                if varPowersCheck != 4:
                                        varSpells = varSpells +1
                                varPowersCheck2=random.randint(1,4)
                                if varPowersCheck2 == 4:
                                        varPowers = +1
                                if varPowersCheck != 4:
                                        varSpells =  +1
                                varPowersCheck3=random.randint(1,4)
                                if varPowersCheck3 == 4:
                                        varPowers = +1
                                if varPowersCheck != 4:
                                        varSpells = varSpells +1                                

                                        
                        print("You recieve a", varMagicQuality, "rank Magical Staff of", varMagicItemOrigin, "make.")
                        print("   This staff contains", varPowers, "powers, and this/these spell(s),")
                        print("   if any are listed below:")                    

                        while varSpells >= 1:
                                varSpellLevel=(random.randint(1,20)) + (varEL)
                                if varSpellLevel >= 1 and varSpellLevel <=10:
                                        print("      ", random.choice(varFirstLevelSpells))
                                if varSpellLevel >= 11 and varSpellLevel <=15:
                                        print("      ", random.choice(varSecondLevelSpells))                                    
                                if varSpellLevel >= 16 and varSpellLevel <=20:
                                        print("      ", random.choice(varThirdLevelSpells))
                                if varSpellLevel >= 21 and varSpellLevel <=25:
                                        print("      ", random.choice(varFourthLevelSpells))  
                                if varSpellLevel >= 26 and varSpellLevel <=30:
                                        print("      ", random.choice(varFifthLevelSpells))             
                                if varSpellLevel >= 31 and varSpellLevel <=32:
                                        print("      ", random.choice(varSixthLevelSpells))
                                if varSpellLevel >= 33 and varSpellLevel <=34:
                                        print("      ", random.choice(varSeventhLevelSpells))                                   
                                if varSpellLevel >= 35 and varSpellLevel <=36:
                                        print("      ", random.choice(varEighthLevelSpells))
                                if varSpellLevel >= 37 and varSpellLevel <=40:
                                        print("      ", random.choice(varNinthLevelSpells))
                                varSpells= -1


                #wand
                if varMagicItemTypeRoll >= 16 and varMagicItemTypeRoll <= 17:
                        varMagicItemType="Magic Wand"
                        varSpellLevel=(random.randint(1,20)) + (varEL)
                        if varSpellLevel >= 1 and varSpellLevel <=10:
                                varWandSpell=random.choice(varFirstLevelSpells)
                        if varSpellLevel >= 11 and varSpellLevel <=15:
                                varWandSpell=random.choice(varSecondLevelSpells)                                        
                        if varSpellLevel >= 16 and varSpellLevel <=20:
                                varWandSpell=random.choice(varThirdLevelSpells)
                        if varSpellLevel >= 21 and varSpellLevel <=25:
                                varWandSpell=random.choice(varFourthLevelSpells)
                        if varSpellLevel >= 26 and varSpellLevel <=30:
                                varWandSpell=random.choice(varFifthLevelSpells)         
                        if varSpellLevel >= 31 and varSpellLevel <=32:
                                varWandSpell=random.choice(varSixthLevelSpells)
                        if varSpellLevel >= 33 and varSpellLevel <=34:
                                varWandSpell=random.choice(varSeventhLevelSpells)                               
                        if varSpellLevel >= 35 and varSpellLevel <=36:
                                varWandSpell=random.choice(varEighthLevelSpells)
                        if varSpellLevel >= 37 and varSpellLevel <=40:
                                varWandSpell=random.choice(varNinthLevelSpells)
                        print("You recieve a Magic Wand of", varWandSpell, "with", random.randint(1,10), "charges left,")
                        print("of", varMagicItemOrigin, "make.")
                

                #wondrous item
                if varMagicItemTypeRoll >= 18 and varMagicItemTypeRoll <= 20:
                        varMagicItemType="Wondrous Item"
                        print("You recieve a", varMagicQuality, "rank Wondrous Item of", varMagicItemOrigin, "make.")


                #beacon check
                varBeacon=(random.randint(1,20))
                if varBeacon >= 11 and varBeacon <= 15: 
                        print("   This item sheds", random.choice(varMagicColors), "light like a torch on command.")
                if varBeacon >= 16 and varBeacon <= 19:
                        print("   This item sheds", random.choice(varMagicColors), "light like a torch when in use.")
                if varBeacon == 20:
                        print("   This item continuously sheds", random.choice(varMagicColors), "light like a torch.")

                #curse check
                varCursed=(random.randint(1,20))
                if varCursed == 1:
                        print("""      This item is cursed and instantly attunes to any 
      who pick it up. You cannot unattune this item 
      until you recieve a remove curse spell. The item 
      bears an additional negative effect assigned by your DM.""")
                        
        #BIG RANDOM STUFF SECTION
        
        #define big random stuff quantity for loop
        varStuffSoFar = 0
        varRandomStuffRolls = (random.randint(2,4)) + (random.randint(-3,2))
                
        #heading for big random stuff
        if varRandomStuffRolls < 1:
                print("-----------------------------------")
                print("You find no incidental items.")
        if varRandomStuffRolls > 0:
                print("-----------------------------------")    
                
        #start big random stuff loop
        while varStuffSoFar < varRandomStuffRolls:

                #set variables for loot
                varConditionList=['superior', 'fine', 'fine', 'good', 'good', 'good', 'average', 'average', 
        'average', 'average', 'poor', 'poor', 'poor', 'ruined', 'ruined', 'destroyed']
                varQuality=['superior', 'fine', 'fine', 'good', 'good', 'good', 'average', 'average', 'average', 
        'average', 'poor', 'poor', 'poor', 'terrible', 'terrible', 'disgusting']
                varD3=(random.randint(1,3))
                varD4=(random.randint(1,4))
                varD6=(random.randint(1,6))
                varD8=(random.randint(1,8))
                varD10=(random.randint(1,10))
                varD12=(random.randint(1,12))
                varD20=(random.randint(1,20))
                varD00=(random.randint(1,100))
                
#FIX THIS FUCKING LINE WITH THE CORRECT NUMBER - this has been fixed
                varBRSRoll=(random.randint(1,1000))
                
                if varBRSRoll == 1:
                        print("  ", varD20, "pints of lamp oil.")
                if varBRSRoll == 2:
                        print("   A small sewing kit in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 3:
                        print("   A small silver mirror in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 4:
                        print("   A set of eastern prayer beads.  ")
                if varBRSRoll == 5:
                        print("   An imperial rosary.  ")               
                if varBRSRoll == 6:
                        print("  ", varD6, "wax candles.  ")
                if varBRSRoll == 7:
                        print("  ", (random.randint(10,200)),"ft of strong rope.  ")            
                if varBRSRoll == 8:
                        print("   A tinder box in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 9:
                        print("  ", varD10, "torche(s).  ")             
                if varBRSRoll == 10:
                        print("  ", varD6, "pint(s) of beer.  ")
                if varBRSRoll == 11:
                        print("  ", varD6, "quart(s) of wine.  ")
                if varBRSRoll == 12:
                        print("  ", varD6, "iron spike(s).  ")
                if varBRSRoll == 13:
                        print("  ", varD12, "wooden stake(s).  ")
                if varBRSRoll == 14:
                        print("   A fancy hat in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 15:
                        print("   A small iron box.  ")
                if varBRSRoll == 16:
                        print("   A leather scroll case in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 17:
                        print("  ", (random.randint(1,10)), "writing quill(s).  ")
                if varBRSRoll == 18:
                        print("   An ounce of bottled ink.  ")
                if varBRSRoll == 19:
                        print("   A small sack.  ")
                if varBRSRoll == 20:
                        print("  ", (random.randint(1,20)), "bandage(s).  ")
                if varBRSRoll == 21:
                        print("  ", (random.randint(1,3)), "stick(s) of incense.")
                if varBRSRoll == 22:
                        print("  ", (random.randint(1,8)), "bud(s) of garlic.")
                if varBRSRoll == 23:
                        print("  ", (random.randint(1,8)), "sprig(s) of aconite.")
                if varBRSRoll == 24:
                        print("  ", (random.randint(1,6)), "sprig(s) of belladonna.")
                if varBRSRoll == 25:
                        print("  ", (random.randint(1,8)), "link(s) of packed sausage.")
                if varBRSRoll == 26:
                        print("  ", (random.randint(1,3)), "pint(s) of whiskey.")
                if varBRSRoll == 27:
                        print("  ", (random.randint(1,3)), "lbs of cheese.")
                if varBRSRoll == 28:
                        print("  ", (random.randint(1,6)), "apple(s).")
                if varBRSRoll == 29:
                        print("   A handful of bloody rags.")
                if varBRSRoll == 30:
                        print("   A lucky coin.")
                if varBRSRoll == 31:
                        print("  ", (random.randint(1,6)), "vial(s) of holy water.")
                if varBRSRoll == 32:
                        print("   A gnomish folding knife in ", random.choice(varConditionList), "condition.")
                if varBRSRoll == 33:
                        print("   A silver ring worth", (random.randint(2,40)), "copper pieces.")
                if varBRSRoll == 34:
                        print("   A gold ring worth", (random.randint(5,100)),"copper pieces.")
                if varBRSRoll == 35:
                        print("   A metal file.")
                if varBRSRoll == 36:
                        print("   A bandanna.")
                if varBRSRoll == 37:
                        print("   A worn chisel.")
                if varBRSRoll == 38:
                        print("   A small cooking pot.")
                if varBRSRoll == 39:
                        print("   A wood auger.")
                if varBRSRoll == 40:
                        print("   A tiny intricate music box worth", (random.randint(1,20)), "silver pieces.")
                if varBRSRoll == 41:
                        print("   A bone or ivory scroll case in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 42:
                        print("  ", (random.randint(1,10)), "sheet(s) of parchment.")
                if varBRSRoll == 43:
                        print("  ", (random.randint(1,20)), "feet of copper wire.")
                if varBRSRoll == 44:
                        print("   A crude local map.")
                if varBRSRoll == 45:
                        print("   A pile of oily rags.")
                if varBRSRoll == 46:
                        print("   A woven sweater.")
                if varBRSRoll == 47:
                        print("   A finely crafted poncho.")
                if varBRSRoll == 48:
                        print("   A winter blanket in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 49:
                        print("   A bedroll in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 50:
                        print("   A hacksaw.")
                if varBRSRoll == 51:
                        print("   A keyhole saw.")
                if varBRSRoll == 52:
                        print("   A pair of gnomish wire cutters in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 53:
                        print("   A crowbar in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 54:
                        print("   A pair of dwarven pliers in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 55:
                        print("  ", varD6, "bag(s) of berries.")
                if varBRSRoll == 56:
                        print("  ", varD6, "lb(s) of salt.")
                if varBRSRoll == 57:
                        print("   A large wooden mallet in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 58:
                        print("   An empty waterskin in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 59:
                        print("   A small empty pouch.")
                if varBRSRoll == 60:
                        print("   A conical straw hat in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 61:
                        print("   A fancy hat in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 62:
                        print("   A peasant cap in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 63:
                        print("   A priest's skull cap in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 64:
                        print("  ", varD6, "sprig(s) of mistletoe.")
                if varBRSRoll == 65:
                        print("  ", varD10, "personal letter(s).")
                if varBRSRoll == 66:
                        print("   A carved flute in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 67:
                        print("   A small silver bell worth", varD10, "silver pieces.")
                if varBRSRoll == 68:
                        print("   A pair of deerskin gloves in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 69:
                        print("   A straight razor in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 70:
                        print("  ", varD6, "quart(s) of mead.")
                if varBRSRoll == 71:
                        print("  ", varD4, "quarts of lubricating oil.")
                if varBRSRoll == 72:
                        print("   A vial of strong acid (2d6 acid damage).")
                if varBRSRoll == 73:
                        print("   A sack of rare spices worth", (random.randint(4,40)), "silver pieces.")
                if varBRSRoll == 74:
                        print("   A pouch of 'pipe weed'.")
                if varBRSRoll == 75:
                        print("   A set of small tweezers in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 76:
                        print("   A wooden bowl.")
                if varBRSRoll == 77:
                        print("   A crystal prism worth", (random.randint (1,100)), "copper pieces.")
                if varBRSRoll == 79:
                        print("   An awl in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 80:
                        print("   A bottle of cologne of", random.choice(varQuality), "quality.")
                if varBRSRoll == 81:
                        print("   A bottle of perfume of", random.choice(varQuality), "quality.")
                if varBRSRoll == 82:
                        print("   A whetstone in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 83:
                        print("   A comb in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 84:
                        print("   A brush in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 85:
                        print("   A pouch of", random.choice(varQuality), "quality tea.")
                if varBRSRoll == 86:
                        print("  ", varD12, "large nails in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 87:
                        print("   A small lock of hair.")
                if varBRSRoll == 88:
                        print("  ", varD6, "owl pellets.")
                if varBRSRoll == 89:
                        print("   A small worry stone in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 90:
                        print("   A small bag of seed.")
                if varBRSRoll == 91:
                        print("  ", varD4, "lbs of raisins in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 92:
                        print("  ", varD4, "lbs of jerky in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 93:
                        print("   A small bag filled with", random.randint(1,100), "humanoid teeth.")
                if varBRSRoll == 94:
                        print("  ", varD4, "ounce(s) of fool's gold.")
                if varBRSRoll == 95:
                        print("   A set of iron shears in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 96:
                        print("   A small bottle of mineral oil.")
                if varBRSRoll == 97:
                        print("   A piece of origami in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 98:
                        print("   A small glass jar.")
                if varBRSRoll == 99:
                        print("   A small glass lens in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 100:
                        print("  ", varD10, "corks, in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 101:
                        print("   A brass locket with a portrait, in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 102:
                        print("   A torn out page from a book, in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 103:
                        print("   A set of false teeth in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 104:
                        print("   A child's toy in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 105:
                        print("  ", varD6, "colorful stones.")
                if varBRSRoll == 106:
                        print("   A bag of marbles in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 107:
                        print("   A sealed jar of urine.")
                if varBRSRoll == 108:
                        print("   A shrunken head in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 109:
                        print("   A continual flashlight.")
                if varBRSRoll == 110:
                        print("   A steel crowbar in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 111:
                        print("   A miner's pickaxe in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 112:
                        print("   A woodcutter's handaxe in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 113:
                        print("  ", varD4, "iron spikes in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 114:
                        print("  ", varD4, "steel crampons in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 115:
                        print("   A set of steel manacles in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 116:
                        print("  ", varD00, "feet of iron chain in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 117:
                        print("  ", varD00, "feet of hemp rope in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 118:
                        print("  ", varD00, "feet of silk rope in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 119:
                        print("   A small soup bowl in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 120:
                        print("   A carpenter's maul in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 121:
                        print("   A set of flint & steel in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 122:
                        print("   A small patch of ringmail in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 123:
                        print("   A set of kitchen utensils in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 124:
                        print("   A spool of twine.")
                if varBRSRoll == 125:
                        print("   A pair of delicate pliers in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 126:
                        print("   A fine file in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 127:
                        print("   A soup ladle in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 128:
                        print("   A fisher's block & tackle in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 129:
                        print("   A machete in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 130:
                        print("   A bridle in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 131:
                        print("   A dog whistle in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 132:
                        print("   A small step-stool in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 133:
                        print("   A burned out torch.")
                if varBRSRoll == 134:
                        print("   A small silver dagger in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 135:
                        print("   A pile of iron filings.")
                if varBRSRoll == 136:
                        print("   A snakeskin pouch in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 137:
                        print("   A wyldskin pouch.")
                if varBRSRoll == 138:
                        print("   A wyldskin backpack, worth 1 gp.")
                if varBRSRoll == 139:
                        print("   A dragonskin pouch, crafted from", random.choice(varDragonColor), "dragon hide, worth 5 gp.")
                if varBRSRoll == 140:
                        print("   A dragonskin backpack, crafted from", random.choice(varDragonColor), "dragon hide, worth 10 gp.")
                if varBRSRoll == 141:
                        print("   A large dragonskin sack, crafted from", random.choice(varDragonColor), "dragon hide, worth 25 gp.")
                if varBRSRoll == 142:
                        print("   A set of large needles in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 143:
                        print("   A tin of waterproofing oil in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 144:
                        print("   A primitive compass.")
                if varBRSRoll == 145:
                        print("   A grappling hook in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 146:
                        print("   An empty bottle.")
                if varBRSRoll == 147:
                        print("   A pint of paint.")
                if varBRSRoll == 148:
                        print("   A coarse whetstone in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 149:
                        print("   A small wooden wedge, useful for propping doors open.")
                if varBRSRoll == 150:
                        print("   A small armor polish kit in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 151:
                        print("   A steel hammer in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 152:
                        print("  ", varD6, "empty vials in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 153:
                        print("   A utility knife in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 154:
                        print("   A dusting of wood shavings.")
                if varBRSRoll == 155:
                        print("  ", varD12, "carpentry nails.")
                if varBRSRoll == 156:
                        print("   A large cooking pot in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 157:
                        print("  ", varD10, "pieces of chalk.")
                if varBRSRoll == 158:
                        print("   A winter coat in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 159:
                        print("   A small tin cup, probably from a mess kit.")
                if varBRSRoll == 160:
                        print("  ", varD12, "darts in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 161:
                        print("   A leather skullcap in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 162:
                        print("   A vial of expensive ink in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 163:
                        print("   An axe head in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 164:
                        print("   A spyglass in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 165:
                        print("   A carpenter's wood planer in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 166:
                        print("  ", varD4, "bone writing quills in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 167:
                        print("   A set of steel calipers in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 168:
                        print("   A pot helm in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 169:
                        print("   An iron padlock and key in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 170:
                        print("   A leather belt pouch in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 171:
                        print("   A fine riding pack in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 172:
                        print("   A military signal flag in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 173:
                        print("   An empty flask in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 174:
                        print("   A wooden box in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 175:
                        print("   A locked wooden box in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 176:
                        print("   A set of snow goggles in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 177:
                        print("   A sheaf of parchment in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 178:
                        print("   A small wooden mug in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 179:
                        print("   A fisher's gaff in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 180:
                        print("   A set of theives' tools in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 181:
                        print("   A hoof cleaning kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 182:
                        print("  ", varD12, "arrow heads in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 183:
                        print("  ", varD6, "ounce(s) of lamp oil.") 
                if varBRSRoll == 184:
                        print("   A leatherworker's awl in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 185:
                        print("   A leather crop in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 186:
                        print("   A small steel mirror in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 187:
                        print("   A carpenter's plumb in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 188:
                        print("   An adze in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 189:
                        print("   A treasure map in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 190:
                        print("   A crude measuring string.") 
                if varBRSRoll == 191:
                        print("   A sheaf of vellum in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 192:
                        print("   A 'portable' anvil in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 193:
                        print("   A soldier's trowel in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 194:
                        print("  ", varD20, "wooden stakes in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 195:
                        print("   An herbalist's mortar & pestle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 196:
                        print("   A carpenter's square in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 197:
                        print("   An empty scroll case in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 198:
                        print("   A small gemcutting kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 199:
                        print("   A carpenter's handsaw in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 200:
                        print("  ", varD4, "small sacks.") 
                if varBRSRoll == 201:
                        print("  ", varD4, "large sacks.") 
                if varBRSRoll == 202:
                        print("   A farming sickle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 203:
                        print("   An ancient compass in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 204:
                        print("   A falconer's glove in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 205:
                        print("   A", varD20, "lb bag of sand.") 
                if varBRSRoll == 206:
                        print("   A set of draftsman's tools in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 207:
                        print("   A bullwhip in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 208:
                        print("   A poison ring in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 209:
                        print("   A crude gas mask in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 210:
                        print("   A diver's snorkel in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 211:
                        print("   A small sharpened coin, tinged with blood.") 
                if varBRSRoll == 212:
                        print("   A farmer's hoe in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 213:
                        print("  ", varD6, "shuriken in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 214:
                        print("   A small broken wheel.") 
                if varBRSRoll == 215:
                        print("   A falconer's jesses in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 216:
                        print("   A letter written to home in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 217:
                        print("   A letter written from a lover in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 218:
                        print("   A book of poetry in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 219:
                        print("   A sprig of dried flowers.") 
                if varBRSRoll == 220:
                        print("   An engagement ring in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 221:
                        print("   A jeweler's loupe in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 222:
                        print("   A set of foreceps in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 223:
                        print("   A small makeup kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 224:
                        print("   A towel.") 
                if varBRSRoll == 225:
                        print("   A silken pillow in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 226:
                        print("   A small address book in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 227:
                        print("   A ring of keys in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 228:
                        print("   A shaving kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 229:
                        print("   A teddy bear in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 230:
                        print("   A knitting kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 231:
                        print("   A small sculpture of whittled wood in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 232:
                        print("   Extra shoestrings.") 
                if varBRSRoll == 233:
                        print("   A tin of boot polish in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 234:
                        print("   A tin of woad/warpaint in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 235:
                        print("   A small painting of a paramour's likeness in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 236:
                        print("  ", varD20, "silver teeth caps.") 
                if varBRSRoll == 237:
                        print("   A lucky rabbit's foot in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 238:
                        print("   A polished turtle shell in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 239:
                        print("   A homespun blanket in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 240:
                        print("  ", varD6, "lb(s) of soap.") 
                if varBRSRoll == 241:
                        print("   An ocarina in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 242:
                        print("   A tin of talcum powder in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 243:
                        print("   A set of playing cards in",random.choice(varConditionList), "condition." ) 
                if varBRSRoll == 244:
                        print("   A pipe and tobacco in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 245:
                        print("   A spare shirt in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 246:
                        print("   A toothbrush in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 247:
                        print("   A sewing kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 248:
                        print("  ", varD6, "lb(s) of lye.") 
                if varBRSRoll == 249:
                        print("   A straw hat in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 250:
                        print("   A prosthetic hook in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 251:
                        print("   A book of smutty literature in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 252:
                        print("   A wooden holy symbol dedicated to", random.choice(varDivineList))
                        print("      in", random.choice(varConditionList), "condition.")
                if varBRSRoll == 253:
                        print("   A set of dominoes in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 254:
                        print("   A ceramic pot in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 255:
                        print("   A dog bowl in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 256:
                        print("   A hand drum in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 257:
                        print("   A set of gaudy pantaloons in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 258:
                        print("   A book of jokes in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 259:
                        print("   A gravestone rubbing in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 260:
                        print("   A personal journal in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 261:
                        print("   A book of heraldry in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 262:
                        print("   A 'marital aid' in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 263:
                        print("   A dwarven dictionary in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 264:
                        print("   A set of fine undergarments in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 265:
                        print("   A fiddle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 266:
                        print("   A beret in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 267:
                        print("   An iron holy symbol dedicated to", random.choice(varDivineList))
                        print("      in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 268:
                        print("   A balaclava in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 269:
                        print("   A bolt of cloth in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 270:
                        print("   A bracelet in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 271:
                        print("   A pair of earrings in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 272:
                        print("   A dirty handkerchief.") 
                if varBRSRoll == 273:
                        print("   A wooden puzzle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 274:
                        print("   A bawdy mask in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 275:
                        print("   A set of gaming dice in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 276:
                        print("  ", varD10, "toy soliders in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 277:
                        print("   A winter scarf in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 278:
                        print("  ", varD10, "ceramic plates in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 279:
                        print("   A fancy tea set in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 280:
                        print("  ", varD4, "lb(s) of beeswax.") 
                if varBRSRoll == 281:
                        print("   A small prayer book dedicated to", random.choice(varDivineList))
                        print("      in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 282:
                        print("   A shipping invoice in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 283:
                        print("   A small dwarven cog in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 284:
                        print("   A sealed container of balefire in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 285:
                        print("   A beer stein in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 286:
                        print("   A to-do list in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 287:
                        print("   A book of fiction in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 288:
                        print("   A torc forged of", random.choice(varMagicMaterial)) 
                if varBRSRoll == 289:
                        print("   A disheveled washcloth.") 
                if varBRSRoll == 290:
                        print("   A rosary dedicated to", random.choice(varDivineList))
                        print("      in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 291:
                        print("   A sketchbook in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 292:
                        print("  ", varD12, "candles in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 293:
                        print("   A neatly folded flag.") 
                if varBRSRoll == 294:
                        print("   A small, crumpled caricature.") 
                if varBRSRoll == 295:
                        print("   A single black candle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 296:
                        print("  ", varD6, "vials of holy water.") 
                if varBRSRoll == 297:
                        print("  ", varD8, "lb(s) of coal.") 
                if varBRSRoll == 298:
                        print("   A dead canary.") 
                if varBRSRoll == 299:
                        print("   A ledger in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 300:
                        print("   A small statuette in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 301:
                        print("   A large dog collar in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 302:
                        print("   A cook's apron in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 303:
                        print("  ", varD6, "vials of milk of the poppy.") 
                if varBRSRoll == 304:
                        print("  ", varD6, "vials of unholy water.") 
                if varBRSRoll == 305:
                        print("   A pair of reading glasses in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 306:
                        print("   A cookbook in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 307:
                        print("   A history book in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 308:
                        print("   A small collection of fish bones.") 
                if varBRSRoll == 309:
                        print("   A small metal toothpick in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 310:
                        print("   An empty spellbook in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 311:
                        print("   A sinister spellbook in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 312:
                        print("   A live rabbit.") 
                if varBRSRoll == 313:
                        print("   A live octopus.") 
                if varBRSRoll == 314:
                        print("  ", varD4, "lb(s) of beets in.", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 315:
                        print("   A handful of candy.") 
                if varBRSRoll == 316:
                        print("  ", varD20, "lb(s) of raw venison in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 317:
                        print("  ", varD6, "lb(s) of truffles in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 318:
                        print("  ", varD20, "green apples.") 
                if varBRSRoll == 319:
                        print("  ", varD20, "red apples.") 
                if varBRSRoll == 320:
                        print("  ", varD20, "lb(s) of unripe fruit.") 
                if varBRSRoll == 321:
                        print("  ", varD4, "servings of ravioli in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 322:
                        print("  ", varD20, "toxic mushrooms. (save DC", (random.randint(10,16)), "/", (random.randint(1,6)), "d6 poison damage.)") 
                if varBRSRoll == 323:
                        print("  ", varD10, "lb(s) of purple jerky.") 
                if varBRSRoll == 324:
                        print("  ", varD10, "lb(s) of blue jerky.") 
                if varBRSRoll == 325:
                        print("  ", varD10, "lb(s) of violently pink jerky.") 
                if varBRSRoll == 326:
                        print("  ", varD00, "lb(s) of dragon meat in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 327:
                        print("  ", varD4, "bottle(s) of honey brandy in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 328:
                        print("   A small cloth bag containing", varD00, "tiny spiders of various types.") 
                if varBRSRoll == 329:
                        print("  ", varD12, "piece(s) of exotic fruit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 330:
                        print("   A handful of mint leaves in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 331:
                        print("  ", varD12, "orange(s) in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 332:
                        print("  ", varD6, "lb(s) of beans in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 333:
                        print("  ", varD00, "lb(s) of beans in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 334:
                        print("  ", varD6, "lb(s) of hops in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 335:
                        print("  ", varD00, "lb(s) of hops in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 336:
                        print("  ", varD4, "lb(s) of chocolate in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 337:
                        print("  ", varD20, "candied scorpion(s).") 
                if varBRSRoll == 338:
                        print("   A small sack of hardtack and biscuits in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 339:
                        print("   A live lobster.") 
                if varBRSRoll == 340:
                        print("  ", varD10, "live crabs.") 
                if varBRSRoll == 341:
                        print("   A skewer of grilled rat.") 
                if varBRSRoll == 342:
                        print("  ", varD10, "baguettes in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 343:
                        print("   A handful of edible flowers.") 
                if varBRSRoll == 344:
                        print("   A tin of earthworms in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 345:
                        print("  ", varD6, "lb(s) of grain in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 346:
                        print("  ", varD00, "lb(s) of grain in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 347:
                        print("   A wineskin full of red wine in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 348:
                        print("   A wineskin full of white wine in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 349:
                        print("   A wineskin full of piss.") 
                if varBRSRoll == 350:
                        print("  ", varD6, "lb(s) of almonds in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 351:
                        print("  ", varD00, "lb(s) of almonds in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 352:
                        print("   A leg of boiled dog.") 
                if varBRSRoll == 353:
                        print("   A wineskin full of dandelion wine in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 354:
                        print("  ", varD10, "bottled pints of melomel meade in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 355:
                        print("   A handful of juicy beetles.") 
                if varBRSRoll == 356:
                        print("  ", varD00, "lb(s) of rotten meat.") 
                if varBRSRoll == 357:
                        print("  ", varD6, "lb(s) of smoked salmon in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 358:
                        print("   A loaf of sweet brown bread in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 359:
                        print("  ", varD6, "lb(s) of pemmican.") 
                if varBRSRoll == 360:
                        print("  ", varD6, "lb(s) of coffee in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 361:
                        print("  ", varD00, "lb(s) of coffee in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 362:
                        print("  ", varD6, "lb(s) of honey in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 363:
                        print("  ", varD00, "lb(s) of honey in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 364:
                        print("  ", varD6, "lb(s) of cured beef in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 365:
                        print("  ", varD00, "lb(s) of cured beef in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 366:
                        print("   A small bag of popped corn in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 367:
                        print("  ", varD20, "lb(s) of dry pasta in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 368:
                        print("  ", varD4, "lb(s) of uncooked bacon in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 369:
                        print("  ", varD4, "lb(s) of raw cherries in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 370:
                        print("   A quart of fresh buttermilk.") 
                if varBRSRoll == 371:
                        print("  ", varD4, "bottles of wine in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 372:
                        print("   A handful of grilled leeks.") 
                if varBRSRoll == 373:
                        print("   A jar of pickled herring.") 
                if varBRSRoll == 374:
                        print("   A cart of fresh cabbages.") 
                if varBRSRoll == 375:
                        print("  ", varD6, "lb(s) of walnuts in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 376:
                        print("  ", varD00, "lb(s) of walnuts in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 377:
                        print("   A quart of fresh cream.") 
                if varBRSRoll == 378:
                        print("   A freshly butchered pig carcass.") 
                if varBRSRoll == 379:
                        print("  ", varD6, "lb(s) of flour in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 380:
                        print("  ", varD00, "lb(s) of flour in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 381:
                        print("  ", varD20, "tomatoes in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 382:
                        print("   A knapsack containing an apple pie in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 383:
                        print("   A roasted chicken in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 384:
                        print("   A tin full of ground horseradish.") 
                if varBRSRoll == 385:
                        print("   A tremendous dagwood sandwich.") 
                if varBRSRoll == 386:
                        print("   A jar of sourkraut.") 
                if varBRSRoll == 387:
                        print("   A pot of mustard in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 388:
                        print("   A small tin of jellied agave nectar in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 389:
                        print("   A single thousand year egg.") 
                if varBRSRoll == 390:
                        print("  ", varD6, "garlands of garlic.") 
                if varBRSRoll == 391:
                        print("   A quarter rack of lamb in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 392:
                        print("  ", varD8, "squash in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 393:
                        print("   A handful of chestnuts in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 394:
                        print("   A pound of preserved, salted fish.") 
                if varBRSRoll == 395:
                        print("   A dried bit of horse hide.") 
                if varBRSRoll == 396:
                        print("   A rack of pork in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 397:
                        print("   A handful of sunflower seeds.") 
                if varBRSRoll == 398:
                        print("   A handful of pure sea salt.") 
                if varBRSRoll == 399:
                        print("  ", varD20, "chicken feet.") 
                if varBRSRoll == 400:
                        print("  ", varD6, "unpeeled potatoes.") 
                if varBRSRoll == 401:
                        print("  ", varD4, "meat pies in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 402:
                        print("   A small pumpkin.") 
                if varBRSRoll == 403:
                        print("  ", varD4, "lb(s) of dried apricots.") 
                if varBRSRoll == 404:
                        print("  ", varD6, "pheasant(s).") 
                if varBRSRoll == 405:
                        print("  ", varD6, "plucked duck(s).") 
                if varBRSRoll == 406:
                        print("   A small block of goatshead cheese.", ) 
                if varBRSRoll == 407:
                        print("  ", varD4, "sprigs of hemlock.") 
                if varBRSRoll == 408:
                        print("  ", varD6, "lb(s) of cornmeal.") 
                if varBRSRoll == 409:
                        print("  ", varD10, "lb(s) of snake meat in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 410:
                        print("  ", varD6, "lb(s) of sliced roast beef in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 411:
                        print("   A half-rack of salted ribs in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 412:
                        print("   A jar of broth in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 413:
                        print("   A jar of rendered fat in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 414:
                        print("  ", varD4, "lb(s) of carrots.") 
                if varBRSRoll == 415:
                        print("   A bag of dried willow tree bark in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 416:
                        print("  ", varD4, "loaves of flatbread.") 
                if varBRSRoll == 417:
                        print("   A knapsack of goblin pastries.") 
                if varBRSRoll == 418:
                        print("  ", varD10, "turnips in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 419:
                        print("   A necklace of wildcat fangs.") 
                if varBRSRoll == 420:
                        print("  ", varD10, "pine cones.") 
                if varBRSRoll == 421:
                        print("   A set of movable type in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 422:
                        print("   A finger-painting in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 423:
                        print("   A dessicated tentacle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 424:
                        print("   A sinister mask in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 425:
                        print("   A set of rune stones in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 426:
                        print("   A petrified pixie.") 
                if varBRSRoll == 427:
                        print("   A collection of small petrified animals.") 
                if varBRSRoll == 428:
                        print("   A tin of ground goat hoof.") 
                if varBRSRoll == 429:
                        print("   A vial of strange powder.") 
                if varBRSRoll == 430:
                        print("   A ranting letter in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 431:
                        print("   A cast footprint in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 432:
                        print("  ", varD10, "strange coins in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 433:
                        print("   A shoddy treasure map.") 
                if varBRSRoll == 434:
                        print("   A spare doorknob.") 
                if varBRSRoll == 435:
                        print("   A small pot of paint.") 
                if varBRSRoll == 436:
                        print("   A humanoid skull in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 437:
                        print("   A handful of glowing fungus.") 
                if varBRSRoll == 438:
                        print("   A dead two-headed snake.") 
                if varBRSRoll == 439:
                        print("   A songshard crystal in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 440:
                        print("   A clay cast of a humanoid face in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 441:
                        print("   A large piece of ivory in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 442:
                        print("   A carved mug in the shape of an animal in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 443:
                        print("   A single child's shoe in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 444:
                        print("   A ring of orc's teeth.") 
                if varBRSRoll == 445:
                        print("   A crumpled plan for a mutual fund.") 
                if varBRSRoll == 446:
                        print("   A goblin crest in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 447:
                        print("   A noble crest in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 448:
                        print("   A token for a free drink.") 
                if varBRSRoll == 449:
                        print("   A chunk of fine marble.") 
                if varBRSRoll == 450:
                        print("   A very friendly live pet rat.") 
                if varBRSRoll == 451:
                        print("   A golden thimble in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 452:
                        print("   A notched wooden dowel, stained with blood.") 
                if varBRSRoll == 453:
                        print("   A huge, 2 lb ball of lint.") 
                if varBRSRoll == 454:
                        print("   A square foot of canvas cut from a sail, with partial colors.") 
                if varBRSRoll == 455:
                        print("   A lizard-foot backscratcher.") 
                if varBRSRoll == 456:
                        print("   An ornate door hinge in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 457:
                        print("   A scythe shaped letter opener in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 458:
                        print("   A tiny noose.") 
                if varBRSRoll == 459:
                        print("  ", varD12, "lb(s) of dead fish.") 
                if varBRSRoll == 460:
                        print("   A well-kept journal of a noble's bowel movements.") 
                if varBRSRoll == 461:
                        print("   A strange deck of cards in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 462:
                        print("   A deck of playing cards in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 463:
                        print("   A roll of propaganda posters in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 464:
                        print("   A sealed last will and testament in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 465:
                        print("   A bloody flag in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 466:
                        print("   A single severed finger.") 
                if varBRSRoll == 467:
                        print("  ", varD6, "mice, glued together.") 
                if varBRSRoll == 468:
                        print("  ", varD6, "large sack(s) of earth.") 
                if varBRSRoll == 469:
                        print("   A deranged weasel, very much alive.") 
                if varBRSRoll == 470:
                        print("   A necklace of humanoid ears.") 
                if varBRSRoll == 471:
                        print("   A necklace of beast ears.") 
                if varBRSRoll == 472:
                        print("   A necklace of beast fangs.") 
                if varBRSRoll == 473:
                        print("   A necklace of beast claws.") 
                if varBRSRoll == 474:
                        print("   A child's femur in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 475:
                        print("   A small cask filled with urine.") 
                if varBRSRoll == 476:
                        print("   A handful of wooden coins in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 477:
                        print("   A 30' rope ladder in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 478:
                        print("   A blood-soaked dagger in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 479:
                        print("   A gaudy cloak pin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 480:
                        print("   A set of jingling bells in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 481:
                        print("   A single, massive monstrous fingernail.") 
                if varBRSRoll == 482:
                        print("   An astrology chart in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 483:
                        print("   A dowsing rod in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 484:
                        print("   An ancient deed, sealed against the ravages of time.") 
                if varBRSRoll == 485:
                        print("   A set of children's blocks in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 486:
                        print("   A harlequin's hat in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 487:
                        print("   A set of antlers or horns in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 488:
                        print("   A taxidermied pet in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 489:
                        print("   A taxidermied beast in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 490:
                        print("   A taxidermied monster in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 491:
                        print("   A small basket of bees.") 
                if varBRSRoll == 492:
                        print("   A map of a strange city in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 493:
                        print("   A large mithril spring in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 494:
                        print("   A small adamantine cog in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 495:
                        print("   A simple music box in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 496:
                        print("   A piece of tattooed humanoid skin.") 
                if varBRSRoll == 497:
                        print("   A smutty flip book in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 498:
                        print("   A small tin of guano in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 499:
                        print("   The top of a battle standard in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 500:
                        print("   A tiny flea circus in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 501:
                        print("   A tin of smoking herbs.") 
                if varBRSRoll == 502:
                        print("   A scrawled password to a secret meeting.") 
                if varBRSRoll == 503:
                        print("   A large ship in a bottle in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 504:
                        print("   A bat-winged plate helm in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 505:
                        print("   A horned plate helm in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 506:
                        print("   A delicate bag full of cobwebs.") 
                if varBRSRoll == 507:
                        print("   A crumbling book filled with a lich's autobiography.") 
                if varBRSRoll == 508:
                        print("   A crude map of a manor house.") 
                if varBRSRoll == 509:
                        print("   A perfect marble sphere in pristine condition.") 
                if varBRSRoll == 510:
                        print("   A small pamphlet titled 'The Arcane and You'.") 
                if varBRSRoll == 511:
                        print("   A collection of wine corks in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 512:
                        print("   A mercenary recruitment letter in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 513:
                        print("   A giant insect mandible in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 514:
                        print("   A magical scroll of protection from a trivial threat.") 
                if varBRSRoll == 515:
                        print("   A magical scroll of protection from a trivial threat.") 
                if varBRSRoll == 516:
                        print("   A glass skull in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 517:
                        print("   A small vial of humanoid blood.") 
                if varBRSRoll == 518:
                        print("   A small vial of animal blood.") 
                if varBRSRoll == 519:
                        print("   A comically inflated taxidermied toad.") 
                if varBRSRoll == 520:
                        print("   A single eyeball in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 521:
                        print("   A bag containing", varD20, "eyeballs in various conditions.") 
                if varBRSRoll == 522:
                        print("   A belt of shrunken heads in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 523:
                        print("   A large sack of feathers in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 524:
                        print("   A", varD20, "lb cannonball.") 
                if varBRSRoll == 525:
                        print("   A flask of acid in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 526:
                        print("   An adventurer's kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 527:
                        print("   A flask of alchemist's fire in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 528:
                        print("   An adventurer's kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 529:
                        print("  ", varD20, "arrows in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 530:
                        print("  ", varD20, "bolts in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 531:
                        print("  ", varD20, "brightspark rounds in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 532:
                        print("  ", varD20, "sling bullets in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 533:
                        print("   A dose of antitoxin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 534:
                        print("  ", varD00, "ball bearings in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 535:
                        print("   A bucket in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 536:
                        print("  ", varD12, "caltrops in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 537:
                        print("  ", varD12, "pieces of chalk in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 538:
                        print("   A disguise kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 539:
                        print("   A healer's kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 540:
                        print("   An hourglass in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 541:
                        print("   A hunting trap in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 542:
                        print("  ", varD4, "clay jugs in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 543:
                        print("   A common lamp in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 544:
                        print("   A bullseye lamp in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 545:
                        print("   A magnifying glass in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 546:
                        print("   A mess kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 547:
                        print("   A war horn in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 548:
                        print("  ", varD12, "pitons in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 549:
                        print("   A portable ram in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 550:
                        print("   A stick of sealing wax in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 551:
                        print("   A gravedigger's shovel in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 552:
                        print("   A canvas tent in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 553:
                        print("   A waterskin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 554:
                        print("   A filled waterskin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 555:
                        print("   A befouled waterskin.") 
                if varBRSRoll == 556:
                        print("   A small set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 557:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 558:
                        print("   A small set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 559:
                        print("   A small set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 560:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 561:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 562:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 563:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 564:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 565:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 566:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 567:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 568:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 569:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 570:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 571:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 572:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 573:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 574:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 575:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 576:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 577:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 578:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 579:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 580:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 581:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 582:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 583:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 584:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 585:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 586:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 587:
                        print("   A medium set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 588:
                        print("   A small set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 589:
                        print("   A small set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 590:
                        print("   A small set of", random.choice(varRandomArmor), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 591:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 592:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 593:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 594:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 595:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 596:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 597:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 598:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 599:
                        print("   A", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 600:
                        print("   A pygmy blowgun in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 601:
                        print("   A drow hand crossbow in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 602:
                        print("   A mage's orb in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 603:
                        print("   A mage's wand in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 604:
                        print("   A mage's rod in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 605:
                        print("   A mage's staff in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 606:
                        print("   A set of arctic camouflage in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 607:
                        print("   A set of stone camouflage in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 608:
                        print("   A set of forest camouflage in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 609:
                        print("   A set of desert camouflage in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 610:
                        print("   A dwarven blasting kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 611:
                        print("   A dwarven land mine in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 612:
                        print("   A dwarven blast tube in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 613:
                        print("   An adamantine crowbard.") 
                if varBRSRoll == 614:
                        print("   A ten foot pole in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 615:
                        print("   A dose of Aboleth Mucus (Con DC 12)") 
                if varBRSRoll == 616:
                        print("   A quart of ipecac syrup.") 
                if varBRSRoll == 617:
                        print("   A", varD10, "lb dwarven magnet.") 
                if varBRSRoll == 618:
                        print("   An ancestral blade in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 619:
                        print("   Mjolnir. No, you can't lift it.") 
                if varBRSRoll == 620:
                        print("   A sword, plunged blade first into a massive stone.") 
                if varBRSRoll == 621:
                        print("   A mithril", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 622:
                        print("   An adamantine", random.choice(varRandomWeapon)) 
                if varBRSRoll == 623:
                        print("   A mithril", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 624:
                        print("   A mithril", random.choice(varRandomWeapon), "in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 625 and varBRSRoll <= 629:
                        print("   An abacus in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 630 and varBRSRoll <= 639:
                        print("   An Alchemist's Kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 640:
                        print("   A masterwork Alchemist's Kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 641 and varBRSRoll <= 650:
                        print("   A set of Artisan's Tools in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 651 and varBRSRoll <= 660:
                        print("   A set of spare cloths in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 661 and varBRSRoll <= 670:
                        print("   A set of navigator's tools in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 671 and varBRSRoll <= 675:
                        print("   A poisoner's kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll == 676:
                        varSpellRoundLevel=(random.randint(1,20)) + (varEL)
                        if varSpellRoundLevel >= 1 and varSpellRoundLevel <=10:
                                print("   A Brightspark Spell Round of", random.choice(varFirstLevelSpells))
                        if varSpellRoundLevel >= 11 and varSpellRoundLevel <=15:
                                print("   A Brightspark Spell Round of", random.choice(varSecondLevelSpells))                                   
                        if varSpellRoundLevel >= 16 and varSpellRoundLevel <=20:
                                print("   A Brightspark Spell Round of", random.choice(varThirdLevelSpells))
                        if varSpellRoundLevel >= 21 and varSpellRoundLevel <=25:
                                print("   A Brightspark Spell Round of", random.choice(varFourthLevelSpells))  
                        if varSpellRoundLevel >= 26 and varSpellRoundLevel <=30:
                                print("   A Brightspark Spell Round of", random.choice(varFifthLevelSpells))            
                        if varSpellRoundLevel >= 31 and varSpellRoundLevel <=32:
                                print("   A Brightspark Spell Round of", random.choice(varSixthLevelSpells))
                        if varSpellRoundLevel >= 33 and varSpellRoundLevel <=34:
                                print("   A Brightspark Spell Round of", random.choice(varSeventhLevelSpells))                                  
                        if varSpellRoundLevel >= 35 and varSpellRoundLevel <=36:
                                print("   A Brightspark Spell Round of", random.choice(varEighthLevelSpells))
                        if varSpellRoundLevel >= 37 and varSpellRoundLevel <=40:
                                print("   A Brightspark Spell Round of", random.choice(varNinthLevelSpells))    
                if varBRSRoll == 678:
                        print("   A Tome of Lore (your DM determines the Tome's subject).") 
                if varBRSRoll >= 679 and varBRSRoll <= 686:
                        print("   A vial bandolier.") 
                if varBRSRoll >= 687 and varBRSRoll <= 691:
                        print("   A vial belt.") 
                if varBRSRoll >= 692 and varBRSRoll <= 705:     
                        print("   An adventurer's kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 706 and varBRSRoll <= 710:     
                        print("   A flask of alchemist's fire in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 711 and varBRSRoll <= 720:     
                        print("  ", varD20, "arrows in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 721 and varBRSRoll <= 730:     
                        print("  ", varD20, "bolts in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 731 and varBRSRoll <= 735:     
                        print("  ", varD20, "brightspark rounds in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 736 and varBRSRoll <= 740:     
                        print("  ", varD20, "sling bullets in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 741 and varBRSRoll <= 745:     
                        print("   A dose of antitoxin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 746 and varBRSRoll <= 750:     
                        print("  ", varD12, "caltrops in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 751 and varBRSRoll <= 755:     
                        print("  ", varD12, "pieces of chalk in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 756 and varBRSRoll <= 760:     
                        print("   A disguise kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 761 and varBRSRoll <= 770:     
                        print("   A healer's kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 771 and varBRSRoll <= 773:     
                        print("   An hourglass in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 774 and varBRSRoll <= 777:     
                        print("   A hunting trap in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 778 and varBRSRoll <= 782:     
                        print("  ", varD4, "clay jugs in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 783 and varBRSRoll <= 790:     
                        print("   A common lamp in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 791 and varBRSRoll <= 795:     
                        print("   A bullseye lamp in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 796 and varBRSRoll <= 797:     
                        print("   A magnifying glass in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 798 and varBRSRoll <= 803:     
                        print("   A mess kit in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 804 and varBRSRoll <= 808:     
                        print("   A war horn in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 809 and varBRSRoll <= 812:     
                        print("  ", varD12, "pitons in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 813 and varBRSRoll <= 815:     
                        print("   A stick of sealing wax in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 816 and varBRSRoll <= 825:     
                        print("   A canvas tent in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 826 and varBRSRoll <= 860:     
                        print("   A waterskin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 861 and varBRSRoll <= 865:     
                        print("   A filled waterskin in", random.choice(varConditionList), "condition.") 
                if varBRSRoll >= 866 and varBRSRoll <= 880:
                        print("   A bedroll in", random.choice(varConditionList), "condition.")
                if varBRSRoll >= 881 and varBRSRoll <= 1000:
                        print("  ", varD4, "ounce(s) of", random.choice(varHerbalism), "in", random.choice(varConditionList), "condition.")

                        #increase stuffsofar so the loop ends eventually        
                varStuffSoFar = varStuffSoFar +2
                
        print("")
        print("Hit enter for another set of loot.")
        print("")
        print("")
        print("")
        print("")
        print("")
        input()
        

'''



def run_loot(level):
    """Run the embedded loot generator once and return its output."""
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.py') as tmp:
        tmp.write(CLI_SCRIPT)
        tmp_path = tmp.name
    try:
        proc = subprocess.Popen([
            sys.executable, tmp_path
        ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        proc.stdin.write(f"{level}\n")
        proc.stdin.flush()

        lines = []
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            lines.append(line)
            if 'Hit enter for another set of loot.' in line:
                proc.kill()
                break
        proc.communicate()
    finally:
        os.unlink(tmp_path)

    output = ''.join(lines)
    prompt = 'Encounter level? (1-30) '
    if output.startswith(prompt):
        output = output[len(prompt):]
    return output


def _extract_magic_item(output):
    parts = output.split('-----------------------------------')
    if len(parts) >= 4:
        return parts[3].strip() or 'No magic item generated.'
    return 'No magic item generated.'


def run_magic_item(level, attempts=5):
    """Return a magic item for the given level, retrying if none found."""
    item = 'No magic item generated.'
    for _ in range(attempts):
        item = _extract_magic_item(run_loot(level))
        if 'no magic item' not in item.lower():
            break
    return item


def _split_sections(text):
    """Split raw loot output into its component sections."""
    sections = [s.strip() for s in text.split('-----------------------------------')]
    if not sections:
        return sections

    sections[0] = sections[0].replace('====================================', '').strip()
    if sections[-1].endswith('Hit enter for another set of loot.'):
        sections[-1] = sections[-1].split('Hit enter')[0]
    sections[-1] = sections[-1].replace('====================================', '').strip()

    # Move any herbal pouch section to the incidental items section
    for idx, sec in enumerate(sections):
        if 'pouch of herbal ingredients' in sec.lower():
            herbal = sections.pop(idx)
            if sections:
                sections[-1] = f"{herbal}\n{sections[-1]}".strip()
            else:
                sections.append(herbal)
            break

    return sections


def run_hoard(level, count=5):
    """Generate multiple sets of loot for a treasure hoard."""
    aggregated = [[] for _ in LootzApp.SECTION_LABELS]
    for _ in range(count):
        for idx, part in enumerate(_split_sections(run_loot(level))):
            if idx < len(aggregated):
                aggregated[idx].append(part)
    return ['\n\n'.join(parts) for parts in aggregated]


class LootzApp(tk.Tk):
    """Simple Tkinter GUI for the loot generator."""

    SECTION_LABELS = [
        "Coins",
        "Gems / Art",
        "Consumables",
        "Magic Items",
        "Incidental Items",
    ]

    def __init__(self):
        super().__init__()
        self.title('Lootz GUI')

        tk.Label(self, text='Encounter Level (1-30):').pack(pady=5)
        self.level_entry = tk.Entry(self)
        self.level_entry.pack(pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text='Generate Loot', command=self.generate).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text='Generate Magic Item', command=self.generate_magic).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text='Generate Hoard', command=self.generate_hoard).pack(side=tk.LEFT, padx=5)
        # create two-column pane layout for the sections
        self.paned = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        self.left_col = tk.PanedWindow(self.paned, orient=tk.VERTICAL)
        self.right_col = tk.PanedWindow(self.paned, orient=tk.VERTICAL)
        self.paned.add(self.left_col)
        self.paned.add(self.right_col)

        self.section_widgets = []
        half = (len(self.SECTION_LABELS) + 1) // 2
        for idx, label in enumerate(self.SECTION_LABELS):
            parent = self.left_col if idx < half else self.right_col
            frame = tk.Frame(parent)
            tk.Label(frame, text=label).pack(anchor='w')
            txt = scrolledtext.ScrolledText(frame, width=40, height=6)
            txt.pack(fill=tk.BOTH, expand=True)
            parent.add(frame)
            self.section_widgets.append(txt)

    def generate(self):
        """Generate loot and populate each pane."""
        level = self.level_entry.get().strip()
        if not level:
            return
        sections = _split_sections(run_loot(level))

        for idx, widget in enumerate(self.section_widgets):
            widget.delete('1.0', tk.END)
            if idx < len(sections):
                widget.insert(tk.END, sections[idx])
            else:
                widget.insert(tk.END, '')

    def generate_hoard(self):
        """Generate multiple loot sets and display them."""
        level = self.level_entry.get().strip()
        if not level:
            return
        sections = run_hoard(level)
        for idx, widget in enumerate(self.section_widgets):
            widget.delete("1.0", tk.END)
            if idx < len(sections):
                widget.insert(tk.END, sections[idx])
            else:
                widget.insert(tk.END, "")

    def generate_magic(self):
        """Display a single magic item in the first pane."""
        level = self.level_entry.get().strip()
        if not level:
            return
        result = run_magic_item(level)
        for widget in self.section_widgets:
            widget.delete('1.0', tk.END)
        self.section_widgets[0].insert(tk.END, result)

if __name__ == '__main__':
    app = LootzApp()
    app.mainloop()
