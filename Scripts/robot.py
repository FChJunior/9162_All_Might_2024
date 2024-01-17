#---------------- Smash FRC 2024 - CRECENDO -----------------#
# Equipe: 9162 All Migth
# Robô: Smash
# Programadores: Niord e João Antônio
# Mentor: Chagas Junior

import wpilib 


class Smash (wpilib.TimedRobot):

    def robotInit(self) -> None:
        self.joy = wpilib.XboxController(0)

    def teleopPeriodic(self) -> None:
        if self.joy.getAButton():
            self.logger.info("pressionado")