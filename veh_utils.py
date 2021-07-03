import alt

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