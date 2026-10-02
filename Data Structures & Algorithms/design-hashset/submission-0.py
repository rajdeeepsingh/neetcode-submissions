class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        bucket_index = key % 10

        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)
    
    def remove(self, key: int) -> None:
        bucket_index = key % 10

        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = key % 10

        if key in self.buckets[bucket_index]:
            return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)