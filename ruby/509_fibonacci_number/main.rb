# @param {Integer} n
# @return {Integer}
def fib(n)
  if n == 0 || n == 1
    return n
  end

  previous = 0
  current = 1

  i = 2

  while i <= n
    tmp = previous + current
    previous = current
    current = tmp
    i += 1
  end
  current
end

puts fib(2)
puts fib(3)
puts fib(4)
puts fib(5)
