# Mover hacia adelante a velocidad máxima
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
# Espera 1 segundo
basic.pause(1000)
# Detener los motores
maqueen.motor_stop(maqueen.Motors.ALL)
# Espera medio segundo
basic.pause(500)
# Mover hacia atrás a velocidad máxima
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 255)
# Espera 1 segundo
basic.pause(1000)
# Detener los motores
maqueen.motor_stop(maqueen.Motors.ALL)