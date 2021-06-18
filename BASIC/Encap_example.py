#This is Basic Encapsulation example from Platzi trainning courses
class VotingBox:

    def __init__(self, personal_id, country):
        self.__personal_id = personal_id
        self.__country = country
        self.__region = None

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        if region in self.__country:
            self.__region = region
        else:
            raise ValueError(f'Region {region} is not valid inside {self.__country}')

#we create an object and the region should be inside this array to be valid
votingBox =  VotingBox(270118, ['Ciudad de Mexico', 'Jalisco'])

#answer should be None
print(votingBox.region)

votingBox.region = 'Ciudad de Mexico'
#answer should be valid
print(votingBox.region)

votingBox.region = 'Oxxo'
#this should raise the exception
print(votingBox.region)
