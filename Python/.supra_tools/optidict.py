class optidict:
    def __init__(self, *args):
        self.reset()
        if args: self.multi_add(args)

    def add(self, key, value):
        val = self.exist(key)
        if not val:
            self.root = node(key, value, self.root)
            self.len += 1
        else:
            val.value = value

    def multi_add(self, items):
        for item in items: self.add(item[0], item[1])

    def remove(self, item):  # je suis mauvais mdr
        if not self.empty():
            previous = self.root
            current = previous.next
            if previous.key == item:
                self.root = current
                self.len -= 1
            else:
                for _ in range(self.len - 1):
                    if current.key == item:
                        previous.next = current.next
                        self.len -= 1
                        break
                    previous = previous.next
                    current = current.next
                else:
                    raise

    def exist(self, val):
        if self.empty(): return False
        current = self.root
        for _ in range(self.len):
            if current.key == val: return current
            current = current.next
        return False

    def empty(self):
        if self.root is None: return True
        return False

    def reset(self):
        self.root = None
        self.len = 0

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, item):
        if not self.empty():
            current = self.root
            for _ in range(self.len):
                if current.key == item: return current.value
                current = current.next
        raise ValueError(f"The key [{item}] doesn't exist")

    def __str__(self):
        if not self.empty():
            __str = "{"
            current = self.root
            for _ in range(self.len):
                __str += f"{current},"
                current = current.next
            return __str[:-1]+"}"
        return "Empty"

    def __len__(self):
        return self.len

class node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.key}: {self.value}"
