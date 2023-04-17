basic.showIcon(IconNames.Happy)
basic.showString("KOMPAS")
basic.forever(function () {
    if (input.compassHeading() > 357 || input.compassHeading() < 3) {
        basic.showString("N")
    } else if (input.compassHeading() > 87 && input.compassHeading() < 93) {
        basic.showString("E")
    } else if (input.compassHeading() > 177 && input.compassHeading() < 183) {
        basic.showString("S")
    } else if (input.compassHeading() > 267 && input.compassHeading() < 273) {
        basic.showString("S")
    } else {
        basic.clearScreen()
    }
})
