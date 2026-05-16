# The 100 Series: TouchDesigner Fundamentals

- consolidate first attempt at org.
    
    Error: when logging into derivative forums (trying to use my td learn/ Curriculum log in info)
    
    `Derivative accounts do not work, please login with your Curriculum account`, 
    
    - ~~derivative~~ curriculum account for learning tutorials and logging progress: `@hermaarsha`
        
        misspelling oof
        
        Hermaarsha
        
        ![image.png](The%20100%20Series%20TouchDesigner%20Fundamentals/image.png)
        
    - derivative account: td + forum //   `@make.da`
    
    curriculum navigator: a living breathing (.toe) note where all the course examples and link to docs would be stored
    
    https://learn.derivative.ca/learning-resources/curriculum-navigator/
    
    ### setting up curr nav. on my mac
    
    - curriculum navigator path:
        
        touchdesigner folder (td)
        
        /Users/kidist/td 
        
        https://macpaw.com/how-to/copy-file-path-mac?clickid=1QeT%3Av10HxyKTEvV6IViSVk4UksTLHRh22tQWA0&iradid=66209&irpid=2447408&utm_content=ONLINE_TRACKING_LINK&utm_campaign=FatCoupon%20Technology%20Ltd&sharedid=6834d1921f5e7a0012a8c36d&utm_medium=affiliate&mpaid=3&utm_source=impactradius
        
        to get path: right click + opt
        
        - right click /  or ctrl+click
        - hold down opt
        - “copy as path”
        
        downloaded curruculum nav
        
        /Users/kidist/Downloads/td-navigator.toe
        
        move it to td folder (done)
        
        new path:
        
    
    /Users/kidist/td/td-navigator.toe
    
    opened td-navigator.toe
    
    - error window pic:
        
        ![image.png](The%20100%20Series%20TouchDesigner%20Fundamentals/image%201.png)
        
    - debug steps:
        
        search “project1” in spotlight search > scroll down to “search in finder”
        
        - pic
            
            ![image.png](The%20100%20Series%20TouchDesigner%20Fundamentals/image%202.png)
            
        
        ..
        
        notice path 
        
        ![image.png](The%20100%20Series%20TouchDesigner%20Fundamentals/image%203.png)
        
        create a project named `td-navigator` this is a folder
        
        file> create project folder
        
        notice how inside td/ 
        
        /  📁 td-navigator.  
        
        (organizes the toe file i dl’d into a project format, similar to logic projects (remember form intro to electronic music making, prof recommended  to save logic assignments/songs as projects in file format…)
        
        /  🗒️ td-navigator.toe. 
        
        (thing i downloaded)
        
        ![image.png](The%20100%20Series%20TouchDesigner%20Fundamentals/image%204.png)
        
        ![now we have the `td-navigator.toe` as a project folder and as a file . notice how `users/kidist/td/td-navigator/td-navigator.toe` is 5KB and `users/kidist/td/td-navigator.toe` is 198 KB](The%20100%20Series%20TouchDesigner%20Fundamentals/image%205.png)
        
        now we have the `td-navigator.toe` as a project folder and as a file . notice how `users/kidist/td/td-navigator/td-navigator.toe` is 5KB and `users/kidist/td/td-navigator.toe` is 198 KB
        
        - `users/kidist/td/td-navigator/td-navigator.toe`
            - in the project view, all the assets and stuff are saved in the folder and the td-navigator.toe file just links all the references to em, so it’s just 5KB
        - `users/kidist/td/td-navigator.toe`
            - the whole td file i downloaded, isn’t saved as a project, so all assets and stuff are saved in the .toe file itself
        
        why are touchdesigner networks staved as a .toe file?
        
        **.toe** 
        
        **to**uchdesigner **e**nvironment file
        
        noticing that this is an issue with the `Project` class in TD
        
        https://docs.derivative.ca/Project_Class
        
        opening texport
        
        : Dialogs > Texport and DATs
        
        run `>>print(project.pythonStack())` 
        
        note: (print(project.stack()) yielded nothing, probably because i haven’t done anything w the project yet, so it’s stack was empty
        
        ![output after running `>>print(project.pythonStack())` in the Textport](The%20100%20Series%20TouchDesigner%20Fundamentals/image%206.png)
        
        output after running `>>print(project.pythonStack())` in the Textport
        
        print current work directory (cwd) of this project (td-navigator)
        
        ![notice how the cwd is the filepath for the project](The%20100%20Series%20TouchDesigner%20Fundamentals/image%207.png)
        
        notice how the cwd is the filepath for the project
        
    
    - what are these errors about?
        
        
        project1 errors
        
        other errors
        
        view errors
        
        dialogs> Errors 
        
        make sure to click “Log Errors” + then “Refresh Errors” to show all of the errors
        
        i think the default behaviors of the Errors dialogue window is to start logging new errors since it’s (Errors window)  opening, so we have to click that “Log Errors” button to get all the errors
        
        ![image.png](The%20100%20Series%20TouchDesigner%20Fundamentals/image%208.png)
        
        okay let’s learn how to troubleshoot in td
        
        Error DAT 
        
        https://docs.derivative.ca/ErrorDAT_Class
        
    
    ---
    
    -pickupwhereweleftoff-
    
    https://derivative.ca/UserGuide/Troubleshooting_in_TouchDesigner
    
    - [ ]  read thru troubleshooting ^
- other notes
    
    [101: Navigating the Environment (NTE)](The%20100%20Series%20TouchDesigner%20Fundamentals/101%20Navigating%20the%20Environment%20(NTE)%201ffa70bb517c80fe8ce8fa07069ba747.md)
    
    [101](The%20100%20Series%20TouchDesigner%20Fundamentals/101%201ffa70bb517c800fa6d7ce1346d96151.md)
    

[taw: td | day: 29/84 | week: 05/12](taw%20td%20day%2029%2084%20week%2005%2012%201ffa70bb517c80168a1dcfd7b7b0627e.md)

[TAWWB: TD](https://www.notion.so/TAWWB-TD-1ffa70bb517c8029a262cb07f2ee8fcc?pvs=21)

[Untitled](The%20100%20Series%20TouchDesigner%20Fundamentals/Untitled%20203a70bb517c80a783bce766054a00d3.csv)

view ref