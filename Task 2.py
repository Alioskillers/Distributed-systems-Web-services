#importing mrjob library that is used for map reduce to process (Big Data)
from mrjob.job import MRJob as mj

#defining a map reduce class using mrjob
class AvgGradePerUniversity(mj):

    # defining the mapper function to process each line in the files
    def mapper(self, _,line):
        # split the line into 2 components seperated by a comma that are desired in the output(grade, university)
        _, _, grade, university= line.split(',')
        #return university and grade
        yield university, int(grade)

    # defining a reducer function to calculate the average
    def reducer(self, university, grades):
        # converting the output into a list for calculating the average
        grade_list = list(grades)
        # return the sum divided by the count
        yield university, sum(grade_list) / len(grade_list)

#running the main method for mrjob
if __name__ == '__main__':
    AvgGradePerUniversity.run()