class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def put(self, key: int, value: int) -> None:
        bucket_index = key % 10

        for index, pair in enumerate(self.buckets[bucket_index]):
            stored_key, stored_value = pair

            if stored_key == key:
                self.buckets[bucket_index][index] = (key, value)
                return

        self.buckets[bucket_index].append((key, value))

    def get(self, key: int) -> int:
        bucket_index = key % 10

        for stored_key, stored_value in self.buckets[bucket_index]:
            if stored_key == key:
                return stored_value

        return -1

    def remove(self, key: int) -> None:
        bucket_index = key % 10

        for stored_key, stored_value in self.buckets[bucket_index]:
            if stored_key == key:
                self.buckets[bucket_index].remove((stored_key, stored_value))
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)