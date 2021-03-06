from . import bbModule
from ....bbConfig import bbData

class bbTransfusionBeamModule(bbModule.bbModule):
    def __init__(self, name, aliases, HPps=0, count=0, value=0, wiki="", manufacturer="", icon="", emoji=""):
        super(bbTransfusionBeamModule, self).__init__(name, aliases, value=value, wiki=wiki, manufacturer=manufacturer, icon=icon, emoji=emoji)

        self.HPps = HPps
        self.count = count


    def statsStringShort(self):
        return "*HP/s: " + str(self.HPps) + ", Count: " + str(self.count) + "*"


    def getType(self):
        return bbTransfusionBeamModule


def fromDict(moduleDict):
    return bbTransfusionBeamModule(moduleDict["name"], moduleDict["aliases"] if "aliases" in moduleDict else [], HPps=moduleDict["HPps"] if "HPps" in moduleDict else 0,
                            count=moduleDict["count"] if "count" in moduleDict else 0,
                            value=moduleDict["value"] if "value" in moduleDict else 0, wiki=moduleDict["wiki"] if "wiki" in moduleDict else "",
                            manufacturer=moduleDict["manufacturer"] if "manufacturer" in moduleDict else "", icon=moduleDict["icon"] if "icon" in moduleDict else bbData.rocketIcon,
                            emoji=moduleDict["emoji"] if "emoji" in moduleDict else "")
