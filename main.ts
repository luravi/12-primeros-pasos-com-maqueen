// Mover hacia adelante a velocidad máxima
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
// Espera 1 segundo
basic.pause(1000)
// Detener los motores
maqueen.motorStop(maqueen.Motors.All)
// Espera medio segundo
basic.pause(500)
// Mover hacia atrás a velocidad máxima
maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 255)
// Espera 1 segundo
basic.pause(1000)
// Detener los motores
maqueen.motorStop(maqueen.Motors.All)
