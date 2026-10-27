class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        rotations = 0

        while sandwiches and rotations < len(students):
            if sandwiches[0] != students[0]:
                students.append(students.pop(0))
                rotations += 1
            else:
                sandwiches.pop(0)
                students.pop(0)
                rotations = 0
        return len(students)
            

            