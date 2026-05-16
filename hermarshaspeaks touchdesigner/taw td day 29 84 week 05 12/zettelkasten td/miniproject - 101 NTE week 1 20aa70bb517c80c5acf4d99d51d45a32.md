# : miniproject - 101 NTE : week 1

tags: project, week1
Created time: June 5, 2025 7:43 PM
Status: In progress

Algorithmic Beauty of Plants 

https://algorithmicbotany.org/papers/abop/abop.pdf

### idea: implement interacive + generative koch curves with L-Systems + turtle graphics!

- notes from “Algorithmic Beauty of Plants: Chapter 1”
    
    
    ![pg 10](miniproject%20-%20101%20NTE%20week%201/image.png)
    
    pg 10
    
    and thus the project idea was solidified after reading 10 pages into ABOP (Algorithmic Beauty of Plants)
    
    from. 
    
    **pg 10, Chapter 1: Graphical Modeling Using L-systems**
    
    ![pg 8](miniproject%20-%20101%20NTE%20week%201/image%201.png)
    
    pg 8
    
    relevant terms:
    
    - L-System: Astrid Lindenmayer (1968) - Systems: a way to describe a fractal
        - OL-system: open (no context)
            - is O for organic or overload? couldn't find decisive answer on google…
        - IL-system: needs context
        - DOL-System: deterministic, no context needed L system
    - Koch Curve: Von Koch (1905)
        - snowflake curve
    
    - Initiator: starting shape
    - Generator: recursive replacement
    
    ![pg 2](miniproject%20-%20101%20NTE%20week%201/image%202.png)
    
    pg 2
    
    - Turtle: a generative graphic
        - `(x, y, $\delta)$`
            - `x, y` : position Cartesian coordinates
            - `$\delta$` : angle
    - Predecessor: initial starting string
    - Successor: string after a number of productions (transformations) have been applied
    - Grammar:
        - Chomsky’s Grammar: https://www.geeksforgeeks.org/chomsky-hierarchy-in-theory-of-computation/#
    - Axiom: starting string

### useful docs/ references

https://docs.derivative.ca/First_Things_to_Know_about_TouchDesigner

- saving a new project folder
    - searched in webpage for “project”
    
    > ctrl+F “project”
    > 
    > 
    > ### **12. Save your work**
    > 
    > Frequently save the state of your work. Under the File menu, choose [Create Project Folder](https://docs.derivative.ca/New_Project_Dialog). Make sure your Path is your Desktop. Change the Project Folder to `Learning`, then press Create.
    > 
    > Explorer or Finder will show you it created a folder on your desktop called `Learning` containing a bunch of folders for your media, plus two identical TouchDesigner Environment files called `Learning.1.toe` and `Learning.toe`.
    > 
    - https://docs.derivative.ca/New_Project_Dialog
- sss
- 

https://matthewragan.com/2017/12/03/touchdesigner-working-styles-git/

- 

http://forum.derivative.ca/t/saving-with-assets/11152/4

- 

https://forum.derivative.ca/t/i-keep-getting-this-error-message-error-float-argument-must-be-a-string-or-a-number-not-td-nullchop/254179/3?u=make.da

how to read from a chop → dat → get a float type