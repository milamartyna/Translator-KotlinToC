fun complex_add(a: Int): Int {
    var c: Int = 5
    var d: Int = 10
    while ((a <= 15) && (c > d)) {
        c--
        a++
    }
    return a + d
}

fun run(argCount: Int, args: String): Int {
    var a: Int = 8
    var b: Int = 9
    while (a <= b) {
        print('Aloha')
        a++
    }
    if (argCount > 1) {
        return 1
    }
     else{
        return complex_add(a)
    }
}

fun main(argCount: Int, args: String): Int {
    run(2, 'stringArg')
    return 0
}

