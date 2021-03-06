from . import bbModule
from ....bbConfig import bbData

class bbCloakModule(bbModule.bbModule):
    def __init__(self, name, aliases, duration=0, value=0, wiki="", manufacturer="", icon="", emoji=""):
        super(bbCloakModule, self).__init__(name, aliases, value=value, wiki=wiki, manufacturer=manufacturer, icon=icon, emoji=emoji)
        
        self.duration = duration

    
    def statsStringShort(self):
        return "Duration: " + str(self.duration) + "s" if self.duration != 0 else "No effect"

    
    def getType(self):
        return bbCloakModule


def fromDict(moduleDict):
    return bbCloakModule(moduleDict["name"], moduleDict["aliases"] if "aliases" in moduleDict else [], duration=moduleDict["duration"] if "duration" in moduleDict else 0,
                            value=moduleDict["value"] if "value" in moduleDict else 0, wiki=moduleDict["wiki"] if "wiki" in moduleDict else "",
                            manufacturer=moduleDict["manufacturer"] if "manufacturer" in moduleDict else "", icon=moduleDict["icon"] if "icon" in moduleDict else bbData.rocketIcon,
                            emoji=moduleDict["emoji"] if "emoji" in moduleDict else "")