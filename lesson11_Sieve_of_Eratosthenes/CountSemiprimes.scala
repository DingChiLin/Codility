object CountSemiprimes extends App{
  println("HELLO")

  val p = Array(1,4,16)
  val q = Array(26,10,20)
  val n = 26
  //val p = Array(1)
  //val q = Array(1)
  //val n = 1
  val s = solution(n, p, q)
  println(s.toList)

  def solution(n:Int, p: Array[Int], q:Array[Int]): Array[Int] = {
    val semiPrimesPreSum = semiPrimesList(n)
    val l = p.length
    val r = (0 until l).toArray
    for(i <- (0 until l)){
      val p_val = p(i)
      val q_val = q(i)
      r(i) = countSemiPrimes(p_val, q_val, semiPrimesPreSum)
    }

    return r
  }

  def countSemiPrimes(p_val: Int, q_val:Int, semiPrimesPreSum:Array[Int]): Int = {
    return semiPrimesPreSum(q_val) - semiPrimesPreSum(p_val-1)
  }

  def semiPrimesList(x: Int): Array[Int] = {
    val result = Array.fill[Int](x+1)(0)
    var index = 2
    while(index * index <= x){
      if(result(index) == 0){
        var k = index * index
        while(k <= x){
          if(result(k) == 0){
            result(k) = index
          }
          k += index
        }
      }
      index += 1
    }

    val semiPrimesPreSum = Array.fill[Int](x+1)(0)
    var count = 0
    for(k <- (0 to x)){
      if(result(k) != 0){
        if(k % result(k) == 0){
          val p = k / result(k)
          if(result(p) == 0){
            count += 1
          }
        }
      }
      semiPrimesPreSum(k) = count
    }
    
    return semiPrimesPreSum
  }


}

