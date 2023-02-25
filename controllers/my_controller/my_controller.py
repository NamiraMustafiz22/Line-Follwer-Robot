"""line-follow-robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,DistanceSensor

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

timestep = 32
max_speed = 6.28

#motor
wheels = []
#              top_left, top_right, back_left, back_right
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

#IR sensor
ds = ['ds_right','ds_mid','ds_left']
pos = []
for i in range(3):
    pos.append(robot.getDevice(ds[i]))
    pos[i].enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    r = right_ir_val = pos[0].getValue()
    m = mid_ir_val = pos[1].getValue()
    l = left_ir_val = pos[2].getValue()
    print(f'Left: {left_ir_val} Mid: {mid_ir_val} Right: {right_ir_val}')
    left_speed = max_speed 
    right_speed = max_speed 
    
    # Process sensor data here.
    val = 700
    if l<val and r<val and m>=val:
         wheels[0].setVelocity(left_speed)
         wheels[1].setVelocity(right_speed)
         wheels[2].setVelocity(left_speed)
         wheels[3].setVelocity(right_speed)
    if l<val and r>=val and m>=val:
         wheels[0].setVelocity(left_speed)
         wheels[1].setVelocity(0) 
         wheels[2].setVelocity(left_speed)
         wheels[3].setVelocity(0)  
    if l>=val and r<val and m>=val:
         wheels[0].setVelocity(0)
         wheels[1].setVelocity(right_speed) 
         wheels[2].setVelocity(0)
         wheels[3].setVelocity(right_speed)   
    if l>=val and r<val and m<val:
         wheels[0].setVelocity(0)
         wheels[1].setVelocity(right_speed)
         wheels[2].setVelocity(0)
         wheels[3].setVelocity(right_speed)
    if l<val and r>=val and m<val:
         wheels[0].setVelocity(left_speed)
         wheels[1].setVelocity(0)
         wheels[2].setVelocity(left_speed)
         wheels[3].setVelocity(0)
    if l<val and r<val and m<val:
         wheels[0].setVelocity(left_speed)
         wheels[1].setVelocity(right_speed)
         wheels[2].setVelocity(left_speed)
         wheels[3].setVelocity(right_speed)
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
