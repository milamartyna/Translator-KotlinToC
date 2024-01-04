fun stuff(a: Int, b: Int): Int {
    var c: Int = 5
    var d: Int = 10
    print('Hello World', a)
    while ((a <= b) || (c > d)) {
        d--
        a++
    }
    return add(a, b)
}

fun main(argCount: Int, args: String): Int {
    var a: Int = 5
    var b: Int = 10
    while (a <= b) {
        print('Aloha')
        a++
    }
    if (argCount > 1) {
        return 1
    }
     else{
        return a
    }
}
