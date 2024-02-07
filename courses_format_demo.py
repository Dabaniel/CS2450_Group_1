#This file is a stand-in for a better course-management system
#TODO: indicates what still needs to be implemented
#JSON would likely be the best way to organize all this data

#SUBJECTS - courses (i.e. CS, MATH, etc.)
#COURSES  - course numbers (i.e. 1030, 1400, etc.)
#COURSE   - credits, int: credit hours (i.e. 3, 5, etc.)
#         - pre, tuple: prerequisites (i.e. ('CS', '1030', 0), ('CS', '1400', 0), ('ACT', 23), etc.)
#               LAYOUTS
#           ('subject', 'course', 'letter grade')   "have you taken this course ('' letter grade is pass)"
#           ('test', 'minimum score')                "INCLUSIVE: test with at least [score]"
#           ('subject', 'course')                    "NON INCLUSIVE: have you taken above this course?"
#               OPERATIONS
#           'not'
#           'and'
#           'or'
#               FORMAT i.e. prefix maths :)
#           none = 'pre': ()
#           'A' = 'pre': ('A')
#           'A' and 'B' = 'pre': ('and', ('A'), ('B'))
#           ('A' or 'B') and 'C' = 'pre': ('and', 'or', ('A'), ('B'), ('C'))
#           ex. CS 1030 and (MAT 1010 or MAT 1015 with a B or higher)
#            -> 'pre': ('and', ('CS', '1030', ''), 'or', ('MAT', '1010', 'B'), ('MAT', '1015', 'B'))
#         - TODO: co, tuple: corequisites
#         - desc, string: description (i.e. "Introduces the basics of...", etc.)

CS = {
    '1030': {
        'credits': 3,
        'pre': (),
        'co': (),
        'desc': 'Introduces the basics of computing, including computer hardware, and programming concepts and language. Explores how computers work and how a computer may be programmed. Includes a brief history of computer, programming languages, and computer numbering systems. Presents basic programming constructs; students produce a variety of introductory level programs. Surveys various computing professions. May be delivered hybrid and/or online. Lab access fee of $45 computers applies.'
    },
    '1400': {
        'credits': 3,
        'pre': ('or', 'or', 'or', ('MAT', '1010', ''), ('MAT', '1015', 'B'), ('ACT', 23), ('ALEKS', 38)),
        'co': (),
        'desc': 'Introduces techniques and tools to formulate and solve problems where computer algorithms and programs are a core part of an effective, repeatable solution. Demonstrates algorithmic thinking using procedural programs composed of sequences of commands, functions, loops, conditionals, and basic data structures. May be delivered online. Lab access fee of $45 for computers applies.'
    },
    '1410': {
        'credits': 3,
        'pre': ('and', ('CS', '1400', ''), 'or', 'or', ('MATH', '1050', ''), ('MATH', '1055', 'C+'), 'or', 'and', ('MATH', '1050'), 'not', ('MATH', '1055', ''), ('MATH', '1055')),
        'co': (),
        'desc': 'Teaches proper program structure using the core concepts of object-oriented programming: classes, objects, encapsulation, inheritance and polymorphism. Presents problems of increasing size and complexity requiring OOP techniques, standard libraries and other appropriate language constructs. Presents methods to identify, define and implement solutions to naturally recursive problems. May be delivered online. Lab access fee of $45 for computers applies.'
    },
    '2250': {
        'credits': 3,
        'pre': ('CS', '1400', ''),
        'co': (),
        'desc': 'Covers practical Java programming in-depth, including abstract classes and interfaces, proper use of the packages Java.lang, Java.io, and Java.util, GUI design and implementation, and programming. Lab access fee of $45 for computers applies.'
    },
    '2300': {
        'credits': 3,
        'pre': ('and', 'or', ('CS', '1410', ''), ('INFO', '2200', ''), 'or', ('MATH', '1050', ''), ('MATH', '1050')),
        'co': (),
        'desc': 'Covers algebraic structures applied to computer programming. Includes logic, sets, elementary number theory, mathematical induction, recursion, algorithm complexity, combinatorics, relations, graphs, and trees. Lab access fee of $45 for computers applies.'
    },
    '2370': {
        'credits': 3,
        'pre': ('CS', '1400', ''),
        'co': (),
        'desc': 'Introduces C++ programming for students with prior programming experience. Covers language fundamentals, core standard library components, error handling, value semantics, pointers and memory management, object-oriented programming, and templates. Lab access fee of $45 for computers applies.'
    }
    # ,
    # '': {
    #     'credits': ,
    #     'pre': (),
    #     'co': (),
    #     'desc': ''
    # }
}

MATH = {

}

#main
SUBJECTS = {
    'CS': CS,
    'MATH': MATH
}

def get_course(subject, number):
    #Function which returns a dictionary with a course's information
    return SUBJECTS[subject][number]

def main():
    name = 'CS'
    num = '1400'
    print(get_course(name, num))

if __name__ == '__main__':
    main()