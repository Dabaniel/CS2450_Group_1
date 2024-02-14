User Stories

1. As a student using UVSim, I want to be able to test my understanding of BasicML and the basic opertaions.
2. As an instructor for the BasicML class, I want to have basic opertations such as read, write, store, and load usable for my students.
3. As an instructor for the BasicML class, I need UVSim to replicate the instruction opertaions and memory for BasicML 

Use Cases

1. Read Function
-Map to specific instruction 10
-Read word from keyboard into specified memory location

2. Write Function
-Map to specific instruction 11
-Take value from specified memory location and print to screen

3. Load Function
-Map to specific instruction 20
-Take value from specified location in memory and put into accumulator

3. Load Function
-Map to specific instruction 21
-Take value from accumulator into specified location in memory

Functional Requirements
-Input from console
-Validate Input
-Perform operation based on specified word

Non-Functional Requirements
-Allow for however many inputs a student needs
-Perform operations with little to to no delay
-Able to run on low performance machines

Development Plan

Objective: 
-Develop the foundational components of the UVSim, ensuring accuracy in mathematical operations and memory management.

Key Actions:
-Implement the accumulator logic to handle pre-calculation data storage and manipulation.
-Develop the memory module with support for 100-word storage, ensuring correct handling of signed four-digit decimal numbers.
-Implement the CPU module capable of decoding and executing BasicML instructions.
-Create a loader mechanism for inputting BasicML programs into main memory starting at location 00.

Testing and Validation:
-Conduct thorough testing to ensure the UVSim and BasicML programs operate as intended across a variety of test cases.
-Develop unit tests for individual components (CPU, memory, accumulator).
-Create integration tests to verify the system works as a whole.
-Design and run BasicML program test cases to validate the instruction set and execution flow.
-Implement a debugging and logging framework to identify and fix issues.

Documentation and Training:
-Provide comprehensive documentation and training materials for users of the UVSim.
-Document the system architecture, module interfaces, and interaction flows.
-Create detailed documentation for the BasicML instruction set and programming guidelines.
-Develop user guides for loading and running BasicML programs on the UVSim.
-Organize meetings for developers or users.

