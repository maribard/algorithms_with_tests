class DictM:
    def __init__(self):
        self.key_list = []
        self.value_list = []

    def get_item(self, key):
        if key in self.key_list:
            key_index = self.key_list.index(key)
            return self.value_list[key_index]

    def get_items(self):
        return list(zip(self.key_list, self.value_list))

    def add_item(self, key, value):
        if key not in self.key_list:
            self.key_list.append(key)
            self.value_list.append(value)
        else:
            key_index = self.key_list.index(key)
            self.value_list[key_index] = value

    def update_item(self, key, value):
        if key in self.key_list:
            key_index = self.key_list.index(key)
            self.value_list[key_index] = value
        else:
            print(f"There is no key {key}")

    def delete_item(self, key):
        if key in self.key_list:
            item_index = self.key_list.index(key)

            self.key_list.pop(item_index)
            self.value_list.pop(item_index)

    def get_keys(self):
        return self.key_list

    def get_values(self):
        return self.value_list

    def __str__(self):
        str_to_return = ""
        for item in range(len(self.key_list)):
            if type(self.key_list[item]) is str:
                item_key = f"'{self.key_list[item]}'"
            else:
                item_key = self.key_list[item]

            if type(self.value_list[item]) is str:
                item_value = f"'{self.value_list[item]}'"
            else:
                item_value = self.value_list[item]

            if item != len(self.key_list) - 1:
                str_to_return += f"{item_key}" + ": " + f"{item_value}" + ", "
            else:
                str_to_return += f"{item_key}" + ": " + f"{item_value}"
        return "{" + str_to_return + "}"

    def __repr__(self):
        return f"Dict_M()(keys={self.key_list}, values={self.value_list})"












