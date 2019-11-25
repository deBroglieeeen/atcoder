import Foundation
let s = readLine()!.componentsSeparatedByString(" ")
let xs = s.map{Int($0)!}
let w = xs[0]
let h = xs[1]

if w % 4 == 0 && h % 3 == 0{
  print("4:3")
}else if w % 16 == 0 && h % 9 == 0{
  print("16:9")
}