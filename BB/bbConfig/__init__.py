"""
⚠ WARNING: MARKED FOR CHANGE ⚠
The following function is provisional and marked as planned for overhaul.
Details: Item rarities are to be overhauled, from a linear scale to exponential. In layman's terms, mid price-range items are to become more common.

"""

import operator

from . import bbData
from . import bbConfig
from ..bbObjects.bounties import bbCriminal, bbSystem
from ..bbObjects.items import bbShip, bbModuleFactory, bbWeapon, bbShipUpgrade, bbTurret

# generate bbCriminal objects from data in bbData
for criminalDict in bbData.builtInCriminalData.values():
    bbData.builtInCriminalObjs[criminalDict["name"]] = bbCriminal.fromDict(criminalDict)
    bbData.builtInCriminalObjs[criminalDict["name"]].builtIn = True
    bbData.builtInCriminalData[criminalDict["name"]]["builtIn"] = True

# generate bbSystem objects from data in bbData
for systemDict in bbData.builtInSystemData.values():
    bbData.builtInSystemObjs[systemDict["name"]] = bbSystem.fromDict(systemDict)
    bbData.builtInSystemData[systemDict["name"]]["builtIn"] = True
    bbData.builtInSystemObjs[systemDict["name"]].builtIn = True

# # generate bbShip objects from data in bbData
# # NOTE: ONLY for use in shop listings - buying of ships should make a deep copy of the object, or 
# # spawn a new one from the data dict
# for shipDict in bbData.builtInShipData.values():
#     bbData.builtInShipObjs[shipDict["name"]] = bbShip.fromDict(shipDict)

# generate bbModule objects from data in bbData
for moduleDict in bbData.builtInModuleData.values():
    bbData.builtInModuleObjs[moduleDict["name"]] = bbModuleFactory.fromDict(moduleDict)
    bbData.builtInModuleData[moduleDict["name"]]["builtIn"] = True
    bbData.builtInModuleObjs[moduleDict["name"]].builtIn = True

# generate bbWeapon objects from data in bbData
for weaponDict in bbData.builtInWeaponData.values():
    bbData.builtInWeaponObjs[weaponDict["name"]] = bbWeapon.fromDict(weaponDict)
    bbData.builtInWeaponData[weaponDict["name"]]["builtIn"] = True
    bbData.builtInWeaponObjs[weaponDict["name"]].builtIn = True

# generate bbUpgrade objects from data in bbData
for upgradeDict in bbData.builtInUpgradeData.values():
    bbData.builtInUpgradeObjs[upgradeDict["name"]] = bbShipUpgrade.fromDict(upgradeDict)
    bbData.builtInUpgradeData[upgradeDict["name"]]["builtIn"] = True
    bbData.builtInUpgradeObjs[upgradeDict["name"]].builtIn = True

# generate bbTurret objects from data in bbData
for turretDict in bbData.builtInTurretData.values():
    bbData.builtInTurretObjs[turretDict["name"]] = bbTurret.fromDict(turretDict)
    bbData.builtInTurretData[turretDict["name"]]["builtIn"] = True
    bbData.builtInTurretObjs[turretDict["name"]].builtIn = True


# Sort ships by value
unsortedShipKeys = {}
for shipKey in bbData.builtInShipData.keys():
    unsortedShipKeys[shipKey] = bbData.builtInShipData[shipKey]["value"]
sortedShipKeys = sorted(unsortedShipKeys.items(), key=operator.itemgetter(1))[::-1]

shipKeysNum = {}
# Make a list of ship KEYS ranked by value for random picking
for keyIndex in range(len(sortedShipKeys) - 1, -1, -1):
    # currentShip = bbData.builtInShipObjs[sortedShipKeys[keyIndex][0]]
    currentShip = sortedShipKeys[keyIndex][0]
    shipKeysNum[currentShip] = int(keyIndex / bbConfig.numShipRanks)
    for n in range(int(keyIndex / bbConfig.numShipRanks)):
        bbData.rankedShipKeys.append(currentShip)

numRankedShipKeys = len(bbData.rankedShipKeys)
for shipKey in bbData.builtInShipData.keys():
    bbData.shipKeySpawnRates[shipKey] = round((shipKeysNum[shipKey] / numRankedShipKeys) * 100, 2)


# Sort weapons by value
unsortedWeaponKeys = {}
for weaponKey in bbData.builtInWeaponObjs.keys():
    unsortedWeaponKeys[weaponKey] = bbData.builtInWeaponObjs[weaponKey].value
sortedWeaponKeys = sorted(unsortedWeaponKeys.items(), key=operator.itemgetter(1))[::-1]

weaponKeysNum = {}
# Make a list of weapons ranked by value for random picking
for keyIndex in range(len(sortedWeaponKeys) - 1, -1, -1):
    currentWeapon = bbData.builtInWeaponObjs[sortedWeaponKeys[keyIndex][0]]
    weaponKeysNum[sortedWeaponKeys[keyIndex][0]] = int(keyIndex / bbConfig.numWeaponRanks)
    for n in range(int(keyIndex / bbConfig.numWeaponRanks)):
        bbData.rankedWeaponObjs.append(currentWeapon)

numRankedWeaponObjs = len(bbData.builtInWeaponObjs)

for weapon in bbData.builtInWeaponObjs.values():
    weapon.shopSpawnRate = round((weaponKeysNum[weapon.name] / numRankedWeaponObjs) * 100, 2)


# Sort modules by value
unsortedModuleKeys = {}
for moduleKey in bbData.builtInModuleObjs.keys():
    unsortedModuleKeys[moduleKey] = bbData.builtInModuleObjs[moduleKey].value
sortedModuleKeys = sorted(unsortedModuleKeys.items(), key=operator.itemgetter(1))[::-1]

moduleKeysNum = {}
# Make a list of modules ranked by value for random picking
for keyIndex in range(len(sortedModuleKeys) - 1, -1, -1):
    currentModule = bbData.builtInModuleObjs[sortedModuleKeys[keyIndex][0]]
    moduleKeysNum[sortedModuleKeys[keyIndex][0]] = int(keyIndex / bbConfig.numModuleRanks)
    for n in range(int(keyIndex / bbConfig.numModuleRanks)):
        bbData.rankedModuleObjs.append(currentModule)

numRankedModuleObjs = len(bbData.builtInModuleObjs)

for module in bbData.builtInModuleObjs.values():
    module.shopSpawnRate = round((moduleKeysNum[module.name] / numRankedModuleObjs) * 100, 2)


# Sort turrets by value
unsortedTurretKeys = {}
for turretKey in bbData.builtInTurretObjs.keys():
    unsortedTurretKeys[turretKey] = bbData.builtInTurretObjs[turretKey].value
sortedTurretKeys = sorted(unsortedTurretKeys.items(), key=operator.itemgetter(1))[::-1]

turretKeysNum = {}
# Make a list of turrets ranked by value for random picking
for keyIndex in range(len(sortedTurretKeys) - 1, -1, -1):
    currentTurret = bbData.builtInTurretObjs[sortedTurretKeys[keyIndex][0]]
    turretKeysNum[sortedTurretKeys[keyIndex][0]] = int(keyIndex / bbConfig.numTurretRanks)
    for n in range(int(keyIndex / bbConfig.numTurretRanks)):
        bbData.rankedTurretObjs.append(currentTurret)

numRankedTurretObjs = len(bbData.builtInTurretObjs)

for turret in bbData.builtInTurretObjs.values():
    turret.shopSpawnRate = round(((turretKeysNum[turret.name] / numRankedTurretObjs) * 100) * (bbConfig.turretSpawnProbability / 100), 2)
