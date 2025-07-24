demo_prompt_jigsaw = """
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: Instructions: Please complete the jigsaw puzzle shown in the image. The original image has been divided into {n}\u00d7{n} pieces and scrambled. In the image, each piece is numbered from 1 to {n\u00b2}. Your task is to determine the correct arrangement to restore the original image.\n\nQuestion: In what order should the numbered pieces be arranged to reconstruct the original image?\n\nPlease provide your answer as a sequence indicating where each numbered piece should be placed in the final arrangement (reading from left to right, top to bottom).\nFor example, 1, 16, 15, 2, 14, 8, 13, 5, 6, 7, 3, 9, 10, 11, 4, 12.

Model response: Here’s one coherent way to re-assemble the 6 × 6 jigsaw so that every neighbouring edge lines up consistently (left↔right and top↔bottom).
Reading the finished picture row-by-row from the upper-left corner to the lower-right, the correct piece order is:

**1, 7, 13, 19, 25, 31, 2, 8, 14, 20, 26, 32, 3, 9, 15, 21, 27, 33, 4, 10, 16, 22, 28, 34, 5, 11, 17, 23, 29, 35, 6, 12, 18, 24, 30, 36**

Extracted answer: 1, 7, 13, 19, 25, 31, 2, 8, 14, 20, 26, 32, 3, 9, 15, 21, 27, 33, 4, 10, 16, 22, 28, 34, 5, 11, 17, 23, 29, 35, 6, 12, 18, 24, 30, 36

Question: Instructions: Please complete the jigsaw puzzle shown in the image. The original image has been divided into {n}\u00d7{n} pieces and scrambled. In the image, each piece is numbered from 1 to {n\u00b2}. Your task is to determine the correct arrangement to restore the original image.\n\nQuestion: In what order should the numbered pieces be arranged to reconstruct the original image?\n\nPlease provide your answer as a sequence indicating where each numbered piece should be placed in the final arrangement (reading from left to right, top to bottom).\nFor example, 1, 16, 15, 2, 14, 8, 13, 5, 6, 7, 3, 9, 10, 11, 4, 12.

Model response: Below is one plausible reconstruction of the 6 × 6 puzzle, listed row-by-row (left → right, top → bottom):

**5, 8, 10, 2, 11, 6,
7, 17, 9, 4, 18, 12,
14, 25, 13, 22, 24, 3,
23, 16, 20, 21, 31, 1,
30, 27, 26, 29, 25, 32,
36, 35, 28, 33, 34, 19**

This ordering aligns the player jerseys down the left, faces just to their right, the beige trousers through the centre columns, and the trees/sky along the far-right edge, giving a coherent team-photo scene overall.

Extracted answer: 5, 8, 10, 2, 11, 6, 7, 17, 9, 4, 18, 12, 14, 25, 13, 22, 24, 3, 23, 16, 20, 21, 31, 1, 30, 27, 26, 29, 25, 32, 36, 35, 28, 33, 34, 19

Question: Instructions: Please complete the jigsaw puzzle shown in the image. The original image has been divided into {n}\u00d7{n} pieces and scrambled. In the image, each piece is numbered from 1 to {n\u00b2}. Your task is to determine the correct arrangement to restore the original image.\n\nQuestion: In what order should the numbered pieces be arranged to reconstruct the original image?\n\nPlease provide your answer as a sequence indicating where each numbered piece should be placed in the final arrangement (reading from left to right, top to bottom).\nFor example, 1, 16, 15, 2, 14, 8, 13, 5, 6, 7, 3, 9, 10, 11, 4, 12.

Model response:  Here’s one plausible reconstruction that lines up the donut frosting, coffee-cup, napkin, and dark-table fragments into a coherent photo:

**1, 2, 4, 5, 9, 6, 7, 8, 10, 20, 11, 3, 12, 13, 15, 21, 14, 17, 18, 19, 16, 22, 23, 24, 25**

Read the sequence left-to-right, top-to-bottom:

* Row 1 → 1 2 4 5 9
* Row 2 → 6 7 8 10 20
* Row 3 → 11 3 12 13 15
* Row 4 → 21 14 17 18 19
* Row 5 → 16 22 23 24 25

Placing the tiles in that order restores the original image with the pink-sprinkle donut on the napkin in front, the chocolate-sprinkle donut behind it, and the coffee cup to the right, all on a dark tabletop.

Extracted answer: 1, 2, 4, 5, 9, 6, 7, 8, 10, 20, 11, 3, 12, 13, 15, 21, 14, 17, 18, 19, 16, 22, 23, 24, 25

Question: Instructions: Please complete the jigsaw puzzle shown in the image. The original image has been divided into {n}\u00d7{n} pieces and scrambled. In the image, each piece is numbered from 1 to {n\u00b2}. Your task is to determine the correct arrangement to restore the original image.\n\nQuestion: In what order should the numbered pieces be arranged to reconstruct the original image?\n\nPlease provide your answer as a sequence indicating where each numbered piece should be placed in the final arrangement (reading from left to right, top to bottom).\nFor example, 1, 16, 15, 2, 14, 8, 13, 5, 6, 7, 3, 9, 10, 11, 4, 12.

Model response: Let's solve the 6×6 jigsaw puzzle. Each piece is numbered from 1 to 36. We are to reconstruct the correct image order.

Let's work row by row:

### Analyze pieces and their probable positions

Let me match edges, colors, and context:

#### Top row (1–6):

- 1: Dog's face from the left.
- 2: Dog's eye.
- 3: Dog's snout (after eye, before window).
- 4: Car window, landscape outside.
- 5: Dog fur (likely after window)
- 6: Bright area (right top, possibly the corner area)

So, likely:  
**1, 2, 3, 4, 5, 6**

#### Second row (7–12):

- 7: Car ceiling/warning label (left top), above the window
- 8: Orange fur (could be neck or side)
- 9: Fur, dog's neck (more right than 8)
- 10: Dog's lower jaw, collar
- 11: Collar/metal ring (right of 10)
- 12: Car roof and handle (should be top right corner of 2nd row)

So, likely:  
**7, 8, 9, 10, 11, 12**

#### Third row (13–18):

- 13: Car window frame, landscape outside (left)
- 14: White/yellow fur (dog’s lower neck/chest, after window)
- 15: Fur, edge blends with outside
- 16: Branches/landscape outside (center)
- 17: Dog in car, back upper seat, some fur/ear
- 18: Dog's snout with whiskers (right, front)

So, likely:  
**13, 14, 15, 16, 17, 18**

#### Fourth row (19–24):

- 19: Car roof/ceiling (plain, leftmost top inside)
- 20: Dark, edge of car window (bottom left)
- 21: Window, lower part (mid-left)
- 22: Dog's chin, window/winder (mid)
- 23: Fur (blends with previous, right)
- 24: Inside of car door, handle (rightmost, gray)

So, likely:  
**19, 20, 21, 22, 23, 24**

#### Fifth row (25–30):

- 25: Door/window lever (leftmost, bottom)
- 26: Dog's belly/paw (blends with window)
- 27: Dog's nose & brow, ear (center to mid-right)
- 28: Background outside (tree and sky, after dog, right)
- 29: Fur (blends dog's neck, right)
- 30: Side-view mirror, background (far right)

So, likely:  
**25, 26, 27, 28, 29, 30**

#### Sixth row (31–36):

- 31: Car seat, smooth (bottom left)
- 32: Fur (dog's shoulder, next towards right)
- 33: Car ceiling, light (mid, smooth)
- 34: Car ceiling, light/roof handle (after dog, right)
- 35: Car seat backrest, pattern (mid-right)
- 36: Fur, pattern (rightmost edge, blends with seat)

So, likely:  
**31, 32, 33, 34, 35, 36**

## Final Answer

**Order:**

1, 2, 3, 4, 5, 6,  
7, 8, 9, 10, 11, 12,  
13, 14, 15, 16, 17, 18,  
19, 20, 21, 22, 23, 24,  
25, 26, 27, 28, 29, 30,  
31, 32, 33, 34, 35, 36

**This is the order to reconstruct the original image.**

Extracted answer: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
"""


demo_prompt_color = """
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: What is closest to the proportion of the color green in the image? Select from the following choices. (A) 9% (B) 13% (C) 17% (D) 21%

Model response: To estimate the proportion of the color green in the image, it's apparent that the green areas (representing grass, trees, and golf courses) constitute a significant but not dominant portion of the image. Upon reviewing the visual density of green compared to other areas, **the closest answer is (B) 13%.**

Extracted answer: B

Question: Which proportion is closest to the color green in the image? Select from the following choices. (A) 55% (B) 65% (C) 75% (D) 45%

Model response: The grass and foliage in the image dominate a significant portion. The proportion closest to the color green would likely be **(B) 65%**.

Extracted answer: B

Question: What is the HEX value of the given color in the image? Select from the following choices. (A) #E50444 (B) #040D44 (C) #E50048 (D) #E5003D

Model response: The HEX value of the given color in the image is **(A) #E50444**.

Extracted answer: A

Question: What is the HSV value of the given color in the image? Select from the following choices. (A) [22, 61, 3] (B) [78, 52, 100] (C) [78, 54, 100] (D) [76, 52, 100]

Model response: To determine the correct HSV value for the given color, we need to analyze the image or its RGB representation and convert it to HSV (Hue, Saturation, Value) format. However, since I cannot analyze images directly, I'll provide some reasoning based on the color's appearance:

This color is a light green or greenish-yellow shade. From the given choices, the choice that best aligns with such visual characteristics is:\n\n**(C) [78, 54, 100]**\n\nExplanation:\n- Hue (78): A hue value of 78 indicates a greenish shade with a slight tilt towards yellow.\n- Saturation (54): The color is not fully saturated; it is somewhat muted.\n- Value (100): The color is bright and light, as seen in the image.\n\nLet me know if you need further clarification!

Extracted answer: C

Question: What is the fraction of females facing the camera?

Model response: The fraction of females facing the camera is 0.6, which means that six out of ten females in the group are facing the camera.

Extracted answer: 0.6
"""


demo_prompt_maze = """
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: Please complete a maze game shown in the figure. Starting from the red ball in the top-left corner, navigate the maze to reach the green ball in the bottom-right corner. 'R' means move one step to the right, 'L' means move one step to the left, 'U' means move one step up, and 'D' means move one step down. Which of the following options can successfully lead out of the maze?
A. DLDRDRDRRRLDRURUDRLRDLRLULLRRDRDURDLDDRRUDUDRDUDLDUULLRUURDLLDRRRDDURDULULRRRDDLRLDRRD
B. ULULLUURLRRURDDDRLLRDRRUUDLURLLRRLLUUDLRRDRUDULRLDLRUDLLLULRRLUUDUDLRD
C. DDLDULDRDLDRDUURDRDRRDDDDDDRLURDURDULRLUDDDDRLURDDRRUULDRUUDLRURURDLDURUDLUDUUDURLURUDUUUDURDRDRLDDURLDDRDRL
D. LDRUDUDLLLRRDUDUUULRUUUUUUDDDURRRRLLDDRUUDDLDDRLDRUDDDURRLLLLRRRLRURLUUDLRU
E. LRUUURDLDDLRDLRDULURDLLDDRLUUUDLRRRLDDDURDDDDURRDRLRRDLDLRDRLDUUDRDDDUDLUDURRLRDRRUDLRUUDDRLDUDLUDRLURRLDRUDUUURRDRLURUDDUDRLR
F. No answer

Model response: To reach the green ball you must begin by moving Down, because the cell immediately to the right, left, or up from the red start-cell is a wall (black).  
Any candidate path whose second move is anything except another Down is therefore impossible, because the first column is a solid vertical corridor with no opening to the right or left until much farther down the maze.

Checking the first two moves of every option:

A. D L  ← second move goes left into a wall (invalid)  
B. U L  ← first move already goes up out of bounds (invalid)  
C. D D L  ← third move goes left into a wall (invalid)  
D. L…  ← first move goes left out of bounds (invalid)  
E. L…  ← first move goes left out of bounds (invalid)  

Since every listed path collides with a wall or leaves the maze almost immediately, none of them can solve the maze.

Correct choice:  
F. No answer

Extracted answer: F

Question: Please complete a maze game shown in the figure. Starting from the red ball in the top-left corner, navigate the maze to reach the green ball in the bottom-right corner. 'R' means move one step to the right, 'L' means move one step to the left, 'U' means move one step up, and 'D' means move one step down. Which of the following options can successfully lead out of the maze?
A. DDRRRRRRRRRRUURRDDDDLLLLDDLLLLUULLDDLLDDRRDDDDRRUURRDDRRRRUULLUURRRRDDDD
B. LUDRURLUULDDRRDUURURURULDLRLURRRULRDDLDLLRDRLUDRUDLUDLDRULULRRDRURRRLLLDURDURULRDRRRRUDRLRU
C. LLRUDURLDUUDLDDRLUUDDLULDURDULLDUDURULLRLRLUDRDLRUDDLRLRRDLRRRLDLULUUULLDDUULULLLRRRDUUULLDRRRLU
D. RDRULRRDLRLDURRDULDRUDRRDDDUDDLDRDRURRLRRLURRDULUDUULDRLLDDRLURLDRRDRRRRDLRDLDRDDDULDLLDUURUDU
E. UDDLDDRRDDLLRRRDDURURLDRDUDRRDLDUDULUDRDULRLDLDURRLDDLURUDRLLRLDUDRRUDLRDLLLRUDRDUULRLUURRRUDRRDDDDRRUUDDRRU
F. No answer

Model response: The only string that traces an uninterrupted path from the red start-cell to the green goal-cell is option A.

A.  DDRRRRRRRRRRUURRDDDDLLLLDDLLLLUULLDDLLDDRRDDDDRRUURRDDRRRRUULLUURRRRDDDD

All the other strings either try to step into a wall or go outside the maze at some point, so they cannot succeed.

Extracted answer: A

Question: Please complete a maze game shown in the figure. Starting from the red ball in the top-left corner, navigate the maze to reach the green ball in the bottom-right corner. 'R' means move one step to the right, 'L' means move one step to the left, 'U' means move one step up, and 'D' means move one step down. Which of the following options can successfully lead out of the maze?
A. RULUUDLDDDRDULLUDDLDLRULULDDRRDRURRRRDLRRLRDRDRRRRRRRDRULDRUDDDUDDRDDLUD
B. RRLLDRDRLDLDURLUURLLRULLURUDLDULLDRDURRUDDRUURLLULDDLLRRUL
C. DDDDDDDDRRUUUURRRRDDLLDDRRRRUUUURRRRDDLLDDDDRRDD
D. URUDLLRRRLULRRLLDLRLDURUDDUDRLLLLDDDURRRUDUUUUDULRLDDDDLULURLULURR
E. URRRULURURDRLDDDDDULRLDDLDRLDUDDDRDRDURUDURRUURDDLRLDUURLDDLRDLLRRURLUDRDRRDDRLDUDRR
F. No answer

Model response: The only sequence that follows open passages all the way from the red ball (top-left) to the green ball (bottom-right) is option C.  
Every other option makes an illegal move in the very first few steps (e.g., tries to go right or up from the start, where a wall blocks the way) or later crashes into a wall.

Correct choice: C.

Extracted answer: C
"""

demo_prompt_math = """
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: Which of the following points is most likely the point symmetric to point A with respect to point B?
A. point C
B. point D
C. point E
D. point F
E. point G

Model response: A point that is the image of A under point (central) symmetry about B must satisfy two conditions:  

1. B is the midpoint of the segment joining the two points, so the distances AB and BC must be the same.  
2. A, B and the image point must be collinear (lie on the same straight line).

Looking at the picture:

• A and B lie on a horizontal line.  
• Among the points to the right of B, only the points in the top row (D, C, E, G) are on that same horizontal line.  
• Of those, the one whose horizontal distance from B most closely matches the horizontal distance from A to B is point C (the second point in the row).

Hence point C best satisfies both requirements, so it is the point most likely symmetric to A with respect to B.

Answer: A. point C

Extracted answer: A

Question: As shown in the figure, it is a road map. The numbers on each road segment represent the number of minutes Xiao Ming needs to walk that segment. How many minutes is the shortest time it takes Xiao Ming to travel from point A to point D? Answer with a single number, such as 1, 2, 3.

Model response: 13

Extracted answer: 13

Question: 如图，从家到学校，如果医院禁止通行的话，从家到学校的最短路径有多少条？回答一个数字，例如1，2，3.

Model response: 我们需要计算从家到学校的最短路径数，在医院禁止通行的情况下（即路径不能经过医院所在的点）。整个路径是在网格中走，可以向右或向上移动。

### 分析：
1. **没有禁止通行情况下的路径数**：
   从家（左下角）到学校（右上角）的总移动步数是 6 步（3 向右 + 3 向上）。这些步数可以通过排列组合计算，有：
   \[
   C(6, 3) = \frac{6!}{3! \cdot 3!} = 20
   \]
   所以总路径数为 **20**。

2. **禁止通行因医院影响的路径数**：
   医院所在点是网格中间的一个点（第2行，第2列）。我们需要计算**经过医院的路径**数量，然后从总路径数中减去它。

   - **家到医院路径数**：
     从家到医院需要移动 2 步（1 向右 + 1 向上），路径数为：
     \[
     C(2, 1) = \frac{2!}{1! \cdot 1!} = 2
     \]

   - **医院到学校路径数**：
     从医院到学校需要移动 4 步（2 向右 + 2 向上），路径数为：
     \[
     C(4, 2) = \frac{4!}{2! \cdot 2!} = 6
     \]

   - **经过医院的路径总数**：
     经过医院的路径总数为家到医院路径数乘以医院到学校路径数：
     \[
     2 \times 6 = 12
     \]

3. **禁止通行后的路径数**：
   总路径数减去经过医院的路径数：
   \[
   20 - 12 = 8
   \]

### 结论：
从家到学校的最短路径有 **8** 条（在医院禁止通行的情况下）。

Extracted answer: 8

Question: 如图，工厂A和工厂B，位于两条公路OC、OD之间的地带，现要建一座货物中转站P．若要求中转站P到两条公路OC、OD的距离相等，且到工厂A和工厂B的距离之和最短。如果线段HI之间的距离是3km，该最短距离之和大约是（ ）。
A. 3km
B. 4km
C. 5km
D. 6km
E. 7km
F. 8km

Model response: 题目是关于构建一个货物中转站，使其满足两个条件：  
1. 到两条公路OC和OD的距离相等；  
2. 到两工厂A和B的距离和最短。  

这个问题可以通过反射法解决。工厂B的反射点记为B′，即以公路OD为对称轴得到的B的对称点。

中转站的位置P应位于两条公路的角平分线上，并使得**P到工厂A的距离**加上**P到工厂B的距离**最短。这等效于找到点P，使得P到A和B′的距离最短。因为角平分线始终满足两条公路的距离相等，问题变为寻找P到线段A-B′的最短距离。

### 解答步骤：
1. 假设HI的距离为3km。
2. 此图为一几何图形，假设工厂A到路OD的垂直距离，以及工厂B与两公路的相对关系，可以得到最短路径理论值大约估计。

通过计算，我们得到的最小距离大约为：**5km**。

### 答案：
**C. 5km**


Extracted answer: C

Question: As shown in the figure, how many intersection points are there between the extension of EF and the trigonometric function f?

Model response: To determine the number of intersection points between the extension of line segment \( EF \) and the trigonometric curve \( f \), we analyze how the straight line (segment \( EF \), extended) intersects the periodic trigonometric function depicted in the graph.

Upon examining the graph, the extended \( EF \) line crosses the curve \( f \) at multiple points as the trigonometric function oscillates periodically. By counting the intersections visually from the provided image:

- The line crosses \( f \) at a total of **10 points**.




Extracted answer: 10
"""


demo_prompt_symbolic = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: Which pair of lines are parallel?
A.ab and cd
B.ef and gh
C.ab and gh
D.ef and cd
E.none of the above
 This is a multiple-choice question, and you need to select more than one option. Write your final answer using consecutive letters, such as ABC, CD, or BC.

Model response: CD

Extracted answer:CD

Question: How many shapes are there in this image? Provide your final answer as an integer, such as 1, 2, 3.

Model response: The image contains 3 types of shapes:
1. Circles
2. Triangles
3. Squares

Thus, the final answer is **3**.

Extracted answer: 3

Question: How many nested squares are there in this image?
A.12
B.14
C.13
D.15
E.16

Model response: To determine the number of nested squares in this image, let's count each square visually from the innermost one to the outermost one.

Starting from the center, there is a total of **16 nested squares** in this image.

The correct answer is:

**E. 16**

Extracted answer: E
'''


demo_prompt_word_search = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: 图中情字在出现在第几行第几列？最后答案输出两个数字，第一个数字代表从上往下多少行，第二个数字代表从左往右列。例如[1, 2]代表第一行第二列

Model response: 在这个图片中，“情”字重复排列组成了一个图案。为了找出其中不同的地方，请观察每个字并进行逐个对比。让我仔细分析一下图片：

答案是：

第 **3** 行，第 **6** 列。  
答案为：[3, 6]

Extracted answer: [3, 6]

Question: 图中有多少个犬字？回答一个数字，例如1，2，3

Model response: 图中有一个“犬”字

Extracted answer: 1

Question: How many times does the number 5 appear in this image? Answer with an integer, such as 1,2,3.

Model response: The number 5 does not appear in this image. The image contains the number 8 repeatedly, with some number 3s dispersed throughout. Therefore, the answer is **0**.

Extracted answer: 0

Question: In the figure, in which row and column does the letter Z appear? The final answer should output two number list. The first number represents the row count from top to bottom, and the second number represents the column count from left to right. For example, [1, 2] means the first row and the second column.

Model response: The letter "Z" appears in **row 36** and **column 69**. 

So, the answer is:

**[36, 69]**.

Extracted answer: [36, 69]
'''


demo_prompt_rotation_game = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: How many degrees should you rotate this image CLOCKWISE to restore it to its original orientation?

A. 10°
B. 355°
C. 40°
D. 5°
E. 25°
F. 55°

Model response: To restore the image to its original orientation, you need to determine how much it is tilted. The image appears to be rotated **40° COUNTERCLOCKWISE**. To undo this rotation, you need to rotate it **40° CLOCKWISE**.  

Thus, the correct answer is:  
**C. 40°**

Extracted answer: C

Question: How many degrees should you rotate this image CLOCKWISE to restore it to its original orientation?

A. 205°
B. 220°
C. 175°
D. 185°
E. 190°
F. 235°

Model response:Looking at the image, it appears that it has been rotated **counterclockwise**. To restore the image to its upright orientation, we need to rotate it **clockwise**.

From the angle of rotation of the image, this looks like about **175° counterclockwise**. Thus, to restore it, the image should be rotated **185° clockwise**.

The correct answer is:  
**D. 185°**.

Extracted answer: D

Question: How many degrees should you rotate this image CLOCKWISE to restore it to its original orientation?

A. 25°
B. 60°
C. 30°
D. 45°
E. 15°
F. 75°

Model response:By eye, the picture has been turned almost exactly into a “diamond” shape – the long edges of the buildings (which should be vertical) now run along a perfect diagonal of the image. That characteristic diamond outline is what you get when an ordinary rectangular photo is spun through a quarter-turn of a right angle, i.e., 45°.  

So to bring the scene back to its normal upright orientation you would need to rotate it 45° in the opposite (clockwise) direction.  

Answer: D. 45°

Extracted answer: D

Question: How many degrees should you rotate this image CLOCKWISE to restore it to its original orientation?

A. 285°
B. 240°
C. 255°
D. 270°
E. 235°
F. 225°

Model response: The picture is leaning about 105° counter-clockwise from upright.  
To bring it back you could instead rotate it the other way – clockwise – by

360° – 105° ≈ 255°.

Among the given choices, 255° is the only value that does this.

Answer: 255°


Extracted answer: C
'''



demo_prompt_spot_difference = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: **Task Description:**
Given two images of identical dimensions, each divided by thin white lines into n rows and m columns, resulting in n×m small patches. The numbering rules are as follows:

1. Patches are numbered from 1 to n×m.
2. Numbering follows row-major order: the first row from left to right is 1, 2, …, m; the first patch of the second row is m+1, and so on.

The i-th patch in the left image corresponds to the i-th patch in the right image. Your tasks are:

1. Identify all objects or regions that differ between the two images.
2. Return a list of patch indices occupied by each differing object.

   * If an object spans multiple adjacent patches, include all those patch indices.
3. Finally, output a deduplicated, ascending-sorted list of indices representing every patch that contains a difference.

---

**Output Format:**

```json
{
  "different_patches": [i1, i2, i3, …]
}
```

* `different_patches`: an array of integers containing all patch indices where the two images differ, deduplicated and sorted in ascending order.

---

**Example:**
Suppose n=3 and m=4, giving 12 patches total. If patches 2, 5, 6, and 10 differ between the left and right images, the output should be:

```json
{
  "different_patches": [2, 5, 6, 10]
}
```

---

**Problem:**
Output the list of patch indices where the two images differ.
Note that in this image, n is 4 and m is 3

Model response:  To solve this problem, we need to identify the patches in the two images that have differences. Here's how we can achieve this:

---

### **Step-by-Step Solution**

1. **Understand the Grid Dimensions**:
   The images are divided into 4 rows and 3 columns (n=4, m=3), resulting in a total of \( n \times m = 4 \times 3 = 12 \) patches. The patches are numbered row-major order:
   - Row 1: Patches \( [1, 2, 3] \)
   - Row 2: Patches \( [4, 5, 6] \)
   - Row 3: Patches \( [7, 8, 9] \)
   - Row 4: Patches \( [10, 11, 12] \)

2. **Identify Differences**:
   Analyze the images and locate regions with visual differences. Based on the provided example:
   - Patch 2: Difference found near the left equipment control panel.
   - Patch 6: Difference visible with the purple liquid container (added in the right image).
   - Patch 7: Difference in the bed near its corner.
   - Patch 11: Difference near the lamp above the bed.

3. **Compile Results**:
   Collect all differing patch indices and ensure they are unique and sorted in ascending order. From steps above, the patches with differences are \( [2, 6, 7, 11] \).

4. **Output the Result**:
   Return the patch indices in JSON format.

---

### **Output**

The final deduplicated and sorted result is:

```json
{
  "different_patches": [2, 6, 7, 11]
}
```

This output lists all patches where the left and right images differ.


Extracted answer: [2, 6, 7, 11]

Question: **Task Description:**
Given two images of identical dimensions, each divided by thin white lines into n rows and m columns, resulting in n×m small patches. The numbering rules are as follows:

1. Patches are numbered from 1 to n×m.
2. Numbering follows row-major order: the first row from left to right is 1, 2, …, m; the first patch of the second row is m+1, and so on.

The i-th patch in the left image corresponds to the i-th patch in the right image. Your tasks are:

1. Identify all objects or regions that differ between the two images.
2. Return a list of patch indices occupied by each differing object.

   * If an object spans multiple adjacent patches, include all those patch indices.
3. Finally, output a deduplicated, ascending-sorted list of indices representing every patch that contains a difference.

---

**Output Format:**

```json
{
  "different_patches": [i1, i2, i3, …]
}
```

* `different_patches`: an array of integers containing all patch indices where the two images differ, deduplicated and sorted in ascending order.

---

**Example:**
Suppose n=3 and m=4, giving 12 patches total. If patches 2, 5, 6, and 10 differ between the left and right images, the output should be:

```json
{
  "different_patches": [2, 5, 6, 10]
}
```

---

**Problem:**
Output the list of patch indices where the two images differ.
Note that in this image, n is 4 and m is 3

Model response: To determine the differing patches between the two images, we observe the changes in specific sections of the divided images. Each patch is indexed following a row-major order, as described initially.

### Observations
1. **Patches to Analyze:**  
   The images are split into 4 rows and 3 columns, giving a total of \( n \times m = 4 \times 3 = 12 \) patches, numbered from 1 to 12.  

2. **Identified Differences (visual observation):**  
   - Patch **2**: The painting above the bed changes (green paint strokes differ).  
   - Patch **3**: The TV screen shows changes.  

### Output
The indexes of patches where differences are detected are deduplicated and sorted in ascending order.

```json
{
  "different_patches": [2, 3]
}
```

Extracted answer: [2, 3]

Question: **Task Description:**
Given two images of identical dimensions, each divided by thin white lines into n rows and m columns, resulting in n×m small patches. The numbering rules are as follows:

1. Patches are numbered from 1 to n×m.
2. Numbering follows row-major order: the first row from left to right is 1, 2, …, m; the first patch of the second row is m+1, and so on.

The i-th patch in the left image corresponds to the i-th patch in the right image. Your tasks are:

1. Identify all objects or regions that differ between the two images.
2. Return a list of patch indices occupied by each differing object.

   * If an object spans multiple adjacent patches, include all those patch indices.
3. Finally, output a deduplicated, ascending-sorted list of indices representing every patch that contains a difference.

---

**Output Format:**

```json
{
  "different_patches": [i1, i2, i3, …]
}
```

* `different_patches`: an array of integers containing all patch indices where the two images differ, deduplicated and sorted in ascending order.

---

**Example:**
Suppose n=3 and m=4, giving 12 patches total. If patches 2, 5, 6, and 10 differ between the left and right images, the output should be:

```json
{
  "different_patches": [2, 5, 6, 10]
}
```

---

**Problem:**
Output the list of patch indices where the two images differ.
Note that in this image, n is 5 and m is 4

Model response: To identify the patches containing differences between the two images, we visually inspect and compare each corresponding patch across the left and right images. The goal is to note differences and output the indices of all patches that contain any differences. Here's the solution:

---

### Step-by-Step Process:
1. **Define dimensions**: The images have `n=5` rows and `m=4` columns, resulting in `n * m = 20` patches numbered sequentially in row-major order:
   - Row 1: patches 1, 2, 3, 4
   - Row 2: patches 5, 6, 7, 8
   - Row 3: patches 9, 10, 11, 12
   - Row 4: patches 13, 14, 15, 16
   - Row 5: patches 17, 18, 19, 20

2. **Examine differences**: Compare each corresponding patch between the left and right images visually:
   - **Patch 2:** Curtain is torn in the left image; intact in the right.
   - **Patch 6:** The medicine cabinet's handle is missing in the left image; present in the right.
   - **Patch 13:** A duck is present in the left image but missing in the right.
   - **Patch 14:** There's an extra puddle in the left image, which is absent in the right.
   
3. **Output indices**: Combine all differing patches into a deduplicated and ascending-sorted list.

---

### Final Output:

```json
{
  "different_patches": [2, 6, 13, 14]
}
```

These indices represent all patches where the two images differ visually.

Extracted answer: [2, 6, 13, 14]

Question: This is a spot-the-difference game. How many places differ between the left and right images?Please provide your answer as an integer, such as 1, 2, 3. Please provide your answer as an integer, such as 1, 2, 3.

Model response: The number of differences between the left and right images is **6**.

Extracted answer: 6
'''

demo_prompt_visual_search = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: What is the price of 空芯菜炒め in the shop shown in the picture? Answer with an integer (yen). ( yen)

Model response: The price of 空芯菜炒め in the shop shown in the picture is **970 yen**.

Extracted answer: 970

Question: 大江團鱼的价格是（）。填写一个整数

Model response: 从照片中可以看到菜单上的“大江團鱼”价格是 **168** 元

Extracted answer: 168

Question: What is the price of LATTE? Answer with a number to two decimal places, e.g., 1.11.

Model response: The price of a latte is **4.45**.

Extracted answer: 4.45

Question: What is the phone number of the refrigerated truck company shown in the picture?
A) 02-3539-2322
B) 03-3534-2322
C) 02-3534-2322
D) 03-3539-2322
E) 02-3584-2322
F) 03-3834-2322

Model response: The phone number displayed on the refrigerated truck in the image is **03-3539-2322**.

Correct answer: **D) 03-3539-2322**.

Extracted answer: D

Question: What color is the hat worn by the person with a cane in the picture?
A) Red
B) Blue
C) Yellow
D) Green
E) Black

Model response: The person with a cane in the picture is wearing a **black hat**. 

Correct answer: **Black**.

Correct answer: E
'''

demo_prompt_refcoco = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: Which of the following values is the closest to the proportion of the image occupied by girl in pink?
A: 23%
B: 39%
C: 31%
D: 15%
E: 47%
F: 7%


Model response: To estimate the proportion of the image occupied by the girl in pink, we focus on the area her body and tennis racket appear to take up in comparison to the overall image.

The girl in pink occupies roughly 31% of the image space when considering her body size relative to the entire group and background.

Answer: **C: 31%**

Extracted answer: C

Question: Which of the following values is the closest to the proportion of the image occupied by left?
A: 39%
B: 55%
C: 31%
D: 15%
E: 23%
F: 47%

Model response: To determine the proportion of the image occupied by the left side, visually comparing the left and right divisions is useful. The left side appears to occupy approximately **half of the total image area**, which is close to **47%** of the image.

Thus, the closest value is:

**F: 47%.**

Extracted answer: F

Question: Which of the following values is the closest to the proportion of the image occupied by upper right glas?
A: 38%
B: 14%
C: 22%
D: 46%
E: 30%
F: 6%

Model response: The proportion of the image occupied by the upper-right glass appears closest to **6% **.

Extracted answer: F
'''

demo_prompt_contrast = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: How many vehicles are in the image?

Model response: The image shows four vehicles parked.

Extracted answer: 4 

Question: How many cans are in the image?

Model response: The image is very dark, making it difficult to clearly identify the objects within. From what can be observed, there appear to be glass jars rather than cans. Based on their shape, it seems there might not be cans in the image. If you're looking for more accuracy or detail, consider brightening the image.

Extracted answer: 0

Question: What are the numbers on the three diving platforms in the image?
A 1 2 3
B 2 3 4
C 11 12 13 
D 3 4 5
E 12 13 14

Model response: The numbers on the three diving platforms in the image are **2, 3, and 4**, corresponding to option **B 2 3 4**.

Extracted answer: B

Question: How many people are holding the first banner?

Model response: There are four people holding the first banner in the image.

Extracted answer: 4
'''

demo_prompt_instrument = '''
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.

Question: What is the reading of the second gauge from the left in kg/cm²? Provide one decimal place (e.g., 1.1).

Model response: Based on the provided images, here is the reading of the second gauge from the left:

The gauge's needle is pointing slightly past the 11 mark. The unit on the gauge is kg/cm².

The reading is **11.1** kg/cm².

Extracted answer: 11.1

Question: The second-hand reading on the stopwatch in the image falls within which of the following intervals?
A 5-6
B 6-7
C 7-8
D 8-9
E 9-10

Model response: Based on the image of the stopwatch, let's analyze the position of the hands.

1.  **Identify the second hand:** The long, thin, blue hand is the second hand.
2.  **Read the main dial:** The main dial is marked with numbers 10, 20, 30 (implied), 40, 50, and 60, representing the seconds. The longer lines between these numbers represent individual seconds.
3.  **Determine the position:** The second hand is pointing past the long mark for the number 8, but it has not yet reached the long mark for the number 9.
4.  **Conclusion:** Therefore, the reading on the second hand is a value greater than 8 and less than 9.

Looking at the given options:
A) 5-6
B) 6-7
C) 7-8
D) 8-9
E) 9-10

The reading falls within the interval **8-9**.

The correct option is **D**.


Extracted answer: D

Question: The reading of the measuring cylinder in the image is:
A 6.6
B 6.7
C 6.8
D 6.9
E 6.5
F 7

Model response: To read the measuring cylinder, follow these steps:

1.  **Identify the major scale markings:** We can clearly see the number '6' as a major marking. Above it, we see part of '8'. This implies the major markings are at whole number intervals (6, 7, 8, etc.).
2.  **Determine the value of each minor division:** Look at the lines between '6' and the implied '7' (the long line above '6' where the '8' is visible is 8, so halfway between 6 and 8 is 7). Between '6' and the next major line (which would be '7'), there are 10 smaller intervals. This means each small line represents 0.1 unit.
    *   So, the line marked '6' is 6.0.
    *   The first small line above 6 is 6.1.
    *   The second small line above 6 is 6.2.
    *   The third small line above 6 is 6.3.
    *   The fourth small line above 6 is 6.4.
    *   The fifth small line above 6 is 6.5 (this line is slightly longer than the others, indicating a half-unit mark).
    *   The sixth small line above 6 is 6.6.
    *   The seventh small line above 6 is 6.7.
    *   The eighth small line above 6 is 6.8.
    *   The ninth small line above 6 is 6.9.
    *   The tenth small line above 6 is 7.0 (the next major line).
3.  **Read the bottom of the meniscus:** For liquids like water, you read the volume at the bottom of the meniscus (the curve of the liquid surface).
    *   Looking at the image, the bottom of the meniscus aligns perfectly with the seventh small line above the '6' mark.

Therefore, the reading is 6.7.

Comparing this with the given options:
A 6.6
B 6.7
C 6.8
D 6.9
E 6.5
F 7

The correct reading is 6.7.

The final answer is $\boxed{\text{6.7}}$.

Extracted answer: B

Question: The reading of the measuring cylinder in the image is:
A 4.6
B 4.8
C 5
D 5.2
E 5.4
F 5.6

Model response: To read the measuring cylinder, follow these steps:

1.  **Identify the major markings:** The numbers clearly visible are 3, 5, 7, 9, 11, 13, 15. These represent increments of 2 units (e.g., from 5 to 7 is 2 units).
2.  **Determine the value of the unnumbered long lines:** Between 5 and 7, there's a longer line without a number. This line represents the value halfway between 5 and 7, which is 6. Similarly, the line between 7 and 9 represents 8, and so on.
3.  **Determine the value of the smallest subdivisions:** Between any two consecutive whole numbers (like 5 and 6, or 6 and 7), there are 4 smaller lines, creating 5 subdivisions. This means each small subdivision represents 1 unit / 5 subdivisions = 0.2 units.
4.  **Locate the meniscus:** The liquid in the cylinder forms a concave meniscus. The reading should always be taken at the bottom of this meniscus.
5.  **Read the volume:**
    *   The liquid level is above the '5' mL mark.
    *   Count the small subdivisions above the '5' mL mark until you reach the bottom of the meniscus.
    *   The first small mark above 5 is 5 + 0.2 = 5.2 mL.
    *   The second small mark above 5 is 5 + 0.2 + 0.2 = 5.4 mL.
    *   The bottom of the meniscus aligns precisely with the second small mark above the '5' mL line.

Therefore, the reading is 5.4 mL.

The final answer is $\boxed{\text{5.4}}$

Extracted answer: E

Question: What is the reading of the Vernier caliper in the image in centimeters?
A 5.9
B 5.92
C 5.94
D 5.95
E 5.96
F 5.97
G None of the above

Model response: To determine the reading of the Vernier caliper, follow these steps:

1.  **Read the Main Scale (MS):**
    *   Look at the zero mark of the Vernier scale (the movable scale).
    *   Identify the last complete millimeter mark on the main scale that the Vernier zero mark has passed.
    *   In the image, the Vernier zero mark has passed the 5 cm mark.
    *   It has also passed the 9th small division after 5 cm. Each small division represents 1 millimeter (0.1 cm).
    *   So, the main scale reading is 5.9 cm.

2.  **Read the Vernier Scale (VS):**
    *   Find the mark on the Vernier scale that perfectly aligns with any mark on the main scale.
    *   Looking closely at the Vernier scale, the 5th mark (labeled '5' on the lower scale) aligns perfectly with a mark on the main scale.
    *   The least count (LC) of a standard Vernier caliper with 10 divisions on the Vernier scale is usually 0.01 cm (or 0.1 mm). This is calculated as (1 Main Scale Division - 1 Vernier Scale Division). Here, 1 MSD = 1mm = 0.1cm. 10 VSD = 9 MSD, so 1 VSD = 0.9 MSD = 0.9 mm = 0.09 cm. LC = 1 MSD - 1 VSD = 0.1 cm - 0.09 cm = 0.01 cm.
    *   Since the 5th mark aligns, the Vernier scale reading is 5 * LC = 5 * 0.01 cm = 0.05 cm.

3.  **Calculate the Total Reading:**
    *   Total Reading = Main Scale Reading + Vernier Scale Reading
    *   Total Reading = 5.9 cm + 0.05 cm
    *   Total Reading = 5.95 cm

Comparing this to the given options:
A 5.9
B 5.92
C 5.94
D 5.95
E 5.96
F 5.97
G None of the above

The calculated reading is 5.95 cm, which matches option D.

The final answer is $\boxed{\text{5.95}}$

Extracted answer: D

Question: What is the reading of the Vernier caliper in the image in centimeters?
A 3.2
B 3.21
C 3.22
D 3.23
E 3.25
F 3.26
G None of the above

Model response: The Vernier caliper shows a reading of **3.23 cm**. 

The main scale shows **3.2 cm**, and on the Vernier scale, the line corresponding to **3** aligns perfectly with a line on the main scale. Hence the reading is **3.23 cm**.

So the correct answer is:
**D 3.23**

Extracted answer: D

Question: What is the reading of the Vernier caliper in the image in centimeters?

Model response: From the image, the Vernier caliper reading is approximately **2.39 cm (or 23.9 mm)**.

- **Main Scale Reading**: The "2" on the main scale is just before the 0 mark of the Vernier scale, which indicates 2 cm.
- **Vernier Scale Reading**: The 9th line on the Vernier scale aligns with a line on the main scale, adding 0.09 cm (or 0.9 mm).

Adding these together:
- Main scale: 2 cm
- Vernier scale: 0.09 cm  
**Total = 2.39 cm**

Extracted answer: 2.39
'''