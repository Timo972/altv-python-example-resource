import alt

alt.log("Hello World!")

DEFAULT_VEH_NAME = "krieger"

def maxVehicle(vehicle):
    if vehicle.modKit == 0 and vehicle.modKitsCount > 0:
        vehicle.modKit = 1
    elif vehicle.modKit == 0 and vehicle.modKitsCount == 0:
        alt.logError("Vehicle {0} has no modkit".format(vehicle.id))
        return
    elif vehicle.modKit == 1:
        alt.log("Vehicle {0} already maxed".format(vehicle.id))
        
    modTypes = 48

    for modType in range(modTypes):
        modMax = vehicle.getModsCount(modType)
        if modMax > 0:
            vehicle.setMod(modType, modMax)

    alt.log("Vehicle {0} maxed".format(vehicle.id))


def playerConnect(player):
    player.model = "mp_m_freemode_01"
    player.spawn(5, 5, 76, 0)
    veh = alt.Vehicle(DEFAULT_VEH_NAME, 5, 5, 76, 0, 0, 0)
    veh.setMeta("name", DEFAULT_VEH_NAME)
    alt.log("Created vehicle")
    alt.log("Vehicle ID: {}".format(veh.id))

def playerEnterVehicle(player, vehicle, seat):
    alt.log("Player {0} entered vehicle {1}".format(player.name, vehicle.id))
    vehicle.customPrimaryColor = alt.RGBA(243, 255, 0, 255)
    maxVehicle(vehicle)
    vehicle.numberPlateText = player.name

def playerLeaveVehicle(player, vehicle, seat):
    alt.log("Player {0} left vehicle {1}".format(player.name, vehicle.id))
    vehicle.customPrimaryColor = alt.RGBA(0, 0, 0, 255)
    vehicle.numberPlateText = vehicle.getMeta("name")

alt.on("playerConnect", playerConnect)
alt.on("playerEnterVehicle", playerEnterVehicle)
alt.on("playerLeaveVehicle", playerLeaveVehicle)
