class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # x represents the number where sandwiches[x] & students[x] are equal
        # if they're the same value, remove all instances of x in students
        # this means that the student has recieved the sandwich that they liked
        # if there are students left over that didn't get a sandwich they liked, then we return the length(left over students) of the students
        # if the loop has executed successfully and all the students were satisfied, return 0 (no students that were dissatisfied)
        for x in sandwiches:
            if x in students:
                students.remove(x)
            else:
                return len(students)
        return 0