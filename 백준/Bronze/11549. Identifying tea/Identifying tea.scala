import scala.io.StdIn.readLine

object Main {
    def main(args: Array[String]): Unit = {
        val n = readLine().toInt
        val answer = readLine() split " "
        var cnt = 0
        for ans <- answer do
            if ans.toInt == n then 
                cnt += 1
        println(cnt)
    }
}