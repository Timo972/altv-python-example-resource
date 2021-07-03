import alt
import veh_utils
import sys

alt.log("Hello World!")

DEFAULT_VEH_NAME = "krieger"

alt.log(sys.path)

def playerConnect(player):
    player.model = "mp_m_freemode_01"
    player.spawn(5, 5, 76, 0)
    veh = alt.Vehicle(DEFAULT_VEH_NAME, 5, 5, 76, 0, 0, 0)
    veh.setMeta("name", DEFAULT_VEH_NAME)
    alt.log("Created vehicle")
    alt.log("Vehicle ID: {}".format(veh.id))

    player.giveWeapon("weapon_rpg", 999, True)

def playerEnterVehicle(player, vehicle, seat):
    alt.log("Player {0} entered vehicle {1}".format(player.name, vehicle.id))
    vehicle.customPrimaryColor = alt.RGBA(243, 255, 0, 255)
    veh_utils.maxVehicle(vehicle)
    vehicle.numberPlateText = player.name
    alt.log("Vehicle driver: {}".format(vehicle.driver.name))

def playerLeaveVehicle(player, vehicle, seat):
    alt.log("Player {0} left vehicle {1}".format(player.name, vehicle.id))
    vehicle.customPrimaryColor = alt.RGBA(0, 0, 0, 255)
    vehicle.numberPlateText = vehicle.getMeta("name")

def explosion(source, expType, pos, fx, target):
    alt.log("Explosion of type {0} caused by player {1} at position {2}".format(expType, source, pos))

alt.on("playerConnect", playerConnect)
alt.on("playerEnterVehicle", playerEnterVehicle)
alt.on("playerLeaveVehicle", playerLeaveVehicle)
alt.on("explosion", explosion)