#----------------- Smash FRC 2024 - CRECENDO ------------------#
# Equipe: 9162 All Migth
# Robô: Smash
# Programadores: Niord e João Antônio
# Mentor: Chagas Junior
# 
# ----------------------- Descrição: ------------------------- #
# Essa é a classe principal onde chamará todas as ouutras classe
# e criar os objetos de funcionalidades de cada subsitema que 
# trabalharemos no SMASH para a temporada 2024 CRECENDO.
# 


# ------------------- Bibliotecas e Classes ------------------- #
# --> wpilib: Biblioteca principal da competição. Nele encontraremos
# todos os metódos e classes que serão fundamental para o funcionamento
# do robô.
#

import wpilib as wp


class Smash (wp.TimedRobot):
    def robotInit(self) -> None:
        pass
    
    def robotPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        pass


if Smash == "_main_":
    wp.run(Smash)