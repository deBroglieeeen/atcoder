import Foundation

let s = readLine()!.componentsSeparatedByString(" ")
let xs = s.map { Int($0)!}

let a = xs[0]
let b = xs[1]

if b % a == 0{
  print(b/a)
}
else{
  print(b/a+1)
}