from . import bbModule
from ....bbConfig import bbData

class bbCompressorModule(bbModule.bbModule):
    def __init__(self, name, aliases, cargoMultiplier=1.0, value=0, wiki="", manufacturer="", icon="", emoji=""):
        super(bbCompressorModule, self).__init__(name, aliases, cargoMultiplier=cargoMultiplier, value=value, wiki=wiki, manufacturer=manufacturer, icon=icon, emoji=emoji)


    def getType(self):
        return bbCompressorModule


def fromDict(moduleDict):
    return bbCompressorModule(moduleDict["name"], moduleDict["aliases"] if "aliases" in moduleDict else [], cargoMultiplier=moduleDict["cargoMultiplier"] if "cargoMultiplier" in moduleDict else 1,
                            value=moduleDict["value"] if "value" in moduleDict else 0, wiki=moduleDict["wiki"] if "wiki" in moduleDict else "",
                            manufacturer=moduleDict["manufacturer"] if "manufacturer" in moduleDict else "", icon=moduleDict["icon"] if "icon" in moduleDict else bbData.rocketIcon,
                            emoji=moduleDict["emoji"] if "emoji" in moduleDict else "")
