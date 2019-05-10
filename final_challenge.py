# Note: Heavily collaborated with github.com/nsafai
# We will be using Binarytrees to store parsed routing numbers
from binarytree import BinaryTreeNode, BinarySearchTree


class CallRouter(object):
    def __init__(self, phone_numbers_unparsed, route_numbers_unparsed):
        self.phone_numbers_parsed = self.parse_phone_numbers(
            phone_numbers_unparsed)
        self.route_numbers_parsed = self.parse_route_numbers(
            route_numbers_unparsed)

        # Data Structure: Binary Search Tree of Prefixes (quick search)
        self.prefixes = BinarySearchTree()
        # Data Structure: Dictionary of prefixes and best prices (quick price fetching and price updating)
        self.best_prices = {}

    # Step 1: Turn import files into useable python objects
    def parse_phone_numbers(self, phone_numbers_unparsed):
        pass

    def parse_route_numbers(self, route_numbers_unparsed):
        # Take each line in raw data, deconstruct
        for entry in route_numbers_unparsed:
            clean_route = entry(',')
            prefix = clean_route[0]
            price = clean_route[1]
        # If not in prefix binary tree, add to binary tree and add to dictionary
            if self.prefixes.contains(prefix) == False:
                self.prefixes.insert(prefix)
                self.best_prices[prefix] = price
        # If already in prefix binary tree, update compare and update dictionary
            else:
                # If stored price is larger than new price
                if self.best_prices[prefix] > price:
                    self.best_prices[prefix] = price

    # Step 2: Find the longest matching prefix (using recursion)
    def routing_cost(self, phone_number):
        # Find the longest prefix that matches phone number
        # Note: We are always storing best prices in the parse route numbers method
        if phone_number is not None:
            if self.prefixes.contains(phone_number):
                return self.best_prices[phone_number]
            else:
                index_to_slice = len(phone_number) - 1
                return self.routing_cost(phone_number[:index_to_slice])
        else:
            return 0

    # Step 3: Record best routing costs results into a readable format
    def record_routing_costs(self, phone_numbers_parsed):
        results = []
        for phone_number in phone_numbers_parsed:
            cost = self.routing_cost(phone_number)
            line_item = "{},{}".format(phone_number, cost)
            results.append(line_item)
        print(results)
