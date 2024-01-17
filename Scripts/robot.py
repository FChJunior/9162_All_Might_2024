#----------------- Smash FRC 2024 - CRECENDO ------------------#
# Equipe: 9162 All Migth
# Robô: Smash 3.0
# Programadores: Niord e João Antônio
# Mentor: Chagas Junior
#--------------------------------------------------------------#

# ----------------------- Descrição: --------------------------#
# 
# -------------------------------------------------------------#


# ------------------------ Bibliotecas -------------------------#
# 
#---------------------------------------------------------------#

import wpilib as wp
import wpilib.drive as drive
import rev
import phoenix6.hardware as ph


#------------------- Classe de Funcionamento -------------------#
# 
#---------------------------------------------------------------#

class Smash (wp.TimedRobot):

# ------------------ Metodo Inicial do Robô --------------------#
    def robotInit(self) -> None:
        self.joystick    = wp.Joystick(0)
        self.control     = wp.XboxController(1)

        self.motorLeft1  = rev.CANSparkMax(1,rev.CANSparkMax.MotorType.kBrushed)
        self.motorLeft2  = rev.CANSparkMax(2,rev.CANSparkMax.MotorType.kBrushed)
        self.motorRight1 = rev.CANSparkMax(3,rev.CANSparkMax.MotorType.kBrushed)
        self.motorRight2 = rev.CANSparkMax(4,rev.CANSparkMax.MotorType.kBrushed)

        self.motorLeft   = wp.MotorControllerGroup(self.motorLeft1, self.motorLeft2)
        self.motorRight  = wp.MotorControllerGroup(self.motorRight1, self.motorRight2)

        self.driveTrain = drive.DifferentialDrive(self.motorLeft, self.motorRight)
# --------------------------------------------------------------#
        

    def driveTrainController(self):
        in_control = self.joystick.getRawAxis(1)

        speed = (((in_control - 1) * (1)) / -2) + 0
        xSpeed = self.joystick.getRawAxis(2) * speed
        zSpeed = self.joystick.getRawAxis(1) * speed

        self.driveTrain.arcadeDrive(xSpeed, zSpeed, False)


    def robotPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        self.driveTrainController()

    
if __name__ == "__main__":
    wp.run(Smash)