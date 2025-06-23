#importing mrjob library that is used for map reduce to process (Big Data)
from mrjob.job import MRJob as mj

#defining a map reduce class using mrjob
class Top3GradesPerYear(mj):

# defining the mapper function to process each line in the files
    def mapper(self, _,line):
        # split the line into 2 components seperated by a comma that are desired in the output(year, grade)
        year, _, grade, _= line.split(',')
        # return year and grade
        yield year, int(grade)

# defining a reducer function to get the top grades for each year
    def reducer(self, year, grades):
        #sorting the grades and choosing the top 3 values
        top_grades=sorted(grades, reverse=True)[:3]
        #return year and top grades as a tuple
        yield year, top_grades

#running the main method for mrjob
if __name__ == '__main__':
    Top3GradesPerYear.run()