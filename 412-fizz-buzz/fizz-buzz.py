class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1,n+1):
            if not i%3 and not i%5:
                arr.append("FizzBuzz")
            elif not i%3:
                arr.append("Fizz")
            elif not i%5:
                arr.append("Buzz")
            else:
                arr.append(f"{i}")
        return arr