object Flags {
  def main(args: Array[String]): Unit = {
    //val A = Array[Int](1,5,3,4,3,4,1,2,3,4,6,2)
    val A = Array[Int](0,1,0,0,0,1,0,0,0,1,0,0,0,1,0)
    println(solution(A))
  }

  def solution(a: Array[Int]): Int = {
    val peaks = find_peaks(a)
    if(peaks.length == 0) return 0
    if(peaks.length == 1) return 1

    val a_length = a.length
    val max_possible_flags = peaks.length min Math.sqrt(a_length).toInt + 1
    var max_flag_count = 0

    for(i <- 2 to max_possible_flags){
      val step = i
      var peak_point = 0 // 第一個peak
      var point = peaks(peak_point) // 從第一個peak開始
      var flag_count = 1 // 一定可以插第一個peak

      //println("======Start======")
      //println("step: " + step)
      //println("point: " + point)
      //println("flag count: " + flag_count)

      while(point < a_length && flag_count < step){

        point += step
        peak_point += 1
        while(peak_point < peaks.length && peaks(peak_point) < point){
          peak_point += 1
        }
        if(peak_point < peaks.length && flag_count < step){
          flag_count += 1
          point = peaks(peak_point)
          //println("point: " + point)
          //println("flag count: " + flag_count)
        }
      }

      max_flag_count = max_flag_count max flag_count
    }

    return max_flag_count
  }

  def find_peaks(a: Array[Int]) = {
    for{
      i <- Range(1, a.length-1)
      if (a(i) > a(i+1) && a(i) > a(i-1))
    } yield i
  }

}
