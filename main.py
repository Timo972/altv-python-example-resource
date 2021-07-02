import alt

alt.log("Hello World!")

def maxVehicle(vehicle):
    modTypes = 48

def playerConnect(player):
    player.model = "mp_m_freemode_01"
    player.spawn(5, 5, 76, 0)
    veh = alt.Vehicle("krieger", 5, 5, 76, 0, 0, 0)
    alt.log("Created vehicle")
    print(veh)
    alt.log("Vehicle ID: {}".format(veh.id))

def playerEnterVehicle(player, vehicle, seat):
    alt.log("Player {0} entered vehicle {1}".format(player.name, vehicle.model))
    vehicle.customPrimaryColor = alt.RGBA(243, 255, 0, 255)

def playerLeftVehicle(player, vehicle, seat):
    alt.log("Player {0} left vehicle {1}".format(player.name, vehicle.model))
    vehicle.customPrimaryColor = alt.RGBA(0, 0, 0, 255)

alt.on("playerConnect", playerConnect)
alt.on("playerEnterVehicle", playerEnterVehicle)
alt.on("playerLeftVehicle", playerLeftVehicle)
