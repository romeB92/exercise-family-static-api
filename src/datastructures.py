
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [34,65,23,4,6]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age":35,
                "Lucky Numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age":5,
                "Lucky Numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        return self

    def delete_member(self, id):
        # fill this method and update the return
        for position, member in enumerate(self._members): 
            print("here is the member!",  position, member)
            if member["id"] == int(id): #
                outcast_member = self._members.pop(position)
                return outcast_member

    def get_member(self, id):
        # fill this method and update the return
        for person in self._members:
            if person["id"] == int(id): 
                print("self member", self._members)
                print("person",person)
                print("ID",int(id))
                print("person ID",person["id"])

                return person

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members