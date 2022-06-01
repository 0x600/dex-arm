from pydexarm import Dexarm
import time
dexarm = Dexarm("COM6") # Подключение к Windows

# скорость конвейера от 100 до 5000

dexarm.conveyor_belt_forward(5000) # конвейер вперед
dexarm.conveyor_belt_backward(5000) # конвейер назад
dexarm.conveyor_belt_forward(5000) # скорость в мм/секунду 
time.sleep(5) # время в секундах
dexarm.conveyor_belt_backward(5000) # скорость в мм/секунду 
time.sleep(5) # время в секундах
dexarm.conveyor_belt_stop() # остановить конвейер




