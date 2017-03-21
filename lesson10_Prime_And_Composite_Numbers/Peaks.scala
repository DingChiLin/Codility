object Test extends App{

  val A = Array[Int](1,2,3,4,3,4,1,2,3,4,6,2)
  //val A = Array[Int](0,1,0,1,0,0,0,0,1,0,1,0)
  println(solution(A))

  def peak(a: Array[Int]) = {
    for{
      i <- Range(1, a.length-1)
      if a(i) > a(i-1) && a(i) > a(i+1)
    } yield i
  }

  def divisors(n: Int) = {
    for{
      i <- Range(1, n)
      if n % i == 0
    } yield i
  }

  def solution(a: Array[Int]): Int = {
    val peaks = peak(a) // O(n)
    if(peaks.length == 0) return 0
    if(peaks.length == 1) return 1

    val peak_length = peaks.length

    val a_length = a.length
    val ds = divisors(a_length) // O(n)
    if(ds.length == 0) return 1

    var max_d_point = 0
    for(d_point <- Range(0, ds.length)){ // O(n)
      val d = ds(d_point)
      val step = a_length/d
      var a_point = -1
      var peak_point = 0
      var valid = true
      for(i <- Range(0,d)){ // O(log(log(N)))
        a_point += step
        var empty = true
        while(peak_point < peak_length && peaks(peak_point) <= a_point){
          empty = false
          peak_point += 1
        }
        if(empty) valid = false
      }
      if(valid) max_d_point = max_d_point max d_point
    }
    return ds(max_d_point)
  }
}
