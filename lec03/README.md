## Lecture 3: More on Events

### Review
+   [Debug it!](https://scratch.mit.edu/studios/475539/)
    +   [Debug 2.1](https://scratch.mit.edu/projects/23266426/): 希望按下 Scratch Cat 後他會隨鼓聲跳舞，但他沒跳，該怎麼辦？
    +   [Debug 2.2](https://scratch.mit.edu/projects/24268476/): 希望 Nano 被碰到的時候也要說話，該怎麼辦？
    +   [Debug 2.3](https://scratch.mit.edu/projects/24268506/): 希望畫個笑臉，目前有一些地方多畫了，該怎麼辦？
    +   [Debug 2.4](https://scratch.mit.edu/projects/23267140/): 希望花開完了要停下來，該怎麼辦？
    +   [Debug 2.5](https://scratch.mit.edu/projects/23267245/): 希望生日快樂歌唱完才提示可以吹蠟燭了。

### Stories

+   [Characters](https://scratch.mit.edu/projects/115946864/)
    +   Implement small jumps, big jumps, and custom jumps
+   [Conversation](https://scratch.mit.edu/projects/10015800/)
    +   Modification: Use broadcast to trigger the conversation
+   [Scene](https://scratch.mit.edu/projects/115947152/)
    +   Press the left arrow to move to the left
    +   Press the right arrow to move to the right
    +   Press the space bar to jump
+   [Debug it!](https://scratch.mit.edu/studios/475554/)
    +   [Debug 3.1](https://scratch.mit.edu/projects/24269007/): Scratch Cat 教 Gobo 喵喵叫，可是輪到 Gobo 練習時，他沒有喵喵叫，該怎麼辦？
    +   [Debug 3.2](https://scratch.mit.edu/projects/24269046/): 想要設計成輸入一個數字讓 Scratch Cat 數，但他現在每次都是數到 10 ，該怎麼辦？ 
    +   [Debug 3.3](https://scratch.mit.edu/projects/24269070/): Scratch Cat 想要一個一個打電話給朋友，可是按下綠旗後就立刻結束了，該怎麼辦？
    +   [Debug 3.4](https://scratch.mit.edu/projects/24269097/): Scratch Cat 喊 Jump 的時候， Gobo 應該要跳動，但是沒有，該怎麼辦？
    +   [Debug 3.5](https://scratch.mit.edu/projects/24269131/): 恐龍應該只在禮堂跳舞，可是現在恐龍出現在所有場景，並且不會動，該怎麼辦？
+   Built-in event blocks do "more"
    +   [Example](https://scratch.mit.edu/projects/116182454/)
    +   Delay
    +   Block
    +   Cancel
    +   Alternative
        +   [Infinite Loop](https://scratch.mit.edu/projects/116182906/)
        +   [Broadcast](https://scratch.mit.edu/projects/116183365): Define your own event!
+   Task:
    +   Modify [this project](https://scratch.mit.edu/projects/115947152/) to make Scratch Cat jumping in Mario's style
        +   [Reference](https://wiki.scratch.mit.edu/wiki/When_()_Key_Pressed_(block))
    +   Bonus: Rockman X's style
        +   Able to dash
        +   Jump once more

### Modularization and Recursion

+   How to draw a tree?
+   Modularization
    +   Decompose the task into subtasks
        +   More readable
        +   Reusable
+   State
    +   Variable
    +   List
+   Precondition
+   Postcondition
    +   Effect
    +   Side Effect
+   Loop Invariants
+   Recursion
    +   A block contains itself
    +   Infinite loop and recursive calls without terminal condition
    +   Expansion
    +   Draw a tree recursively
+   Task
    +   Draw a snowflake
    +   Optional: [Draw a Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)