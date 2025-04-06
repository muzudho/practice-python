# 📖 [Python イテレータで遅延評価を実装する方法](https://labex.io/ja/tutorials/python-how-to-implement-lazy-evaluation-in-a-python-iterator-397687)

class LazySequence:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            result = self.current_value
            self.current_value += 1
            return result
        else:
            raise StopIteration()

lazy_seq = LazySequence(5)
for num in lazy_seq:
    print(num)  ## Output: 0 1 2 3 4