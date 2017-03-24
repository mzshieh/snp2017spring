## Lecture 4: Stories and Game

## Stories

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
            +   Keyboard might be a flawed game controller. 
        +   [Broadcast](https://scratch.mit.edu/projects/116183365): Define your own event!
+   Task:
    +   Modify [this project](https://scratch.mit.edu/projects/115947152/) to make Scratch Cat jumping in Mario's style
        +   [Reference](https://wiki.scratch.mit.edu/wiki/When_()_Key_Pressed_(block))
    +   Bonus: Rockman X's style
        +   Able to dash
        +   Jump once more

### Game

+   [Maze](https://scratch.mit.edu/projects/11414041/)
+   [Pong](https://scratch.mit.edu/projects/10128515/)
+   [Scrolling](https://scratch.mit.edu/projects/22162012/)
+   [Fish Chomp](https://scratch.mit.edu/projects/10859244/)
    +   Task: Display the score
    +   Clone
        +   10 small fish
        +   Task: 5 small fish in different color
            +   Hint: Use color effect
            +   You may only use one sprite for small fish
+   Puzzles 請準備幾個角色
    +   P1: 當你按下 B 時，角色變大一點。當你按下 S 時，角色變小一點。
    +   P2: 當角色透過網路攝影機看到的畫面變化很大時，換個顏色。
    +   P3: 當角色移動到畫面上方 25% 的區域，會說他喜歡上面。
    +   P4: 當角色碰到藍色時，發出一個高音。當角色碰到紅色時，發出一個低音。
    +   P5: 當角色碰到另外一個角色時，其中一個說「不好意思」。
    +   P6: 當貓角色靠近狗角色時，狗跑離貓。
    +   P7: 當滑鼠點擊一下時，在那邊畫朵花。
    +   P8: 當你點擊一個角色時，其他的角色就跳舞。
    +   P9: 當你移動滑鼠時，角色追著滑鼠跑，但不可以碰到滑鼠。
+   [Debug It!](https://scratch.mit.edu/studios/475634/)
    +   [Debug 4.1](https://scratch.mit.edu/projects/24271192/): Scratch Cat 只能撿起筆記型電腦到 Inventory ，請修改程式讓他可以撿起其他東西。
    +   [Debug 4.2](https://scratch.mit.edu/projects/24271303/): 請改到讓 Scratch Cat 碰到黃色 Gobo 時加 10 分，碰到粉紅 Gobo 時減 10 分。
    +   [Debug 4.3](https://scratch.mit.edu/projects/24271446/): 請修好這個猜數字遊戲，讓 Scratch Cat 不要在那邊胡說八道。
    +   [Debug 4.4](https://scratch.mit.edu/projects/24271475/): 請讓球打到 Scratch Cat 一次時，# of hits 只增加 1。
        +   額外要求：讓畫面上有 10 顆球在飛。
        +   Hint: Clone, 分身。
    +   [Debug 4.5](https://scratch.mit.edu/projects/24271560/): 請修改成不會穿過綠色怪物的版本。

### Modularization and Recursion - Bonus Topic

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
