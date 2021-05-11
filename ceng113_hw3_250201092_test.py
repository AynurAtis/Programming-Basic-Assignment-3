# 250201092

import ceng113_hw3_250201092_menu as hw3menu
import ceng113_hw3_250201092 as hw3


hw3menu.menu()
hw3.add_user("Jack")
hw3.add_user("Alice")
hw3.add_user("Bob")
hw3.add_friend("Bob", "Alice")
hw3.add_friend("Bob", "Jack")
hw3.add_user("Sam")
hw3.add_friend("Alice", "Sam")
hw3.add_user("Leo")
hw3.add_friend("Sam", "Leo")
hw3.offer_friend("Bob")
hw3.add_friend("Leo", "Bob")
hw3.add_user("Toby")
hw3.add_friend("Jack", "Toby")
hw3.offer_friend("Leo")
hw3.delete_user("Alice")
hw3.offer_friend("Leo")
hw3.remove_friend("Leo", "Sam")

